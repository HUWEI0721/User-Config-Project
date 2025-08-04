#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户登录系统测试脚本
"""

import requests
import time
from datetime import datetime

# 测试配置
BASE_URL = "http://localhost:5001"
TEST_USERNAME = "testuser"
TEST_EMAIL = "test@example.com"
TEST_PASSWORD = "testpass123"

def test_register():
    """测试用户注册"""
    print("🔧 测试用户注册...")
    
    data = {
        'username': TEST_USERNAME,
        'email': TEST_EMAIL,
        'password': TEST_PASSWORD,
        'confirm_password': TEST_PASSWORD
    }
    
    response = requests.post(f"{BASE_URL}/register", data=data)
    
    if response.status_code == 200:
        print("✅ 注册测试通过")
        return True
    else:
        print(f"❌ 注册测试失败: {response.status_code}")
        return False

def test_login():
    """测试用户登录"""
    print("🔧 测试用户登录...")
    
    data = {
        'username': TEST_USERNAME,
        'password': TEST_PASSWORD
    }
    
    session = requests.Session()
    response = session.post(f"{BASE_URL}/login", data=data)
    
    if response.status_code == 200 and "登录成功" in response.text:
        print("✅ 登录测试通过")
        return session
    else:
        print(f"❌ 登录测试失败: {response.status_code}")
        return None

def test_dashboard(session):
    """测试仪表板访问"""
    print("🔧 测试仪表板访问...")
    
    response = session.get(f"{BASE_URL}/")
    
    if response.status_code == 200 and TEST_USERNAME in response.text:
        print("✅ 仪表板测试通过")
        return True
    else:
        print(f"❌ 仪表板测试失败: {response.status_code}")
        return False

def test_profile(session):
    """测试个人资料页面"""
    print("🔧 测试个人资料页面...")
    
    response = session.get(f"{BASE_URL}/profile")
    
    if response.status_code == 200 and "个人资料" in response.text:
        print("✅ 个人资料测试通过")
        return True
    else:
        print(f"❌ 个人资料测试失败: {response.status_code}")
        return False

def test_logout(session):
    """测试用户登出"""
    print("🔧 测试用户登出...")
    
    response = session.get(f"{BASE_URL}/logout")
    
    if response.status_code == 200 and "已登出" in response.text:
        print("✅ 登出测试通过")
        return True
    else:
        print(f"❌ 登出测试失败: {response.status_code}")
        return False

def main():
    """主测试函数"""
    print("🚀 开始测试用户登录系统...")
    print(f"📅 测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 测试地址: {BASE_URL}")
    print("-" * 50)
    
    # 检查服务器是否运行
    try:
        response = requests.get(f"{BASE_URL}/login", timeout=5)
        print("✅ 服务器连接正常")
    except requests.exceptions.RequestException:
        print("❌ 无法连接到服务器，请确保服务器正在运行")
        print("💡 运行命令: python app.py")
        return
    
    # 执行测试
    tests_passed = 0
    total_tests = 5
    
    # 测试注册
    if test_register():
        tests_passed += 1
    
    # 测试登录
    session = test_login()
    if session:
        tests_passed += 1
        
        # 测试仪表板
        if test_dashboard(session):
            tests_passed += 1
        
        # 测试个人资料
        if test_profile(session):
            tests_passed += 1
        
        # 测试登出
        if test_logout(session):
            tests_passed += 1
    
    # 测试结果
    print("-" * 50)
    print(f"📊 测试结果: {tests_passed}/{total_tests} 通过")
    
    if tests_passed == total_tests:
        print("🎉 所有测试通过！系统运行正常")
    else:
        print("⚠️  部分测试失败，请检查系统配置")

if __name__ == "__main__":
    main() 