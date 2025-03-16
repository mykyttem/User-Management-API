CREATE DATABASE IF NOT EXISTS user_management;
CREATE DATABASE IF NOT EXISTS test_db_user_management;
GRANT ALL PRIVILEGES ON user_management.* TO 'mysql'@'%';
GRANT ALL PRIVILEGES ON test_db_user_management.* TO 'mysql'@'%';
FLUSH PRIVILEGES;