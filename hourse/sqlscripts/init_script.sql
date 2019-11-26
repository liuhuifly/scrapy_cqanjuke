CREATE DATABASE pymysqldb;

USE pymysqldb;

CREATE TABLE `cq_house_info` (
	`id` int UNSIGNED AUTO_INCREMENT,
  `house_title` varchar(255) DEFAULT NULL,
  `house_cost` varchar(255) DEFAULT NULL,
  `house_code` varchar(255) DEFAULT NULL,
  `house_public_time` varchar(255) DEFAULT NULL,
  `house_community` varchar(255) DEFAULT NULL,
  `house_location` varchar(255) DEFAULT NULL,
  `house_build_years` varchar(255) DEFAULT NULL,
  `house_kind` varchar(255) DEFAULT NULL,
  `house_layout` varchar(255) DEFAULT NULL,
  `house_size` varchar(255) DEFAULT NULL,
  `house_face_to` varchar(255) DEFAULT NULL,
  `house_point` varchar(255) DEFAULT NULL,
  `house_price` varchar(255) DEFAULT NULL,
  `house_first_pay` varchar(255) DEFAULT NULL,
  `house_month_pay` varchar(255) DEFAULT NULL,
  `house_decorate_type` varchar(255) DEFAULT NULL,
  `house_agent` varchar(255) DEFAULT NULL,
  `house_agency` varchar(255) DEFAULT NULL,
  `house_url` varchar(255) DEFAULT NULL,
	`created_on` timestamp DEFAULT current_timestamp,
	`updated_on` timestamp DEFAULT current_timestamp on update current_timestamp,
	PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `cq_area_info` (
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
  `house_title` varchar(255) DEFAULT NULL,
  `house_cost` varchar(255) DEFAULT NULL,
  `house_code` varchar(255) DEFAULT NULL,
  `house_community` varchar(255) DEFAULT NULL,
  `house_location` varchar(255) DEFAULT NULL,
  `house_build_years` varchar(255) DEFAULT NULL,
  `house_kind` varchar(255) DEFAULT NULL,
  `house_layout` varchar(255) DEFAULT NULL,
  `house_size` varchar(255) DEFAULT NULL,
  `house_face_to` varchar(255) DEFAULT NULL,
  `house_price` varchar(255) DEFAULT NULL,
  `house_url` varchar(255) DEFAULT NULL,
	`created_on` timestamp DEFAULT current_timestamp,
	`updated_on` timestamp DEFAULT current_timestamp on update current_timestamp,
	PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

/*
update cq_area_info a 
inner join cq_area_info a2 on a.parent_code = a2.code
set a.parent_id = a2.id
*/