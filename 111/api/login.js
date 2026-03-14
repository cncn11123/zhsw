// 登录 API
module.exports = (req, res) => {
  // 设置 CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { username, password } = req.body;

  // 模拟用户数据（实际项目请连接数据库）
  const users = [
    { username: 'admin', password: 'admin123', role: 'admin' },
    { username: 'user', password: 'user123', role: 'user' },
    { username: 'guest', password: 'guest', role: 'guest' }
  ];

  // 验证用户
  const user = users.find(u => u.username === username && u.password === password);

  if (user) {
    // 生成简单 token（实际项目请用 JWT）
    const token = Buffer.from(JSON.stringify({
      username: user.username,
      role: user.role,
      exp: Date.now() + 24 * 60 * 60 * 1000
    })).toString('base64');

    res.json({
      success: true,
      message: '登录成功',
      token: token,
      user: {
        username: user.username,
        role: user.role
      }
    });
  } else {
    res.status(401).json({
      success: false,
      message: '用户名或密码错误'
    });
  }
};
