// 流量计监控系统 - 通用脚本

// 检查登录状态
function checkAuth() {
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = 'https://zhsw1.pages.dev/login.html';
        return false;
    }
    
    // 显示用户名
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    if (user.username && document.getElementById('username')) {
        document.getElementById('username').textContent = user.username;
    }
    return true;
}

// 退出登录
function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = 'https://zhsw1.pages.dev/login.html';
}

// 导航高亮
function setActiveNav() {
    const path = window.location.pathname;
    const page = path.split('/').pop().replace('.html', '') || 'dashboard';
    
    document.querySelectorAll('.navbar-menu a').forEach(link => {
        const href = link.getAttribute('href').replace('.html', '');
        if (href === page) {
            link.classList.add('active');
        }
    });
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    if (typeof checkAuth === 'function') {
        checkAuth();
    }
    if (typeof setActiveNav === 'function') {
        setActiveNav();
    }
});
