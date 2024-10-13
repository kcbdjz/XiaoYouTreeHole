// pages/register/register.js

const app = getApp();

Page({

  /**
   * 页面的初始数据
   */
  data: {
    jin:true,
    username:'',
    name:'',
    password:''
  },
 
//以下同样是监听，和对注册按钮的设置
  usernameInput:function(e){
    var val = e.detail.value;
      this.setData({
        username:val
      })
      if(val!='' && this.data.password!='' && this.data.name!=''){
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
 
  nameInput:function(e){
    var val = e.detail.value;
      this.setData({
        name:val
      })
      if(val!='' && this.data.username!='' && this.data.password!=''){
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
      if(val!='' && this.data.username!='' && this.data.name!=''){
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
 
//同登录类似
post:function(){
  var that = this
  console.log(that.data.name)
  console.log(that.data.username)
  console.log(that.data.password)
  wx.request({
      url: app.globalData.FLASK+'/register',
      method:"POST",
      data:{
        name:JSON.stringify(that.data.name),
        username:JSON.stringify(that.data.username),
        password:JSON.stringify(that.data.password)
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
          console.log(res);
          if(res.data.text=="注册成功"){
            console.log("注册成功");
            wx.showToast({
              title: '注册成功',
              icon: 'success',
              duration: 1000//持续的时间
            })
            setTimeout(function () {
              wx.switchTab({
                url: '/pages/home/home',
              })
             }, 1000)
          }
          else{
            console.log("账号存在");
            wx.showToast({
              title: '账号存在',
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