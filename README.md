# 用户登录登出系统

一个功能完整的用户登录登出系统，使用Flask和SQLite数据库，具有美观的Bootstrap界面和完整的用户管理功能。

## ✨ 功能特性

### 🔐 用户认证
- 用户注册和登录
- 密码强度验证
- 邮箱格式验证
- 用户会话管理
- 安全的密码哈希存储

### 📊 用户管理
- 用户登出功能
- 登录历史记录
- 个人资料管理
- 会话时长统计
- IP地址记录

### 🎨 用户界面
- 美观的Bootstrap界面
- 响应式设计
- 现代化UI组件
- 直观的导航菜单
- 实时状态显示

### 🔒 安全特性
- 密码强度要求（至少6位，包含字母和数字）
- 邮箱格式验证
- 用户名唯一性检查
- 安全的会话管理
- 登录日志记录

## 🗄️ 数据库结构

### 用户表 (User)
- `id`: 主键
- `username`: 用户名（唯一）
- `email`: 邮箱（唯一）
- `password_hash`: 密码哈希
- `created_at`: 创建时间
- `last_login`: 最后登录时间

### 登录记录表 (LoginLog)
- `id`: 主键
- `user_id`: 用户ID（外键）
- `login_time`: 登录时间
- `logout_time`: 登出时间
- `ip_address`: IP地址

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 启动系统
```bash
# 方式一：使用启动脚本（推荐）
python run.py

# 方式二：直接运行
python app.py
```

### 3. 访问应用
打开浏览器访问 http://localhost:5001

## 📖 使用说明

### 新用户注册
1. 访问注册页面
2. 填写用户名（至少3个字符）
3. 输入有效的邮箱地址
4. 设置密码（至少6位，包含字母和数字）
5. 确认密码
6. 点击注册按钮

### 用户登录
1. 访问登录页面
2. 输入用户名和密码
3. 可选择"记住我"功能
4. 点击登录按钮

### 功能使用
1. **仪表板**: 查看用户信息和快速操作
2. **个人资料**: 查看详细信息和登录历史
3. **登出**: 安全退出登录

## 🧪 测试系统

运行测试脚本验证系统功能：
```bash
python test_system.py
```

## 📁 项目结构

```
questions/
├── app.py              # 主应用文件
├── run.py              # 启动脚本
├── test_system.py      # 测试脚本
├── requirements.txt    # 依赖项
├── README.md          # 项目说明
├── .gitignore         # Git忽略文件
└── templates/         # 前端模板
    ├── base.html      # 基础模板
    ├── login.html     # 登录页面
    ├── register.html  # 注册页面
    ├── dashboard.html # 仪表板
    └── profile.html   # 个人资料
```

## 🛠️ 技术栈

- **后端**: Flask 2.3.3
- **数据库**: SQLAlchemy + SQLite
- **前端**: Bootstrap 5.1.3 + Bootstrap Icons
- **安全**: Werkzeug 密码哈希
- **测试**: Requests 库

## 🔧 配置选项

### 环境变量
- `SECRET_KEY`: 应用密钥（默认: 'your-secret-key-here'）
- `SQLALCHEMY_DATABASE_URI`: 数据库连接（默认: 'sqlite:///users.db'）

### 端口配置
默认端口为5001，可在 `app.py` 中修改：
```python
app.run(debug=True, port=5001)
```

## 📝 开发说明

### 添加新功能
1. 在 `app.py` 中添加新的路由
2. 在 `templates/` 中创建对应的模板
3. 更新数据库模型（如需要）
4. 运行测试验证功能

### 数据库迁移
```python
# 在Python控制台中
from app import app, db
with app.app_context():
    db.create_all()
```

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证。

## 🆘 常见问题

### Q: 无法启动服务器？
A: 检查端口5001是否被占用，或修改端口号。

### Q: 数据库文件在哪里？
A: 数据库文件 `users.db` 会在首次运行时自动创建。

### Q: 如何重置数据库？
A: 删除 `users.db` 文件，重新启动应用。

### Q: 支持哪些浏览器？
A: 支持所有现代浏览器（Chrome、Firefox、Safari、Edge）。

---

**享受使用！** 🎉 