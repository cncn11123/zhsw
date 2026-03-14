# 修复路径
pages = ['login.html', 'dashboard.html', 'devices.html', 'history.html', 'alarms.html', 'settings.html']

for page in pages:
    filepath = f'C:/Users/CN/Desktop/111/{page}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复所有路径为 /xxx.html 格式
    content = content.replace('href="./dashboard.html"', 'href="/dashboard.html"')
    content = content.replace('href="./devices.html"', 'href="/devices.html"')
    content = content.replace('href="./history.html"', 'href="/history.html"')
    content = content.replace('href="./alarms.html"', 'href="/alarms.html"')
    content = content.replace('href="./settings.html"', 'href="/settings.html"')
    content = content.replace('href="./login.html"', 'href="/login.html"')
    content = content.replace('window.location.href = "./dashboard.html"', 'window.location.href = "/dashboard.html"')
    content = content.replace('window.location.href = "./login.html"', 'window.location.href = "/login.html"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {page}')

print('Done')
