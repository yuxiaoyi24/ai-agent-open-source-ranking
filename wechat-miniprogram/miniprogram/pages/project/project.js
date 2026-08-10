var format = require("../../utils/format.js");
var app = getApp();

Page({
  data: { project: null, baseline: false },

  onLoad: function (options) {
    var slug = decodeURIComponent(options.slug || "");
    var rankingData = app.getRankingData();
    var project = rankingData.projects.filter(function (item) { return item.slug === slug; })[0];
    if (!project) {
      wx.showToast({ title: "项目暂未收录", icon: "none" });
      return;
    }
    this.setData({
      baseline: Boolean(rankingData.previous_snapshot_date),
      project: Object.assign({}, project, {
        starsLabel: format.formatStars(project.stars),
        deltaLabel: format.formatDelta(project.weekly_star_delta, rankingData.previous_snapshot_date),
        growthLabel: format.formatGrowth(project.weekly_growth_rate, rankingData.previous_snapshot_date),
        compositeLabel: Number(project.composite_score || 0).toFixed(1),
        momentumLabel: project.momentum_score === null || project.momentum_score === undefined ? "-" : Number(project.momentum_score).toFixed(1),
        activityLabel: format.activityLabel(project.activity_score),
      }),
    });
  },

  copyRepo: function () {
    if (!this.data.project) return;
    wx.setClipboardData({
      data: this.data.project.repo,
      success: function () { wx.showToast({ title: "仓库地址已复制", icon: "none" }); },
    });
  },
});
