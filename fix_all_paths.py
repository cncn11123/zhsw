import os
os.chdir('C:/Users/CN/Desktop/111')

files = ['login.html', 'dashboard.html', 'devices.html', 'history.html', 'alarms.html', 'settings.html']

# 路径映射 - 所有都使用绝对路径格式
path_map = {
    'login.html': '/login.html',
    'dashboard.html': '/dashboard.html',
    'devices.html': '/devices.html',
    'history.html': '/history.html',
    'alarms.html': '/alarms.html',
    'settings.html': '/settings.html'
}

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 替换href链接
    for old_path, new_path in path_map.items():
        content = content.replace(f'href="{old_path}"', f'href="{new_path}"')
        content = content.replace(f'href="./{old_path}"', f'href="{new_path}"')
    
    # 替换window.location
    content = content.replace('window.location.href = "./login.html"', 'window.location.href = "/login.html"')
    content = content.replace('window.location.href = "./dashboard.html"', 'window.location.href = "/dashboard.html"')
    content = content.replace('window.location.href = "./devices.html"', 'window.location.href = "/devices.html"')
    content = content.replace('window.location.href = "./history.html"', 'window.location.href = "/history.html"')
    content = content.replace('window.location.href = "./alarms.html"', 'window.location.href = "/alarms.html"')
    content = content.replace('window.location.href = "./settings.html"', 'window.location.href = "/settings.html"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f'Fixed {f}')

print('All done!')
