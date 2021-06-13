-- phpMyAdmin SQL Dump
-- version phpStudy 2014
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2021 �?06 �?13 �?03:01
-- 服务器版本: 5.6.39
-- PHP 版本: 5.5.38

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `visit_tsinghua`
--

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=45 ;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add test user', 7, 'add_testuser'),
(26, 'Can change test user', 7, 'change_testuser'),
(27, 'Can delete test user', 7, 'delete_testuser'),
(28, 'Can view test user', 7, 'view_testuser'),
(29, 'Can add booking record', 8, 'add_bookingrecord'),
(30, 'Can change booking record', 8, 'change_bookingrecord'),
(31, 'Can delete booking record', 8, 'delete_bookingrecord'),
(32, 'Can view booking record', 8, 'view_bookingrecord'),
(33, 'Can add every day booking info', 9, 'add_everydaybookinginfo'),
(34, 'Can change every day booking info', 9, 'change_everydaybookinginfo'),
(35, 'Can delete every day booking info', 9, 'delete_everydaybookinginfo'),
(36, 'Can view every day booking info', 9, 'view_everydaybookinginfo'),
(37, 'Can add system configuration', 10, 'add_systemconfiguration'),
(38, 'Can change system configuration', 10, 'change_systemconfiguration'),
(39, 'Can delete system configuration', 10, 'delete_systemconfiguration'),
(40, 'Can view system configuration', 10, 'view_systemconfiguration'),
(41, 'Can add user', 11, 'add_user'),
(42, 'Can change user', 11, 'change_user'),
(43, 'Can delete user', 11, 'delete_user'),
(44, 'Can view user', 11, 'view_user');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `BookingRecord`
--

CREATE TABLE IF NOT EXISTS `BookingRecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `datetime_id` int(11) NOT NULL,
  `datetime_start` datetime(6) NOT NULL,
  `datetime_end` datetime(6) NOT NULL,
  `submit_datetime` datetime(6) NOT NULL,
  `is_main_order` int(11) NOT NULL,
  `main_order_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `processed_datetime` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- 转存表中的数据 `BookingRecord`
--

