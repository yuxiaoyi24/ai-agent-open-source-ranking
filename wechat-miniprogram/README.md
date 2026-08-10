# AI Agent 开源技术周榜小程序

这是基于 `wxa5fdbcf1f1f80135` 的原生微信小程序。小程序启动时读取 GitHub Pages 上的最新周榜，并保留本地缓存和安装包内置快照作为断网兜底。

## 本地预览

1. 打开微信开发者工具，导入本目录。
2. 使用项目配置中的 AppID，选择“微信小程序”项目。
3. 编译即可预览首页、模块榜单、项目详情和评分说明。

## 每周自动更新

GitHub Actions 每周生成 `data/miniprogram/latest.json`，并发布到：

`https://yuxiaoyi24.github.io/ai-agent-open-source-ranking/data/latest.json`

小程序在启动和下拉刷新时读取这份数据。网络请求失败时依次使用上次成功缓存和安装包内置快照，因此每周数据更新不需要重新上传代码或再次提审。

## 上线前配置

在微信公众平台的“开发管理 → 开发设置 → 服务器域名”中，将 `https://yuxiaoyi24.github.io` 添加为 `request` 合法域名。开发者工具本地调试时也可以临时关闭“不校验合法域名”，但线上版本必须完成平台配置。
