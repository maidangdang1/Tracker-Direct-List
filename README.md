# Tracker-Direct-List

自动从 [ngosang/trackerslist](https://github.com/ngosang/trackerslist) 获取最新的 BT tracker 列表，并转换为 OpenClash 规则格式。

## 简介

本项目通过 GitHub Actions 每小时自动更新 tracker 列表，转换为 OpenClash 可用的 Direct 规则格式，方便科学上网用户使用。

## 功能特性

- 🚀 自动获取最新的公共 tracker
- ⏰ 每小时自动更新
- 📝 转换为 OpenClash 规则格式
- ✅ 仅在内容变化时提交更新

## 生成的规则文件

生成的规则文件位于 [`rule/Torrent_Tracker_Direct.yaml`](rule/Torrent_Tracker_Direct.yaml)，格式如下：

```yaml
# Generated from rule/Custom_Direct.yaml
# REPO: https://github.com/ngosang/trackerslist
# SOURCE: https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
# TOTAL: xxx
# UPDATED: YYYY-MM-DD HH:MM:SS UTC

payload:
  - DOMAIN-SUFFIX:tracker1.example.com
  - DOMAIN-SUFFIX:tracker2.example.com
  # ...
```

## 在 OpenClash 中使用

1. 下载本仓库的 `Torrent_Tracker_Direct.yaml` 文件
2. 在 OpenClash 的 "配置文件管理" 中添加
3. 在规则设置中选择使用

## 工作原理

1. GitHub Actions 每小时触发
2. 从 `trackers_all.txt` 获取 tracker 列表
3. 提取每个 tracker 的域名
4. 转换为 OpenClash 的 `DOMAIN-SUFFIX` 规则格式
5. 如果内容有变化，则提交到仓库

## 目录结构

```
Tracker-Direct-List/
├── .github/
│   └── workflows/
│       └── update-trackers.yml    # GitHub Actions 工作流
├── scripts/
│   └── convert.py                 # 转换脚本
├── rule/
│   └── Torrent_Tracker_Direct.yaml         # 生成的规则文件
├── README.md                       # 中文说明
└── README_en.md                    # English README
```

## 许可证

MIT License

## 致谢

- [ngosang/trackerslist](https://github.com/ngosang/trackerslist) - Tracker 列表数据源
- [Aethersailor/Custom_OpenClash_Rules](https://github.com/Aethersailor/Custom_OpenClash_Rules) - 格式参考