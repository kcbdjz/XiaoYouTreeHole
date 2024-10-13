// pages/chat/chat.js

const app = getApp();
//引入插件：微信同声传译
const plugin = requirePlugin('WechatSI');
//获取全局唯一的语音识别管理器recordRecoManager
const manager = plugin.getRecordRecognitionManager();


Page({
  data: {
      // 文字框内容
      content: '',
      // 当前登录者信息
      login: {
          id: '2023',
          user: '用户',
          avatar: '/img/avatar.jpg'
      },
      ai: {
        id: '2022',
        user: '小优',
        avatar: '/img/home-person.jpg'
    },
      time: {
          flag : 0
  },
      // 聊天信息
      chatList: [
      {
          msgId: '2022',
          nickname: '小优',
          avatar: '/img/home-person.jpg',
          message: '你好',
          type: 'text',
          date: '05-02 14:24' // 每隔5分钟记录一次时间
      }
      ],
      //语音
      recordState: false, //录音状态
      src:'', //存放语音路径
      word:'', //存放需要转语音的文字
  },
  onLoad() {
    this.scrollToBottom();

    //识别语音
    this.initRecord();
  },
  onReady(){
    var date = new Date
    this.data.time.flag = date.getTime()
    this.data.chatList[0].date = this.formatTime(date.getTime())

    //创建内部 audio 上下文 InnerAudioContext 对象。
    this.innerAudioContext = wx.createInnerAudioContext();
    this.innerAudioContext.onError(function (res) {
      console.log(res);
      wx.showToast({
        title: '语音播放失败',
        icon: 'none',
      })
    })
  },
  // 输入监听
  inputClick(e) {
      this.setData({
          content: e.detail.value
      })
  },
  // 发送监听
  sendClick() {
      var that = this;
      var list = this.data.chatList;
      // 获取当前时间
      var date = new Date();
      // 组装数据
      var msg = {
          msgId: this.data.login.id,
          nickname: this.data.login.user,
          avatar: this.data.login.avatar,
          message: this.data.content,
          type: 'text',
          date: this.formatTime(date.getTime())
      }
      if (date.getTime()-this.data.time.flag<300000) {
        msg.date=null
      }

      this.data.time.flag=date.getTime()

      this.setData({
          chatList: list.concat(msg)
      }, () => {
          that.scrollToBottom();
          that.setData({
              content: ''
          })
      })
      // 向后端发送数据
      wx.request({
        url: app.globalData.FLASK+'/score',
        data: {
          txt:JSON.stringify(msg.message)
        },
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded',
          'chartset': 'utf-8'
        },
        success: function (res) {
          console.log(res)
          if(res.data.result.type=='text'){
            that.acceptClick(res.data.result.text);
            that.wordYun(res.data.result.text)
          }else{
            var u = res.data.result.video[1]
            u = u.trim()
            wx.navigateTo({
              url: '/pages/video/video?src='+app.globalData.HDFS+'/webhdfs/v1'+u,
            })
          }
       },
       fail:function(res){
         console.log(res)
       }
      })
  },

  acceptClick(text) {
    var that = this;
    var list = this.data.chatList;
    // 获取当前时间
    var date = new Date();
    // 组装数据
    var msg = {
        msgId: this.data.ai.id,
        nickname: this.data.ai.user,
        avatar: this.data.ai.avatar,
        message: text,
        type: 'text',
        date: this.formatTime(date.getTime())
    }
    if (date.getTime()-this.data.time.flag<500000) {
      msg.date=null
    }

    this.data.time.flag=date.getTime()

    this.setData({
      chatList: list.concat(msg)
  }, () => {
      that.scrollToBottom();
      that.setData({
          content: ''
      })
  })
},
  // 滑动到最底部
  scrollToBottom() {
      setTimeout(() => {
          wx.pageScrollTo({
              scrollTop: 200000,
              duration: 3
          });
      }, 600)
  },
  formatTime(timeNum){
    var date = new Date();
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = date.getHours();
    var minu = date.getMinutes();
    var now1 = month < 10 ? '0' + month : month;
    var now2 = day < 10 ? '0' + day : day;
    return now1 + '-' + now2 + ' ' + hour + ':' + minu
  },

  //识别语音 -- 初始化
  initRecord: function () {
    const that = this;
    // 有新的识别内容返回，则会调用此事件
    manager.onRecognize = function (res) {
      console.log(res)
    }
    // 正常开始录音识别时会调用此事件
    manager.onStart = function (res) {
      console.log("成功开始录音识别", res)
    }
    // 识别错误事件
    manager.onError = function (res) {
      console.error("error msg", res)
    }
    //识别结束事件
    manager.onStop = function (res) {
      console.log('..............结束录音')
      console.log('录音临时文件地址 -->' + res.tempFilePath); 
      console.log('录音总时长 -->' + res.duration + 'ms'); 
      console.log('文件大小 --> ' + res.fileSize + 'B');
      console.log('语音内容 --> ' + res.result);
      if (res.result == '') {
        wx.showModal({
          title: '提示',
          content: '听不清楚，请重新说一遍！',
          showCancel: false,
          success: function (res) {}
        })
        return;
      }
      // var text = that.data.content + res.result;
      that.setData({
        content: res.result
      })
    }
  },
  //语音  --按住开始
  touchStart: function (e) {
    this.setData({
      recordState: true  //录音状态
    })
    // 语音开始识别
    manager.start({
      lang: 'zh_CN',// 识别的语言，目前支持zh_CN en_US zh_HK sichuanhua
    })
  },
  //语音  --松开结束
  touchEnd: function (e) {
    this.setData({
      recordState: false
    })
    // 语音结束识别
    manager.stop();
  },
  // 文字转语音
  wordYun:function (e) {
    var that = this;
    var content
    if (typeof(e) == 'string'){
      content = e;
    }else{
      console.log(e)
      content = e.currentTarget.dataset.word;
    }
    plugin.textToSpeech({
      lang: "zh_CN",
      tts: true,
      content: content,
      success: function (res) {
        console.log(res);
        console.log("succ tts", res.filename);
        that.setData({
          src: res.filename
        })
        that.yuyinPlay();
 
      },
      fail: function (res) {
        console.log("fail tts", res)
      }
    })
  },
  
  //播放语音
  yuyinPlay: function (e) {
    if (this.data.src == '') {
      console.log(暂无语音);
      return;
    }
    this.innerAudioContext.src = this.data.src //设置音频地址
    this.innerAudioContext.play(); //播放音频
  },
 
  // 结束语音
  end: function (e) {
    this.innerAudioContext.pause();//暂停音频
  },
})