INSERT INTO `BookingRecord` (`id`, `user_id`, `username`, `datetime_id`, `datetime_start`, `datetime_end`, `submit_datetime`, `is_main_order`, `main_order_id`, `status`, `processed_datetime`) VALUES
(6, 2, '施建锋', 30, '2021-06-12 16:00:00.000000', '2021-06-13 15:59:59.999999', '2021-06-10 14:43:55.347171', 1, 0, 1, NULL),
(7, 2, '施dd', 28, '2021-06-10 16:00:00.000000', '2021-06-11 15:59:59.999999', '2021-06-10 15:05:04.930520', 1, 0, 1, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(8, 'adminWeb', 'bookingrecord'),
(9, 'adminWeb', 'everydaybookinginfo'),
(10, 'adminWeb', 'systemconfiguration'),
(11, 'adminWeb', 'user'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'test', 'testuser');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=22 ;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-06-07 12:21:29.484845'),
(2, 'auth', '0001_initial', '2021-06-07 12:21:39.715552'),
(3, 'admin', '0001_initial', '2021-06-07 12:21:41.838531'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-06-07 12:21:41.911485'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-06-07 12:21:41.965644'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-06-07 12:21:43.401399'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-06-07 12:21:44.400603'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-06-07 12:21:45.324414'),
(9, 'auth', '0004_alter_user_username_opts', '2021-06-07 12:21:45.479370'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-06-07 12:21:46.032512'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-06-07 12:21:46.073485'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-06-07 12:21:46.118459'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-06-07 12:21:46.983071'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-06-07 12:21:47.682970'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-06-07 12:21:48.557489'),
(16, 'auth', '0011_update_proxy_permissions', '2021-06-07 12:21:48.627629'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-06-07 12:21:49.533399'),
(18, 'sessions', '0001_initial', '2021-06-07 12:21:50.150012'),
(19, 'test', '0001_initial', '2021-06-07 12:21:50.539038'),
(20, 'adminWeb', '0001_initial', '2021-06-07 13:58:47.056361'),
(21, 'adminWeb', '0002_remove_user_createtime', '2021-06-08 01:00:38.764562');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('juv3j2ggf5npvwa4vq8wepwsnkyaxacv', 'eyJpc19sb2dpbiI6dHJ1ZSwiaWRfY2FyZCI6Ijg4OCIsInVzZXJfaWQiOjIsInVzZXJuYW1lIjoiXHU2NWJkZGQifQ:1lrMEs:YkWDcBTjxRK8VM34CqWGhDrDf8VkzWGK_sRtKAGGY88', '2021-06-24 15:04:58.301456');

-- --------------------------------------------------------

--
-- 表的结构 `EveryDayBookingInfo`
--

CREATE TABLE IF NOT EXISTS `EveryDayBookingInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime_start` datetime(6) NOT NULL,
  `datetime_end` datetime(6) NOT NULL,
  `maximum_number` int(11) NOT NULL,
  `remain_number` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=33 ;

--
-- 转存表中的数据 `EveryDayBookingInfo`
--

INSERT INTO `EveryDayBookingInfo` (`id`, `datetime_start`, `datetime_end`, `maximum_number`, `remain_number`) VALUES
(26, '2021-06-08 16:00:00.000000', '2021-06-09 15:59:59.999999', 2, 2),
(27, '2021-06-09 16:00:00.000000', '2021-06-10 15:59:59.999999', 2, 2),
(28, '2021-06-10 16:00:00.000000', '2021-06-11 15:59:59.999999', 2, 1),
(29, '2021-06-11 16:00:00.000000', '2021-06-12 15:59:59.999999', 2, 2),
(30, '2021-06-12 16:00:00.000000', '2021-06-13 15:59:59.999999', 1, 0),
(31, '2021-06-13 16:00:00.000000', '2021-06-14 15:59:59.999999', 1, 1),
(32, '2021-06-14 16:00:00.000000', '2021-06-15 15:59:59.999999', 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `SystemConfiguration`
--

CREATE TABLE IF NOT EXISTS `SystemConfiguration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `configuration_name` varchar(50) NOT NULL,
  `configuration_value` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- 转存表中的数据 `SystemConfiguration`
--

INSERT INTO `SystemConfiguration` (`id`, `configuration_name`, `configuration_value`) VALUES
(1, 'allow_booking_date_start', '2021-06-13'),
(2, 'allow_booking_date_end', '2021-06-15'),
(3, 'days_showed_at_most_one_time', '7'),
(4, 'maximum_number_per_day', '1');

-- --------------------------------------------------------

--
-- 表的结构 `TestUser`
--

CREATE TABLE IF NOT EXISTS `TestUser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `level` int(11) NOT NULL,
  `createTime` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `TestUser`
--

INSERT INTO `TestUser` (`id`, `name`, `level`, `createTime`) VALUES
(1, '张三', 10, '2021-06-07 20:22:00.111925');

-- --------------------------------------------------------

--
-- 表的结构 `User`
--

CREATE TABLE IF NOT EXISTS `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `id_card` varchar(50) NOT NULL,
  `identity_authentication_type` int(11) NOT NULL,
  `wechat_open_id` varchar(200) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_role` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- 转存表中的数据 `User`
--

INSERT INTO `User` (`id`, `username`, `id_card`, `identity_authentication_type`, `wechat_open_id`, `phone`, `password`, `user_role`) VALUES
(1, '施', '88888', 0, NULL, NULL, NULL, 1),
(2, '施dd', '888', 0, NULL, NULL, NULL, 1),
(3, 'shijianfeng20', '777', 0, NULL, NULL, NULL, 1);

--
-- 限制导出的表
--

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
