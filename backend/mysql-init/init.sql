DROP DATABASE IF EXISTS test_db;
CREATE DATABASE test_db;
GRANT ALL PRIVILEGES ON test_db.* TO 'user'@'%';
FLUSH PRIVILEGES;

-- CREATE TABLE users (
--      -- 고유 번호 (자동 증가)
--      id INT NOT NULL COMMENT '아이디',
--      -- 이메일
--      email VARCHAR(255)  NOT NULL COMMENT '이메일',
--      -- 이름
--      username VARCHAR(255) NOT null COMMENT '사용자명',
--      -- 비밀번호 (암호화된 문자열 저장용으로 충분한 길이)
--      hashed_password VARCHAR(255) NOT null COMMENT '비밀번호',
--      -- 회원 상태 (1: 활성, 0: 비활성 등)
--      is_active TINYINT(1) DEFAULT 1 COMMENT ' 회원 상태 (1: 활성, 0: 비활성 등)',
--      PRIMARY KEY (id),
--      UNIQUE KEY unique_users (email, username)
--  )  COMMENT '가입 회원 정보'  ENGINE=INNODB CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ;