CREATE DATABASE house;

USE house;

CREATE TABLE `house_area` (
	`id` int UNSIGNED AUTO_INCREMENT,
  `code` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
	`parent_id` int not null DEFAULT 0,
  `parent_code` varchar(255) DEFAULT NULL,
  `display_order` INT NOT NULL DEFAULT 0,
	`created_on` timestamp DEFAULT current_timestamp,
	`updated_on` timestamp DEFAULT current_timestamp on update current_timestamp,
	PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `house` (
	`id` int UNSIGNED AUTO_INCREMENT,
	`area_id` int NOT NULL DEFAULT 0,
	`area_code` varchar(255) DEFAULT NULL,
  `title` varchar(2000) DEFAULT NULL,
	`unit_price` decimal(19,4) NOT NULL DEFAULT 0,
  `total_price` decimal(19,4) NOT NULL DEFAULT 0,
  `code` varchar(255) DEFAULT NULL,
  `community` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `build_years` varchar(255) DEFAULT NULL,
  `floor` varchar(255) DEFAULT NULL,
  `layout` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `picture_url` varchar(255) DEFAULT NULL,
  `url` varchar(1024) DEFAULT NULL,
	`created_on` timestamp DEFAULT current_timestamp,
	`updated_on` timestamp DEFAULT current_timestamp on update current_timestamp,
	PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `house_price` (
	`id` int UNSIGNED AUTO_INCREMENT,
	`house_id` int NOT NULL DEFAULT 0,
	`house_code` varchar(255) DEFAULT NULL,
	`unit_price` decimal(19,4) NOT NULL DEFAULT 0,
  `total_price` decimal(19,4) NOT NULL DEFAULT 0,
	`created_on` timestamp DEFAULT current_timestamp,
	`updated_on` timestamp DEFAULT current_timestamp on update current_timestamp,
	PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8;
