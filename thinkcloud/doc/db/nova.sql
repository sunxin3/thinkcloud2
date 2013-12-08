-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 07, 2013 at 05:54 PM
-- Server version: 5.5.34
-- PHP Version: 5.3.10-1ubuntu3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `nova`
--

-- --------------------------------------------------------

--
-- Table structure for table `thkcld_physical_servers`
--

DROP TABLE IF EXISTS `thkcld_physical_servers`;
CREATE TABLE IF NOT EXISTS `thkcld_physical_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `server_models_id` int(11) NOT NULL,
  `region_id` int(11) DEFAULT NULL,
  `locked_by` tinyint(4) DEFAULT NULL COMMENT 'server can be locked by one server apply',
  `is_public` tinyint(1) DEFAULT NULL,
  `power_states_id` int(11) NOT NULL DEFAULT '0',
  `nc_number` varchar(64) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `ipmi_address` varchar(255) DEFAULT NULL,
  `cpu_fre` float DEFAULT NULL COMMENT 'without the curency, only digi value',
  `cpu_core_num` tinyint(4) DEFAULT NULL COMMENT 'pythical',
  `cpu_desc` varchar(255) DEFAULT NULL COMMENT 'value for example: Intel(R) Xeon(R) CPU E5645 @ 2.40Ghz',
  `mem_total` int(11) DEFAULT NULL COMMENT 'without currency, only digi value.',
  `mem_desc` varchar(45) DEFAULT NULL,
  `disk_num` int(11) DEFAULT NULL,
  `disk_desc` varchar(255) DEFAULT NULL COMMENT 'value: big size of disk or small size of disk',
  `nic_num` int(11) DEFAULT NULL,
  `nic_desc` varchar(45) DEFAULT NULL COMMENT 'nic_desc-need to set the max network width, like: 1.0GHz',
  `hba_attached` tinyint(1) DEFAULT NULL,
  `hba_port_num` tinyint(4) DEFAULT NULL,
  `cpu_socket_num` tinyint(4) DEFAULT NULL,
  `disk_total` int(11) DEFAULT NULL COMMENT 'only value',
  `raid_internal` varchar(45) DEFAULT NULL COMMENT 'only raid card model',
  `raid_external` varchar(45) DEFAULT NULL COMMENT 'only raid card model',
  `hba_cards_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`,`server_models_id`,`power_states_id`),
  KEY `fk_servers_server_models_idx` (`server_models_id`),
  KEY `fk_servers_power_states1_idx` (`power_states_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `thkcld_physical_servers`
--

INSERT INTO `thkcld_physical_servers` (`id`, `created_at`, `updated_at`, `deleted_at`, `deleted`, `user_id`, `server_models_id`, `region_id`, `locked_by`, `is_public`, `power_states_id`, `nc_number`, `name`, `description`, `ipmi_address`, `cpu_fre`, `cpu_core_num`, `cpu_desc`, `mem_total`, `mem_desc`, `disk_num`, `disk_desc`, `nic_num`, `nic_desc`, `hba_attached`, `hba_port_num`, `cpu_socket_num`, `disk_total`, `raid_internal`, `raid_external`, `hba_cards_id`) VALUES
(1, '2013-11-27 00:00:00', '2013-12-03 00:00:00', NULL, NULL, NULL, 1, NULL, NULL, 1, 1, NULL, 'RD620', NULL, NULL, 3.4, 4, '1 x Intel® Ci3-4130 processor 3.4 GHz, 2C, 4M Cache, 1.00 GT/s, 65W', 4, '4 GB (1 x 4 GB PC3-12800E 1600MHz DDR3 ECC-UD', 1, NULL, NULL, NULL, NULL, NULL, NULL, 500, NULL, NULL, 0),
(2, '2013-11-27 00:00:00', '2013-12-03 00:00:00', NULL, NULL, NULL, 2, NULL, NULL, 1, 1, NULL, 'TS140', NULL, NULL, 3.5, 4, '1 x Intel® Ci3-4130 processor 3.4 GHz, 2C, 4M Cache, 1.00 GT/s, 65W', 4, '4 GB (1 x 4 GB PC3-12800E 1600MHz DDR3 ECC-UD', 1, '1 x 500 GB 7200 RPM 3.5" DC SATA', NULL, NULL, NULL, NULL, 2, 500, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `thkcld_power_states`
--

DROP TABLE IF EXISTS `thkcld_power_states`;
CREATE TABLE IF NOT EXISTS `thkcld_power_states` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `state` varchar(64) DEFAULT NULL COMMENT 'key_value:\n1. rebooting\n2. poweroff\n3. running\n4. pxe_linux\n5. bois',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `thkcld_power_states`
--

INSERT INTO `thkcld_power_states` (`id`, `created_at`, `updated_at`, `deleted_at`, `deleted`, `state`) VALUES
(1, NULL, NULL, NULL, NULL, 'running'),
(2, NULL, NULL, NULL, NULL, 'poweroff');

-- --------------------------------------------------------

--
-- Table structure for table `thkcld_server_models`
--

DROP TABLE IF EXISTS `thkcld_server_models`;
CREATE TABLE IF NOT EXISTS `thkcld_server_models` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `thkcld_server_models`
--

INSERT INTO `thkcld_server_models` (`id`, `created_at`, `updated_at`, `deleted_at`, `deleted`, `name`) VALUES
(1, NULL, NULL, NULL, 0, 'RD620'),
(2, NULL, NULL, NULL, 0, 'RD420'),
(3, '2013-12-07 02:58:16', NULL, '2013-12-07 05:59:01', 3, 'RD220'),
(4, '2013-12-07 07:11:24', NULL, NULL, 0, 'RD320'),
(5, '2013-12-07 07:16:34', NULL, '2013-12-07 07:32:16', 5, 'RD520');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `thkcld_physical_servers`
--
ALTER TABLE `thkcld_physical_servers`
  ADD CONSTRAINT `fk_servers_power_states1` FOREIGN KEY (`power_states_id`) REFERENCES `thkcld_power_states` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_servers_server_models` FOREIGN KEY (`server_models_id`) REFERENCES `thkcld_server_models` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
