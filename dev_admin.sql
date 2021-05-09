/*
 Navicat Premium Data Transfer

 Source Server         : localhsot
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : localhost:3306
 Source Schema         : dev_admin

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 08/05/2021 13:41:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 53 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add 用户角色', 6, 'add_role');
INSERT INTO `auth_permission` VALUES (22, 'Can change 用户角色', 6, 'change_role');
INSERT INTO `auth_permission` VALUES (23, 'Can delete 用户角色', 6, 'delete_role');
INSERT INTO `auth_permission` VALUES (24, 'Can view 用户角色', 6, 'view_role');
INSERT INTO `auth_permission` VALUES (25, 'Can add 权限角色列表', 7, 'add_permissionrole');
INSERT INTO `auth_permission` VALUES (26, 'Can change 权限角色列表', 7, 'change_permissionrole');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 权限角色列表', 7, 'delete_permissionrole');
INSERT INTO `auth_permission` VALUES (28, 'Can view 权限角色列表', 7, 'view_permissionrole');
INSERT INTO `auth_permission` VALUES (29, 'Can add 权限基础信息列表', 8, 'add_permission');
INSERT INTO `auth_permission` VALUES (30, 'Can change 权限基础信息列表', 8, 'change_permission');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 权限基础信息列表', 8, 'delete_permission');
INSERT INTO `auth_permission` VALUES (32, 'Can view 权限基础信息列表', 8, 'view_permission');
INSERT INTO `auth_permission` VALUES (33, 'Can add 部门信息', 9, 'add_department');
INSERT INTO `auth_permission` VALUES (34, 'Can change 部门信息', 9, 'change_department');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 部门信息', 9, 'delete_department');
INSERT INTO `auth_permission` VALUES (36, 'Can view 部门信息', 9, 'view_department');
INSERT INTO `auth_permission` VALUES (37, 'Can add 系统用户', 10, 'add_sysuser');
INSERT INTO `auth_permission` VALUES (38, 'Can change 系统用户', 10, 'change_sysuser');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 系统用户', 10, 'delete_sysuser');
INSERT INTO `auth_permission` VALUES (40, 'Can view 系统用户', 10, 'view_sysuser');
INSERT INTO `auth_permission` VALUES (41, 'Can add 导航菜单表', 11, 'add_menu');
INSERT INTO `auth_permission` VALUES (42, 'Can change 导航菜单表', 11, 'change_menu');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 导航菜单表', 11, 'delete_menu');
INSERT INTO `auth_permission` VALUES (44, 'Can view 导航菜单表', 11, 'view_menu');
INSERT INTO `auth_permission` VALUES (45, 'Can add 商品分类表', 12, 'add_goodscategory');
INSERT INTO `auth_permission` VALUES (46, 'Can change 商品分类表', 12, 'change_goodscategory');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 商品分类表', 12, 'delete_goodscategory');
INSERT INTO `auth_permission` VALUES (48, 'Can view 商品分类表', 12, 'view_goodscategory');
INSERT INTO `auth_permission` VALUES (49, 'Can add 商品信息', 13, 'add_goods');
INSERT INTO `auth_permission` VALUES (50, 'Can change 商品信息', 13, 'change_goods');
INSERT INTO `auth_permission` VALUES (51, 'Can delete 商品信息', 13, 'delete_goods');
INSERT INTO `auth_permission` VALUES (52, 'Can view 商品信息', 13, 'view_goods');

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_no` int(11) NOT NULL,
  `dept_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `charge_person` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `show_no` int(11) NOT NULL,
  `tel` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` int(11) NOT NULL,
  `parent_comment_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `department_parent_comment_id_393adb86_fk_department_id`(`parent_comment_id`) USING BTREE,
  CONSTRAINT `department_parent_comment_id_393adb86_fk_department_id` FOREIGN KEY (`parent_comment_id`) REFERENCES `department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES (1, 2, '董办', 'blink', '1@1.com', 1001, '123', 1, NULL);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_sys_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_sys_user_id` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (13, 'goods', 'goods');
INSERT INTO `django_content_type` VALUES (12, 'goods', 'goodscategory');
INSERT INTO `django_content_type` VALUES (11, 'menu', 'menu');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (9, 'user_manage', 'department');
INSERT INTO `django_content_type` VALUES (8, 'user_manage', 'permission');
INSERT INTO `django_content_type` VALUES (7, 'user_manage', 'permissionrole');
INSERT INTO `django_content_type` VALUES (6, 'user_manage', 'role');
INSERT INTO `django_content_type` VALUES (10, 'user_manage', 'sysuser');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2020-07-04 09:25:43.753708');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2020-07-04 09:25:44.901491');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2020-07-04 09:25:46.280547');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2020-07-04 09:25:49.251726');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2020-07-04 09:25:49.289400');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2020-07-04 09:25:49.327318');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2020-07-04 09:25:49.361148');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2020-07-04 09:25:49.396054');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2020-07-04 09:25:49.433981');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2020-07-04 09:25:49.467861');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2020-07-04 09:25:49.500826');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2020-07-04 09:25:50.084977');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2020-07-04 09:25:50.122026');
INSERT INTO `django_migrations` VALUES (14, 'user_manage', '0001_initial', '2020-07-04 09:25:52.481827');
INSERT INTO `django_migrations` VALUES (15, 'admin', '0001_initial', '2020-07-04 09:26:02.194336');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0002_logentry_remove_auto_add', '2020-07-04 09:26:04.361663');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0003_logentry_add_action_flag_choices', '2020-07-04 09:26:04.404538');
INSERT INTO `django_migrations` VALUES (18, 'menu', '0001_initial', '2020-07-04 09:26:04.941128');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2020-07-04 09:26:06.453371');
INSERT INTO `django_migrations` VALUES (20, 'goods', '0001_initial', '2020-07-23 13:44:42.131826');
INSERT INTO `django_migrations` VALUES (21, 'auth', '0012_alter_user_first_name_max_length', '2021-03-14 09:18:22.925812');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for goods_category
-- ----------------------------
DROP TABLE IF EXISTS `goods_category`;
CREATE TABLE `goods_category`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cate_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `category_type` smallint(6) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `parent_category_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `goods_category_parent_category_id_3230c112_fk_goods_category_id`(`parent_category_id`) USING BTREE,
  CONSTRAINT `goods_category_parent_category_id_3230c112_fk_goods_category_id` FOREIGN KEY (`parent_category_id`) REFERENCES `goods_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods_category
-- ----------------------------
INSERT INTO `goods_category` VALUES (1, '家电', 1, '2020-07-23 22:00:54.000000', 1, NULL);
INSERT INTO `goods_category` VALUES (2, '冰箱', 2, '2020-07-23 22:01:27.000000', 1, 1);
INSERT INTO `goods_category` VALUES (3, '洗衣机', 2, '2020-07-23 22:01:48.000000', 1, 1);
INSERT INTO `goods_category` VALUES (4, '节能冰箱', 3, '2020-07-23 22:02:27.000000', 1, 2);
INSERT INTO `goods_category` VALUES (5, '聚能装冰箱', 3, '2020-07-23 22:03:40.000000', 1, 2);
INSERT INTO `goods_category` VALUES (6, '滚筒洗衣机', 3, '2020-07-23 22:04:07.000000', 1, 3);
INSERT INTO `goods_category` VALUES (7, '小型洗衣机', 3, '2020-07-23 22:04:36.000000', 1, 3);

-- ----------------------------
-- Table structure for goods_goods
-- ----------------------------
DROP TABLE IF EXISTS `goods_goods`;
CREATE TABLE `goods_goods`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `goods_sn` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `click_num` int(11) NOT NULL,
  `sold_num` int(11) NOT NULL,
  `fav_num` int(11) NOT NULL,
  `goods_num` int(11) NOT NULL,
  `market_price` decimal(11, 3) NOT NULL,
  `shop_price` decimal(11, 3) NOT NULL,
  `descripte` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `goods_front_image` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_hot` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `goods_goods_category_id_da3507dd_fk_goods_category_id`(`category_id`) USING BTREE,
  CONSTRAINT `goods_goods_category_id_da3507dd_fk_goods_category_id` FOREIGN KEY (`category_id`) REFERENCES `goods_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods_goods
-- ----------------------------

-- ----------------------------
-- Table structure for menu_menu
-- ----------------------------
DROP TABLE IF EXISTS `menu_menu`;
CREATE TABLE `menu_menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `authName` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_type` int(11) NOT NULL,
  `parent_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `menu_menu_parent_id_a0981d51_fk_menu_menu_id`(`parent_id`) USING BTREE,
  CONSTRAINT `menu_menu_parent_id_a0981d51_fk_menu_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `menu_menu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of menu_menu
-- ----------------------------
INSERT INTO `menu_menu` VALUES (1, '用户管理', 'users', 1, NULL);
INSERT INTO `menu_menu` VALUES (2, '权限管理', 'rights', 1, NULL);
INSERT INTO `menu_menu` VALUES (3, '商品管理', 'goods', 1, NULL);
INSERT INTO `menu_menu` VALUES (4, '订单管理', 'orders', 1, NULL);
INSERT INTO `menu_menu` VALUES (5, '数据统计', 'reports', 1, NULL);
INSERT INTO `menu_menu` VALUES (6, '用户列表', 'users', 2, 1);
INSERT INTO `menu_menu` VALUES (7, '角色列表', 'roles', 2, 2);
INSERT INTO `menu_menu` VALUES (8, '权限列表', 'rights', 2, 2);
INSERT INTO `menu_menu` VALUES (9, '商品分类', 'categories', 2, 3);
INSERT INTO `menu_menu` VALUES (10, '商品列表', 'goods', 2, 3);
INSERT INTO `menu_menu` VALUES (11, '分类参数', 'param', 2, 3);

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `per_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `level` int(11) NOT NULL,
  `children_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `permission_children_id_115da0cb_fk_permission_id`(`children_id`) USING BTREE,
  CONSTRAINT `permission_children_id_115da0cb_fk_permission_id` FOREIGN KEY (`children_id`) REFERENCES `permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of permission
-- ----------------------------
INSERT INTO `permission` VALUES (1, '商品管理', NULL, 1, NULL);
INSERT INTO `permission` VALUES (2, '删除商品', NULL, 3, 3);
INSERT INTO `permission` VALUES (3, '商品列表', 'goods', 2, 1);
INSERT INTO `permission` VALUES (4, '用户管理', NULL, 1, NULL);
INSERT INTO `permission` VALUES (5, '用户列表', 'users', 2, 4);
INSERT INTO `permission` VALUES (6, '添加用户', NULL, 3, 5);
INSERT INTO `permission` VALUES (7, '编辑用户', NULL, 3, 5);
INSERT INTO `permission` VALUES (8, '删除用户', NULL, 3, 5);
INSERT INTO `permission` VALUES (9, '权限管理', NULL, 1, NULL);
INSERT INTO `permission` VALUES (10, '权限列表', 'rights', 2, 9);
INSERT INTO `permission` VALUES (11, '角色列表', 'roles', 2, 9);
INSERT INTO `permission` VALUES (12, '添加权限', NULL, 3, 10);
INSERT INTO `permission` VALUES (13, '编辑权限', NULL, 3, 10);
INSERT INTO `permission` VALUES (14, '添加角色', NULL, 3, 11);
INSERT INTO `permission` VALUES (15, '编辑角色', NULL, 3, 11);
INSERT INTO `permission` VALUES (16, '添加商品', NULL, 3, 3);
INSERT INTO `permission` VALUES (17, '编辑商品', NULL, 3, 3);

-- ----------------------------
-- Table structure for permission_role
-- ----------------------------
DROP TABLE IF EXISTS `permission_role`;
CREATE TABLE `permission_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `per_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `level` int(11) NOT NULL,
  `children_id` int(11) NULL DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 93 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of permission_role
-- ----------------------------
INSERT INTO `permission_role` VALUES (86, '商品管理', '', 1, NULL, 1, 1);
INSERT INTO `permission_role` VALUES (87, '商品列表', '', 2, 86, 1, 3);
INSERT INTO `permission_role` VALUES (88, '用户管理', '', 1, NULL, 1, 4);
INSERT INTO `permission_role` VALUES (89, '用户列表', '', 2, 88, 1, 5);
INSERT INTO `permission_role` VALUES (90, '添加用户', '', 3, 89, 1, 6);
INSERT INTO `permission_role` VALUES (91, '编辑用户', '', 3, 89, 1, 7);
INSERT INTO `permission_role` VALUES (92, '编辑商品', '', 3, 87, 1, 17);

-- ----------------------------
-- Table structure for permission_role_0712
-- ----------------------------
DROP TABLE IF EXISTS `permission_role_0712`;
CREATE TABLE `permission_role_0712`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  INDEX `permission_id`(`permission_id`) USING BTREE,
  CONSTRAINT `permission_id` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `role_id` FOREIGN KEY (`role_id`) REFERENCES `user_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of permission_role_0712
-- ----------------------------
INSERT INTO `permission_role_0712` VALUES (1, 1, 1);
INSERT INTO `permission_role_0712` VALUES (2, 1, 2);
INSERT INTO `permission_role_0712` VALUES (3, 1, 3);

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `mobile` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `state` tinyint(1) NULL DEFAULT NULL,
  `dept_id` int(11) NULL DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  INDEX `sys_user_dept_id_aad432e7_fk_department_id`(`dept_id`) USING BTREE,
  INDEX `sys_user_role_id_8a2e10d7_fk_user_role_id`(`role_id`) USING BTREE,
  CONSTRAINT `sys_user_dept_id_aad432e7_fk_department_id` FOREIGN KEY (`dept_id`) REFERENCES `department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_role_id_8a2e10d7_fk_user_role_id` FOREIGN KEY (`role_id`) REFERENCES `user_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES (3, 'pbkdf2_sha256$216000$YnevszKkQp7H$pUzRfwtOS2Wrli4EBZCOb31Zx3WPjVv8q9fnI5uacVw=', '2020-07-04 17:40:43.000000', 1, 'admin', '', '', '12@13.com', 1, 1, '2020-07-04 17:39:37.000000', '15070070522', '1', NULL, 1, NULL, 1);
INSERT INTO `sys_user` VALUES (4, 'pbkdf2_sha256$180000$yYGtkssWQx9W$Ahca9Z8+ACxAH5frU8+w6hhseHGE08x1xftTvU82R8s=', '2020-07-04 17:41:22.000000', 0, 'blink', '', '', '1@12.com', 0, 1, '2020-06-14 09:28:30.928454', '15070070522', 'male', '', 0, NULL, 1);
INSERT INTO `sys_user` VALUES (5, 'pbkdf2_sha256$180000$W0vWJbZ5tAWV$UHyBO2/1K/E/6CL9vs7muDXd4jo3IFubxy7STMyTaxY=', '2020-07-04 17:41:24.000000', 0, 'blink01', '', '', '', 0, 1, '2020-06-14 09:28:48.212530', '15070070522', 'male', '', 1, NULL, 2);
INSERT INTO `sys_user` VALUES (6, 'pbkdf2_sha256$180000$nqUZ8SiXE16o$JtcUAQcFFBLd/TNtHZw5Nrw5ONiNb84VvM3t3LpxnPg=', '2020-07-04 17:41:26.000000', 0, 'admin1', '', '', '1@22.com', 0, 1, '2020-06-15 15:04:59.515993', '15070070752', 'male', '', 1, NULL, 1);
INSERT INTO `sys_user` VALUES (7, 'pbkdf2_sha256$180000$W0vWJbZ5tAWV$UHyBO2/1K/E/6CL9vs7muDXd4jo3IFubxy7STMyTaxY=', '2020-07-04 17:41:17.000000', 1, 'admin12', '', '', '12@13.com', 1, 1, '2020-06-14 09:27:10.011292', '15070070522', 'male', '', 1, NULL, 1);

-- ----------------------------
-- Table structure for sys_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_groups`;
CREATE TABLE `sys_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sysuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `sys_user_groups_sysuser_id_group_id_d89870ff_uniq`(`sysuser_id`, `group_id`) USING BTREE,
  INDEX `sys_user_groups_group_id_9b8b43fc_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `sys_user_groups_group_id_9b8b43fc_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_groups_sysuser_id_c05c83fe_fk_sys_user_id` FOREIGN KEY (`sysuser_id`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for sys_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_user_permissions`;
CREATE TABLE `sys_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sysuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `sys_user_user_permissions_sysuser_id_permission_id_e0fa024f_uniq`(`sysuser_id`, `permission_id`) USING BTREE,
  INDEX `sys_user_user_permis_permission_id_55623e22_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `sys_user_user_permis_permission_id_55623e22_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_user_permissions_sysuser_id_66b315b8_fk_sys_user_id` FOREIGN KEY (`sysuser_id`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_no` int(11) NOT NULL,
  `role_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role_descripte` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` int(11) NOT NULL,
  `show_no` int(11) NOT NULL,
  `create_time` date NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_role
-- ----------------------------
INSERT INTO `user_role` VALUES (1, 1, '超级管理员', 'aaa', 1, 1001, '2020-06-14');
INSERT INTO `user_role` VALUES (2, 2, '开发主管', 'bbb', 1, 1002, '2020-06-14');

SET FOREIGN_KEY_CHECKS = 1;
