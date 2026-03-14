import os
os.chdir('C:/Users/CN/Desktop/111')

files = ['login.html', 'dashboard.html', 'devices.html', 'history.html', 'alarms.html', 'settings.html']

# 完整URL前缀
base_url = 'https://zhsw1.pages.dev'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换href链接 - 使用完整URL
    content = content.replace('href="/login.html"', f'href="{base_url}/login.html"')
    content = content.replace('href="/dashboard.html"', f'href="{base_url}/dashboard.html"')
    content = content.replace('href="/devices.html"', f'href="{base_url}/devices.html"')
    content = content.replace('href="/history.html"', f'href="{base_url}/history.html"')
    content = content.replace('href="/alarms.html"', f'href="{base_url}/alarms.html"')
    content = content.replace('href="/settings.html"', f'href="{base_url}/settings.html"')
    
    # 替换window.location跳转 - 使用完整URL
    content = content.replace('window.location.href = "/login.html"', f'window.location.href = "{base_url}/login.html"')
    content = content.replace('window.location.href = "/dashboard.html"', f'window.location.href = "{base_url}/dashboard.html"')
    content = content.replace('window.location.href = "/devices.html"', f'window.location.href = "{base_url}/devices.html"')
    content = content.replace('window.location.href = "/history.html"', f'window.location.href = "{base_url}/history.html"')
    content = content.replace('window.location.href = "/alarms.html"', f'window.location.href = "{base_url}/alarms.html"')
    content = content.replace('window.location.href = "/settings.html"', f'window.location.href = "{base_url}/settings.html"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f'Fixed {f}')

print('All done!')
