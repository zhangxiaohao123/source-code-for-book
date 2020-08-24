/*
Navicat MySQL Data Transfer

Source Server         : aa
Source Server Version : 50545
Source Host           : localhost:3306
Source Database       : ckgl

Target Server Type    : MYSQL
Target Server Version : 50545
File Encoding         : 65001

Date: 2019-01-05 22:24:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `productinfo`
-- ----------------------------
DROP TABLE IF EXISTS `productinfo`;
CREATE TABLE `productinfo` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` int(255) DEFAULT NULL,
  `inver` varchar(255) DEFAULT NULL,
  `class` varchar(255) DEFAULT NULL,
  `supplier` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of productinfo
-- ----------------------------
INSERT INTO `productinfo` VALUES ('001', '轻型纸', '100', '110', '纸张', '常林纸业');
INSERT INTO `productinfo` VALUES ('002', '华为手机', '1000', '1180', '手机', '华为');

-- ----------------------------
-- Table structure for `supplier`
-- ----------------------------
DROP TABLE IF EXISTS `supplier`;
CREATE TABLE `supplier` (
  `supplier` varchar(255) NOT NULL,
  PRIMARY KEY (`supplier`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of supplier
-- ----------------------------
INSERT INTO `supplier` VALUES ('');
INSERT INTO `supplier` VALUES ('1');
INSERT INTO `supplier` VALUES ('s');
INSERT INTO `supplier` VALUES ('中兴');
INSERT INTO `supplier` VALUES ('北电');
INSERT INTO `supplier` VALUES ('华为');
INSERT INTO `supplier` VALUES ('河南大学');
INSERT INTO `supplier` VALUES ('河南科技大学');
INSERT INTO `supplier` VALUES ('清华大学');
INSERT INTO `supplier` VALUES ('郑州大学');
INSERT INTO `supplier` VALUES ('郑州轻工业学院');

-- ----------------------------
-- Table structure for `supplierinfo`
-- ----------------------------
DROP TABLE IF EXISTS `supplierinfo`;
CREATE TABLE `supplierinfo` (
  `name` varchar(255) NOT NULL,
  `tradename` varchar(255) DEFAULT NULL,
  `tradeprice` varchar(255) DEFAULT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of supplierinfo
-- ----------------------------
INSERT INTO `supplierinfo` VALUES ('一汽大众', '奥迪', '1000', '999999', '长春');
INSERT INTO `supplierinfo` VALUES ('华为', '华为手机', '100', '8888', '深圳');
INSERT INTO `supplierinfo` VALUES ('常林纸业', '轻型纸', '1000', '88888888', '上海新沛');

-- ----------------------------
-- Table structure for `userinfo`
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `user` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES ('123', '123');
INSERT INTO `userinfo` VALUES ('admin', '123');
INSERT INTO `userinfo` VALUES ('test', 'test2');
