// pages/login/login.js

const app = getApp();

Page({

  /**
   * 页面的初始数据
   */
  data: {
    jin:true,
    username:'',
    password:'',
    longin:true
  },
 
//以下是监听输入框的数据并获取，和对登录按钮的设置：只有当输入框中都有数据时才能点击
  usernameInput:function(e){
    var val = e.detail.value;
      this.setData({
        username:val
      })
      if(val!='' && this.data.password!=''){
        this.setData({
          jin:false
        })
      }
      else{
        this.setData({
          jin:true
        })
      }
  },
 
  passwordInput:function(e){
    var val = e.detail.value;
      this.setData({
        password:val
      })
      if(val!='' && this.data.username!=''){
        this.setData({
          jin:false
        })
      }
      else{
        this.setData({
          jin:true
        })
      }
  },
 
  post:function(){
    var that = this
    console.log(that.data.username)
    console.log(that.data.password)
    wx.request({    
      url: app.globalData.FLASK+'/login',    //请求与后端连接
      method:"POST",
      data:{
        username:JSON.stringify(that.data.username),
        password:JSON.stringify(that.data.password)
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
          console.log(res);
          if(res.data.text=='登录成功'){    //后端对比数据后，判断正误
            console.log("登录成功")
            wx.showToast({
              title: '登录成功',
              icon: 'success',
              duration: 1000//持续的时间
            })
            setTimeout(function () {
              wx.switchTab({
                // 跳转页面
                url: '/pages/home/home',
              })
             }, 1000)
          }
          else{
            console.log("登录失败")
            wx.showToast({
              title: '账号或密码错误',
              icon: 'error',
              duration: 1000//持续的时间
            })
          }
      } 
    })
  },
  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})