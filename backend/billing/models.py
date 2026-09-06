
-- ตาราง Postgres จริง
CREATE TABLE users (
  id TEXT PRIMARY KEY,
  email TEXT,
  credits INT DEFAULT 20,
  plan TEXT DEFAULT 'free'
);
CREATE TABLE usage_logs (
  id SERIAL PRIMARY KEY,
  user_id TEXT,
  action TEXT,
  cost INT,
  created_at TIMESTAMP DEFAULT NOW()
);
