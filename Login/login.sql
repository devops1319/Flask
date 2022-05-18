CREATE DATABASE IF NOT EXISTS 'geeklogin' DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE 'geeklogin';

CREATE TABLE IF NOT EXISTS 'login'(
	'username' varchar(50) NOT NULL,
    'password' varchar(50) NOT NULL,
) ENGINE=InnoDB AUTO_INCREMEN=2 DEFAULT CHARSET=utf8;
    