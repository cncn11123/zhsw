import os
os.chdir('C:/Users/CN/Desktop/111')

# 基础URL（无.html后缀）
base_url = 'https://zhsw1.pages.dev'

files = ['login.html', 'dashboard.html', 'devices.html', 'history.html', 'alarms.html', 'settings.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换href链接 - 使用无.html后缀的URL
    content = content.replace(f'href="{base_url}/login.html"', f'href="{base_url}/login"')
    content = content.replace(f'href="{base_url}/dashboard.html"', f'href="{base_url}/dashboard"')
    content = content.replace(f'href="{base_url}/devices.html"', f'href="{base_url}/devices"')
    content = content.replace(f'href="{base_url}/history.html"', f'href="{base_url}/history"')
    content = content.replace(f'href="{base_url}/alarms.html"', f'href="{base_url}/alarms"')
    content = content.replace(f'href="{base_url}/settings.html"', f'href="{base_url}/settings"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f'Fixed href in {f}')

print('All done!')
