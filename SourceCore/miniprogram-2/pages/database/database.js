// pages/database/database.js

const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    list: [
  ]
  },
  setList(res){
    var that = this
    console.log(res)
        console.log(that.data)
        var temp = that.data.list
        temp = res.data.list
        that.setData({
          list: temp
        })
  },
  gotovideo(e){
    console.log(e)
    var content = e.currentTarget.dataset.video;
    content = content.trim()
    console.log(content)
    wx.navigateTo({
      url: '/pages/video/video?src='+app.globalData.HDFS+'/webhdfs/v1'+content,
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
    var that = this
    wx.request({    
      url: app.globalData.FLASK+'/video',    //请求与后端连接
      method:"GET",
      data:{
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
        that.setList(res)
      }
    })
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