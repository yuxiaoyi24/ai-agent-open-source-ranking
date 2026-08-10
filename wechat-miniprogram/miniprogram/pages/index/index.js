var format = require("../../utils/format.js");
var app = getApp();

function enrichProject(project, mode, baseline) {
  var score = mode === "momentum" ? (project.momentum_score || 0) : (project.composite_score || 0);
  return Object.assign({}, project, {
    score: score,
    scorePercent: Math.max(0, Math.min(100, score)),
    starsLabel: format.formatStars(project.stars),
    deltaLabel: format.formatDelta(project.weekly_star_delta, baseline),
    growthLabel: format.formatGrowth(project.weekly_growth_rate, baseline),
    activityLabel: format.activityLabel(project.activity_score),
    positive: Number(project.weekly_star_delta || 0) > 0,
  });
}

Page({
  data: {
    date: "",
    previousDate: "",
    baseline: false,
    projectCount: 0,
    candidateCount: 0,
    moduleCount: 0,
    dataSourceLabel: "内置快照",
    totalStars: "0",
    totalDelta: "0",
    activeCount: 0,
    mode: "composite",
    selectedModule: "all",
    tabs: [],
    modules: [],
  },

  onLoad: function () {
    var self = this;
    this.rankingData = app.getRankingData();
    this.refreshView();
    app.refreshRankingData(function (result) {
      self.rankingData = result.data;
      self.setData({ dataSourceLabel: result.source });
      self.refreshView();
    });
  },

  onPullDownRefresh: function () {
    var self = this;
    app.refreshRankingData(function (result) {
      self.rankingData = result.data;
      self.setData({ dataSourceLabel: result.source });
      self.refreshView();
      wx.stopPullDownRefresh();
      wx.showToast({ title: result.updated ? "周榜已同步" : "当前为缓存数据", icon: "none" });
    });
  },

  refreshView: function () {
    var self = this;
    var rankingData = this.rankingData;
    if (!rankingData) return;
    var baseline = Boolean(rankingData.previous_snapshot_date);
    var selected = this.data.selectedModule;
    var mode = this.data.mode;
    var modules = rankingData.modules
      .filter(function (module) { return selected === "all" || module.key === selected; })
      .map(function (module) {
        var source = mode === "momentum" ? module.momentum : module.composite;
        return Object.assign({}, module, {
          projects: source.map(function (project) {
            var enriched = enrichProject(project, mode, baseline);
            enriched.color = module.color;
            enriched.scoreLabel = Number(enriched.score).toFixed(1);
            return enriched;
          }),
        });
      });
    var composite = rankingData.modules.reduce(function (all, module) { return all.concat(module.composite); }, []);
    var unique = {};
    composite.forEach(function (project) { unique[project.slug] = project; });
    var totalStars = Object.keys(unique).reduce(function (sum, slug) { return sum + Number(unique[slug].stars || 0); }, 0);
    var totalDelta = Object.keys(unique).reduce(function (sum, slug) { return sum + Number(unique[slug].weekly_star_delta || 0); }, 0);
    var activeCount = Object.keys(unique).filter(function (slug) { return Number(unique[slug].activity_score || 0) >= 85; }).length;
    var tabs = [{ key: "all", label: "全部模块", color: "#73a7ff" }].concat(rankingData.modules.map(function (module) {
      return { key: module.key, label: module.label, color: module.color };
    }));
    self.setData({
      date: rankingData.date,
      previousDate: rankingData.previous_snapshot_date || "首期基线",
      baseline: baseline,
      projectCount: rankingData.project_count,
      candidateCount: rankingData.candidate_count,
      moduleCount: rankingData.module_count,
      totalStars: format.formatStars(totalStars),
      totalDelta: format.formatDelta(totalDelta, baseline),
      activeCount: activeCount,
      dataSourceLabel: app.globalData.rankingSource,
      tabs: tabs,
      modules: modules,
    });
  },

  onModeTap: function (event) {
    this.setData({ mode: event.currentTarget.dataset.mode });
    this.refreshView();
  },

  onModuleTap: function (event) {
    this.setData({ selectedModule: event.currentTarget.dataset.key });
    this.refreshView();
  },

  onProjectTap: function (event) {
    wx.navigateTo({ url: "/pages/project/project?slug=" + encodeURIComponent(event.currentTarget.dataset.slug) });
  },

  onAboutTap: function () {
    wx.navigateTo({ url: "/pages/about/about" });
  },
});
