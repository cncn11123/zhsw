# 流量计监控系统 - 页面规划

## 当前状态
- ✅ 登录页面 (login.html)
- ✅ 登录API (api/login.js)
- ✅ 仪表盘 (dashboard.html)
- ✅ 设备管理 (devices.html)
- ✅ 历史数据 (history.html)
- ✅ 报警中心 (alarms.html)
- ✅ 系统设置 (settings.html)

## 待开发页面

### 1. 首页/仪表盘 (dashboard.html)
- 流量实时数据展示
- 关键指标卡片（总流量、瞬时流量、累计流量）
- 实时图表（折线图）
- 告警状态指示

### 2. 设备管理 (devices.html)
- 设备列表展示
- 设备状态（在线/离线）
- 设备详情查看
- 添加/删除设备

### 3. 历史数据 (history.html)
- 历史记录查询
- 数据导出功能
- 日期范围选择
- 数据报表

### 4. 报警中心 (alarms.html)
- 告警列表
- 告警级别（严重/警告/提示）
- 告警确认/处理
- 告警设置

### 5. 系统设置 (settings.html)
- 用户管理
- 权限配置
- 系统参数
- 关于页面

## 技术实现
- 前端：HTML + CSS + JavaScript（原生或轻量框架）
- 图表：Chart.js
- 数据：模拟JSON数据（可后续对接真实API）

## 文件结构
```
111/
├── login.html        # 登录页 ✅
├── index.html       # 首页/仪表盘（可复用login页面样式）
├── dashboard.html   # 仪表盘
├── devices.html     # 设备管理
├── history.html     # 历史数据
├── alarms.html      # 报警中心
├── settings.html    # 系统设置
├── css/
│   └── style.css   # 统一样式
├── js/
│   ├── api.js      # API调用封装
│   ├── chart.js    # 图表配置
│   └── app.js      # 通用逻辑
└── api/
    └── login.js    # 登录API ✅
```

## 优先级
1. 首页/仪表盘 - 最重要，展示核心数据
2. 设备管理 - 查看和控制设备
3. 历史数据 - 查询历史记录
4. 报警中心 - 告警管理
5. 系统设置 - 扩展功能
