-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 20, 2014 at 11:03 PM
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
-- Table structure for table `thkcld_disks`
--
DROP TABLE IF EXISTS `thkcld_disks`;
CREATE TABLE IF NOT EXISTS `thkcld_disks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manufacture` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL,
  `interface` varchar(255) NOT NULL,
  `rpm` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `thkcld_hbas`
--

DROP TABLE IF EXISTS `thkcld_hbas`;
CREATE TABLE IF NOT EXISTS `thkcld_hbas` (
  `sn` varchar(255) NOT NULL,
  `type_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `thkcld_hba_types`
--
DROP TABLE IF EXISTS `thkcld_hba_types`;
CREATE TABLE IF NOT EXISTS `thkcld_hba_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(64) NOT NULL,
  `manufacture` varchar(128) NOT NULL,
  `bandwidth` int(11) NOT NULL COMMENT 'Unit: Gb',
  `port_number` tinyint(4) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `thkcld_hba_types`
--

INSERT INTO `thkcld_hba_types` (`id`, `model`, `manufacture`, `bandwidth`, `port_number`, `created_at`, `updated_at`, `deleted_at`, `deleted`, `description`) VALUES
(1, 'LPe1250', 'Emulex', 8, 1, '2014-02-20 16:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'Emulex LPe1250 Fibre Channel card');

-- --------------------------------------------------------

--
-- Table structure for table `thkcld_nics`
--
DROP TABLE IF EXISTS `thkcld_nics`;
CREATE TABLE IF NOT EXISTS `thkcld_nics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_onboard` tinyint(1) NOT NULL,
  `interface_number` tinyint(4) NOT NULL,
  `interface` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

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
  PRIMARY KEY (`id`),
  KEY `fk_servers_server_models_idx` (`server_models_id`),
  KEY `fk_servers_power_states1_idx` (`power_states_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `thkcld_physical_servers`
--

INSERT INTO `thkcld_physical_servers` (`id`, `created_at`, `updated_at`, `deleted_at`, `deleted`, `user_id`, `server_models_id`, `region_id`, `locked_by`, `is_public`, `power_states_id`, `nc_number`, `name`, `description`, `ipmi_address`, `cpu_fre`, `cpu_core_num`, `cpu_desc`, `mem_total`, `mem_desc`, `disk_num`, `disk_desc`, `nic_num`, `nic_desc`, `hba_attached`, `hba_port_num`, `cpu_socket_num`, `disk_total`, `raid_internal`, `raid_external`, `hba_cards_id`) VALUES
(1, '2013-11-27 00:00:00', '2013-12-03 00:00:00', NULL, 0, NULL, 1, NULL, NULL, 1, 1, 'NC10000', 'Ironman', NULL, '10.12.12.12', 3.4, 4, '1 x Intel® Ci3-4130 processor 3.4 GHz, 2C, 4M Cache, 1.00 GT/s, 65W', 4, '4 GB (1 x 4 GB PC3-12800E 1600MHz DDR3 ECC-UD', 1, NULL, NULL, NULL, NULL, NULL, NULL, 500, NULL, NULL, 0),
(2, '2013-11-27 00:00:00', '2013-12-03 00:00:00', NULL, 0, NULL, 2, NULL, NULL, 1, 1, 'NC10001', 'Spiderman', NULL, '12.12.12.13', 3.5, 4, '1 x Intel® Ci3-4130 processor 3.4 GHz, 2C, 4M Cache, 1.00 GT/s, 65W', 4, '4 GB (1 x 4 GB PC3-12800E 1600MHz DDR3 ECC-UD', 1, '1 x 500 GB 7200 RPM 3.5" DC SATA', NULL, NULL, NULL, NULL, 2, 500, NULL, NULL, NULL);

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
-- Table structure for table `thkcld_rams`
--
DROP TABLE IF EXISTS `thkcld_rams`;
CREATE TABLE IF NOT EXISTS `thkcld_rams` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(64) NOT NULL,
  `frequence` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `thkcld_rams`
--

INSERT INTO `thkcld_rams` (`id`, `type`, `frequence`, `capacity`, `quantity`, `created_at`, `updated_at`, `deleted_at`, `deleted`, `description`) VALUES
(1, 'RDIMM', 1333, 4, 1, '2014-02-19 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, ''),
(2, 'UDIMM', 1600, 4, 2, '2014-02-19 09:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, '');

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
(1, NULL, NULL, NULL, 0, 'RD630'),
(2, NULL, NULL, NULL, 0, 'RD420'),
(3, '2013-12-07 02:58:16', NULL, '2013-12-07 05:59:01', 3, 'RD220'),
(4, '2013-12-07 07:11:24', NULL, NULL, 0, 'RD320'),
(5, '2013-12-07 07:16:34', NULL, '2013-12-07 07:32:16', 5, 'RD520');

-- --------------------------------------------------------

--
-- Table structure for table `thkcld_server_ram_map`
--

DROP TABLE IF EXISTS `thkcld_server_ram_map`;
CREATE TABLE IF NOT EXISTS `thkcld_server_ram_map` (
  `server_id` int(11) NOT NULL,
  `ram_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `thkcld_server_ram_map`
--

INSERT INTO `thkcld_server_ram_map` (`server_id`, `ram_id`) VALUES
(1, 2),
(1, 1),
(2, 1);

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
