var fallbackRankingData = require("./data/rankings.js");

var CACHE_KEY = "agent-ranking-latest-v1";
var REMOTE_DATA_URL = "https://yuxiaoyi24.github.io/ai-agent-open-source-ranking/data/latest.json";

function isValidRankingData(data) {
  return Boolean(
    data &&
    data.schema_version === 1 &&
    data.date &&
    Array.isArray(data.modules) &&
    Array.isArray(data.projects)
  );
}

function isNotOlder(candidate, current) {
  return !current || String(candidate.date) >= String(current.date);
}

App({
  globalData: {
    appName: "AI Agent 开源技术周榜",
    dataSource: "GitHub 开源项目周榜",
    rankingData: fallbackRankingData,
    rankingSource: "内置快照",
  },

  onLaunch: function () {
    try {
      var cached = wx.getStorageSync(CACHE_KEY);
      if (isValidRankingData(cached) && isNotOlder(cached, this.globalData.rankingData)) {
        this.globalData.rankingData = cached;
        this.globalData.rankingSource = "本地缓存";
      }
    } catch (error) {
      console.warn("读取周榜缓存失败", error);
    }
  },

  getRankingData: function () {
    return this.globalData.rankingData;
  },

  refreshRankingData: function (callback) {
    var self = this;
    wx.request({
      url: REMOTE_DATA_URL + "?t=" + Date.now(),
      method: "GET",
      timeout: 10000,
      success: function (response) {
        var data = response.data;
        if (response.statusCode !== 200 || !isValidRankingData(data)) {
          callback({ updated: false, data: self.globalData.rankingData, source: self.globalData.rankingSource });
          return;
        }
        if (isNotOlder(data, self.globalData.rankingData)) {
          self.globalData.rankingData = data;
          self.globalData.rankingSource = "在线同步";
          try {
            wx.setStorageSync(CACHE_KEY, data);
          } catch (error) {
            console.warn("写入周榜缓存失败", error);
          }
        }
        callback({ updated: true, data: self.globalData.rankingData, source: self.globalData.rankingSource });
      },
      fail: function () {
        callback({ updated: false, data: self.globalData.rankingData, source: self.globalData.rankingSource });
      },
    });
  },
});
