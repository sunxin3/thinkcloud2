# 地区

DROP TABLE IF EXISTS `thkcld_charge_regions`;
CREATE TABLE `thkcld_charge_regions` (

  `created_at` datetime DEFAULT NULL,

  `updated_at` datetime DEFAULT NULL,

  `deleted_at` datetime DEFAULT NULL,

  `deleted` tinyint(1) DEFAULT NULL,

  `id` int(11) NOT NULL AUTO_INCREMENT,

  `name` varchar(255) NOT NULL,

  PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 扣费项目表

DROP TABLE IF EXISTS `thkcld_charge_items`;
CREATE TABLE `thkcld_charge_items` (

  `created_at` datetime DEFAULT NULL,

  `updated_at` datetime DEFAULT NULL,

  `deleted_at` datetime DEFAULT NULL,

  `deleted` tinyint(1) DEFAULT NULL,

  `id` int(11) NOT NULL AUTO_INCREMENT,

  `name` varchar(255) NOT NULL,

  PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 虚拟机类型

DROP TABLE IF EXISTS `thkcld_charge_item_types`;
CREATE TABLE `thkcld_charge_item_types` (

  `created_at` datetime DEFAULT NULL,

  `updated_at` datetime DEFAULT NULL,

  `deleted_at` datetime DEFAULT NULL,

  `deleted` tinyint(1) DEFAULT NULL,

  `id` int(11) NOT NULL AUTO_INCREMENT,

  `name` varchar(255) NOT NULL,

  PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 计费周期类型

DROP TABLE IF EXISTS `thkcld_charge_payment_types`;
CREATE TABLE `thkcld_charge_payment_types` (

  `created_at` datetime DEFAULT NULL,

  `updated_at` datetime DEFAULT NULL,

  `deleted_at` datetime DEFAULT NULL,

  `deleted` tinyint(1) DEFAULT NULL,

  `id` int(11) NOT NULL AUTO_INCREMENT,

  `name` varchar(255) NOT NULL,

  `interval_unit` varchar(255) NOT NULL,

  `interval_size` int(11) NOT NULL,

  `is_prepaid` tinyint(1) NOT NULL,

  PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 产品表

DROP TABLE IF EXISTS `thkcld_charge_products`;
CREATE TABLE `thkcld_charge_products` (

  `created_at` datetime DEFAULT NULL,

  `updated_at` datetime DEFAULT NULL,

  `deleted_at` datetime DEFAULT NULL,

  `deleted` tinyint(1) DEFAULT NULL,

  `id` int(11) NOT NULL AUTO_INCREMENT,

  `region_id` int(11) NOT NULL,

  `item_id` int(11) NOT NULL,

  `item_type_id` int(11) NOT NULL,

  `payment_type_id` int(11) NOT NULL,

  `order_unit` varchar(255) NOT NULL,  # e.g) hours / days / months / KBytes / requests

  `order_size` int(11) NOT NULL,

  `price` float NOT NULL,

  `currency` varchar(255) NOT NULL,

  PRIMARY KEY (`id`),

  KEY `region_id` (`region_id`),

  KEY `item_id` (`item_id`),

  KEY `item_type_id` (`item_type_id`),

  KEY `payment_type_id` (`payment_type_id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 订单表
DROP TABLE IF EXISTS `thkcld_charge_subscriptions`;
CREATE TABLE `thkcld_charge_subscriptions` (

  `created_at` datetime DEFAULT NULL,

  `updated_at` datetime DEFAULT NULL,

  `deleted_at` datetime DEFAULT NULL,

  `deleted` tinyint(1) DEFAULT NULL,

  `id` int(11) NOT NULL AUTO_INCREMENT,

  `user_id` varchar(64) NOT NULL,

  `approver_id` varchar(64) NOT NULL,

  `project_id` varchar(64) NOT NULL,

  `product_id` int(11) NOT NULL,

  `resource_uuid` varchar(36) NOT NULL,

  `resource_name` varchar(255) NOT NULL,

  `applied_at` datetime DEFAULT NULL,

  `expires_at` datetime DEFAULT NULL,

  `approved_at` datetime DEFAULT NULL,

  `status` varchar(255) DEFAULT NULL,  # comfirmed, creating, deleting

  PRIMARY KEY (`id`),

  KEY `project_id` (`project_id`),

  KEY `product_id` (`product_id`),

  KEY `resource_uuid` (`resource_uuid`),

  KEY `expires_at` (`expires_at`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 扣费记录表

DROP TABLE IF EXISTS `thkcld_charge_purchases`;
CREATE TABLE `thkcld_charge_purchases` (

  `created_at` datetime DEFAULT NULL,

  `updated_at` datetime DEFAULT NULL,

  `deleted_at` datetime DEFAULT NULL,

  `deleted` tinyint(1) DEFAULT NULL,

  `id` int(11) NOT NULL AUTO_INCREMENT,

  `subscription_id` int(11) NOT NULL,

  `quantity` float NOT NULL,

  `line_total` float NOT NULL,

  `flag` tinyint(4) DEFAULT '0',

  PRIMARY KEY (`id`),

  KEY `subscription_id` (`subscription_id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#item_types
insert into thkcld_charge_item_types (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'m1.tiny');

insert into thkcld_charge_item_types (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'m1.small');

insert into thkcld_charge_item_types (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'m1.medium');

insert into thkcld_charge_item_types (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'m1.large');

insert into thkcld_charge_item_types (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'m1.xlarge');

#items
insert into thkcld_charge_items (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'instance');

insert into thkcld_charge_items (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'physical_server');

insert into thkcld_charge_items (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'hpc');

#payment_types
insert into thkcld_charge_payment_types (created_at,updated_at,deleted_at,deleted,name,interval_unit,interval_size,is_prepaid)values(now(),NULL,NULL,0,'hourly','hours',1,0);

insert into thkcld_charge_payment_types (created_at,updated_at,deleted_at,deleted,name,interval_unit,interval_size,is_prepaid)values(now(),NULL,NULL,0,'hourlypp','hours',1,1);

# products
insert into thkcld_charge_products (created_at,updated_at,deleted_at,deleted,region_id,item_id,item_type_id,payment_type_id,order_unit,order_size,price,currency)values(now(),NULL,NULL,0,1,1,1,1,'hours',6000,1,'yuan');

insert into thkcld_charge_products (created_at,updated_at,deleted_at,deleted,region_id,item_id,item_type_id,payment_type_id,order_unit,order_size,price,currency)values(now(),NULL,NULL,0,1,1,2,1,'hours',6000,2,'yuan');

insert into thkcld_charge_products (created_at,updated_at,deleted_at,deleted,region_id,item_id,item_type_id,payment_type_id,order_unit,order_size,price,currency)values(now(),NULL,NULL,0,1,1,3,1,'hours',6000,3,'yuan');

insert into thkcld_charge_products (created_at,updated_at,deleted_at,deleted,region_id,item_id,item_type_id,payment_type_id,order_unit,order_size,price,currency)values(now(),NULL,NULL,0,1,1,4,1,'hours',6000,4,'yuan');

insert into thkcld_charge_products (created_at,updated_at,deleted_at,deleted,region_id,item_id,item_type_id,payment_type_id,order_unit,order_size,price,currency)values(now(),NULL,NULL,0,1,1,5,1,'hours',6000,5,'yuan');

# regions
insert into thkcld_charge_regions (created_at,updated_at,deleted_at,deleted,name)values(now(),NULL,NULL,0,'lenovo');


# subscriptions
insert into thkcld_charge_subscriptions (created_at,updated_at,deleted_at,deleted,user_id,approver_id,project_id,product_id,resource_uuid,resource_name,applied_at,expires_at,approved_at,status)values(now(),NULL,NULL,0,1,1,1,1,1,'instance',now(),now(),now(),'terminated');
