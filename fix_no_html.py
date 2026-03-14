import os
os.chdir('C:/Users/CN/Desktop/111')

# 基础URL（无.html后缀）
base_url = 'https://zhsw1.pages.dev'

files = ['login.html', 'dashboard.html', 'devices.html', 'history.html', 'alarms.html', 'settings.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换window.location跳转 - 使用无.html后缀的URL
    content = content.replace('window.location.href = "https://zhsw1.pages.dev/login.html"', f"window.location.href = '{base_url}/login'")
    content = content.replace('window.location.href = "https://zhsw1.pages.dev/dashboard.html"', f"window.location.href = '{base_url}/dashboard'")
    content = content.replace('window.location.href = "https://zhsw1.pages.dev/devices.html"', f"window.location.href = '{base_url}/devices'")
    content = content.replace('window.location.href = "https://zhsw1.pages.dev/history.html"', f"window.location.href = '{base_url}/history'")
    content = content.replace('window.location.href = "https://zhsw1.pages.dev/alarms.html"', f"window.location.href = '{base_url}/alarms'")
    content = content.replace('window.location.href = "https://zhsw1.pages.dev/settings.html"', f"window.location.href = '{base_url}/settings'")
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f'Fixed {f}')

print('All done!')
