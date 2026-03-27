# Tracker-Direct-List 项目计划

## 项目概述
自动从 ngosang/trackerslist 获取 tracker 列表并转换为 OpenClash 规则格式。

## 目录结构
```
Tracker-Direct-List/
├── .github/
│   └── workflows/
│       └── update-trackers.yml    # GitHub Actions 工作流
├── scripts/
│   └── convert.py                 # 转换脚本
├── rule/
│   └── Custom_Direct.yaml         # 生成的规则文件
├── README.md                      # 中文 README
├── README_en.md                   # 英文 README
└── .gitignore
```

## 转换逻辑
1. 从 `https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt` 获取 tracker 列表
2. 提取每个 tracker 的域名部分
3. 转换为 OpenClash 规则格式：
   - 使用 `DOMAIN-SUFFIX` 规则类型
   - 格式：`DOMAIN-SUFFIX:tracker.example.com`

## GitHub Actions 工作流
- 触发：每小时执行
- 流程：
  1. 检出代码
  2. 运行转换脚本
  3. 比较文件是否有变化
  4. 如有变化，提交并推送
  5. Commit message: `update trackers list - {时间戳}`

## 规则格式 (YAML)
```yaml
payload:
  - DOMAIN-SUFFIX:tracker1.example.com
  - DOMAIN-SUFFIX:tracker2.example.com
  # ...
```

## 任务清单
- [ ] 分析 trackers_all.txt 原始格式
- [ ] 分析 Custom_Direct_Classical.yaml 目标格式
- [ ] 理解格式转换逻辑
- [ ] 创建 GitHub Actions 工作流配置
- [ ] 创建转换脚本
- [ ] 创建 README 中文版
- [ ] 创建 README 英文版
- [ ] 初始化 Git 仓库并提交