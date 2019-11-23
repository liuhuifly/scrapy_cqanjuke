CREATE DATABASE pymysqldb;

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