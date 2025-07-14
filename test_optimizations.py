#!/usr/bin/env python3
"""
Frog-Tech Optimizer - Optimization Test Script
Tests and verifies that optimizations are working properly
"""

import os
import sys
import subprocess
import winreg
import ctypes
from datetime import datetime

def is_admin():
    """Check if running as administrator"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def test_registry_access():
    """Test if we can access and modify registry keys"""
    try:
        # Test writing to a test key
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        winreg.CloseKey(key)
        return True
    except PermissionError:
        return False
    except Exception:
        return False

def test_powershell_execution():
    """Test if PowerShell commands can be executed"""
    try:
        result = subprocess.run(['powershell', 'Get-Process'], 
                              capture_output=True, shell=True, timeout=10)
        return result.returncode == 0
    except:
        return False

def test_system_commands():
    """Test if system commands can be executed"""
    try:
        result = subprocess.run(['fsutil', 'behavior', 'query'], 
                              capture_output=True, shell=True, timeout=10)
        return result.returncode == 0
    except:
        return False

def test_network_commands():
    """Test if network commands can be executed"""
    try:
        result = subprocess.run(['netsh', 'interface', 'show', 'interface'], 
                              capture_output=True, shell=True, timeout=10)
        return result.returncode == 0
    except:
        return False

def main():
    """Main test function"""
    print("🐸 Frog-Tech Optimizer - System Test")
    print("=" * 50)
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Test admin privileges
    print("🔐 Testing Administrator Privileges...")
    if is_admin():
        print("✅ Running with Administrator privileges")
        print("🚀 Full optimization capabilities available")
    else:
        print("⚠️ Running without Administrator privileges")
        print("🔧 Limited optimization capabilities")
        print("💡 Restart as Administrator for maximum performance gains")
    print()
    
    # Test registry access
    print("🔧 Testing Registry Access...")
    if test_registry_access():
        print("✅ Registry access working")
    else:
        print("❌ Registry access failed")
    print()
    
    # Test PowerShell execution
    print("⚡ Testing PowerShell Execution...")
    if test_powershell_execution():
        print("✅ PowerShell execution working")
    else:
        print("❌ PowerShell execution failed")
    print()
    
    # Test system commands
    print("🖥️ Testing System Commands...")
    if test_system_commands():
        print("✅ System commands working")
    else:
        print("❌ System commands failed")
    print()
    
    # Test network commands
    print("🌐 Testing Network Commands...")
    if test_network_commands():
        print("✅ Network commands working")
    else:
        print("❌ Network commands failed")
    print()
    
    # Summary
    print("=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    tests = [
        ("Admin Privileges", is_admin()),
        ("Registry Access", test_registry_access()),
        ("PowerShell", test_powershell_execution()),
        ("System Commands", test_system_commands()),
        ("Network Commands", test_network_commands())
    ]
    
    passed = sum(1 for _, result in tests if result)
    total = len(tests)
    
    for test_name, result in tests:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:<20} {status}")
    
    print()
    print(f"Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Optimizations should work properly.")
    elif passed >= 3:
        print("⚠️ Some tests failed. Optimizations may be limited.")
        print("💡 Try running as Administrator for better results.")
    else:
        print("❌ Many tests failed. Optimizations may not work properly.")
        print("🔧 Please run as Administrator and try again.")
    
    print()
    print("💡 TROUBLESHOOTING TIPS:")
    print("1. Run the application as Administrator")
    print("2. Make sure Windows Defender is not blocking the application")
    print("3. Check if any antivirus software is interfering")
    print("4. Restart your computer after applying optimizations")
    print("5. Some optimizations require a restart to take effect")

if __name__ == "__main__":
    main() 