#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户登录系统启动脚本
"""

import os
import sys
import subprocess
import webbrowser
import time
from datetime import datetime

def check_dependencies():
    """检查依赖项是否已安装"""
    print("🔍 检查依赖项...")
    
    try:
        import flask
        import flask_sqlalchemy
        import werkzeug
        print("✅ 所有依赖项已安装")
        return True
    except ImportError as e:
        print(f"❌ 缺少依赖项: {e}")
        print("💡 请运行: pip install -r requirements.txt")
        return False

def create_database():
    """创建数据库"""
    print("🗄️  初始化数据库...")
    
    try:
        from app import app, db
        with app.app_context():
            db.create_all()
        print("✅ 数据库初始化完成")
        return True
    except Exception as e:
        print(f"❌ 数据库初始化失败: {e}")
        return False

def start_server():
    """启动服务器"""
    print("🚀 启动用户登录系统...")
    print(f"📅 启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🌐 访问地址: http://localhost:5001")
    print("⏹️  按 Ctrl+C 停止服务器")
    print("-" * 50)
    
    try:
        # 启动Flask应用
        from app import app
        app.run(debug=True, port=5001, host='0.0.0.0')
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")

def open_browser():
    """打开浏览器"""
    try:
        time.sleep(2)  # 等待服务器启动
        webbrowser.open('http://localhost:5001')
        print("🌐 已自动打开浏览器")
    except:
        print("💡 请手动打开浏览器访问: http://localhost:5001")

def main():
    """主函数"""
    print("🎯 用户登录系统启动器")
    print("=" * 50)
    
    # 检查依赖项
    if not check_dependencies():
        return
    
    # 创建数据库
    if not create_database():
        return
    
    # 询问是否自动打开浏览器
    try:
        choice = input("是否自动打开浏览器？(y/n): ").lower().strip()
        if choice in ['y', 'yes', '是']:
            import threading
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
    except:
        pass
    
    # 启动服务器
    start_server()

if __name__ == "__main__":
    main() 