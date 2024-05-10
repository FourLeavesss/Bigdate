/*
 Navicat Premium Data Transfer

 Source Server         : Desktop
 Source Server Type    : SQLite
 Source Server Version : 3035005
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3035005
 File Encoding         : 65001

 Date: 01/04/2024 16:19:01
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for BarData
-- ----------------------------
DROP TABLE IF EXISTS "BarData";
CREATE TABLE "BarData" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" varchar(255) NOT NULL,
  "tname" varchar(255) NOT NULL,
  "short_link" varchar(255) NOT NULL,
  "view" integer NOT NULL,
  "author" varchar(255) NOT NULL,
  "src" varchar(255) NOT NULL,
  "danmaku" integer NOT NULL,
  "like" integer NOT NULL,
  "share" integer NOT NULL,
  "favorite" integer NOT NULL,
  "reply" integer NOT NULL,
  "pub_location" varchar(255),
  "pubdate" date
);

-- ----------------------------
-- Table structure for BarsData
-- ----------------------------
DROP TABLE IF EXISTS "BarsData";
CREATE TABLE "BarsData" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" varchar(255) NOT NULL,
  "tname" varchar(255) NOT NULL,
  "short_link" varchar(255) NOT NULL,
  "view" integer NOT NULL,
  "author" varchar(255) NOT NULL,
  "src" varchar(255) NOT NULL,
  "danmaku" integer NOT NULL,
  "like" integer NOT NULL,
  "share" integer NOT NULL,
  "favorite" integer NOT NULL,
  "reply" integer NOT NULL,
  "pub_location" varchar(255),
  "pubdate" date
);

-- ----------------------------
-- Table structure for Colect
-- ----------------------------
DROP TABLE IF EXISTS "Colect";
CREATE TABLE "Colect" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "co_title" varchar(255) NOT NULL,
  "co_down_link" varchar(255) NOT NULL,
  "co_down_img" varchar(255) NOT NULL
);

-- ----------------------------
-- Table structure for History
-- ----------------------------
DROP TABLE IF EXISTS "History";
CREATE TABLE "History" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" varchar(255) NOT NULL,
  "tname" varchar(255) NOT NULL,
  "short_link" varchar(255) NOT NULL,
  "view" integer NOT NULL,
  "author" varchar(255) NOT NULL,
  "src" varchar(255) NOT NULL,
  "danmaku" integer NOT NULL,
  "like" integer NOT NULL,
  "share" integer NOT NULL,
  "favorite" integer NOT NULL,
  "reply" integer NOT NULL,
  "pub_location" varchar(255),
  "pubdate" date
);

-- ----------------------------
-- Table structure for LintData
-- ----------------------------
DROP TABLE IF EXISTS "LintData";
CREATE TABLE "LintData" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" varchar(255) NOT NULL,
  "tname" varchar(255) NOT NULL,
  "short_link" varchar(255) NOT NULL,
  "view" integer NOT NULL,
  "author" varchar(255) NOT NULL,
  "src" varchar(255) NOT NULL,
  "danmaku" integer NOT NULL,
  "like" integer NOT NULL,
  "share" integer NOT NULL,
  "favorite" integer NOT NULL,
  "reply" integer NOT NULL,
  "pub_location" varchar(255),
  "pubdate" date
);

-- ----------------------------
-- Table structure for PieData
-- ----------------------------
DROP TABLE IF EXISTS "PieData";
CREATE TABLE "PieData" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" varchar(255) NOT NULL,
  "tname" varchar(255) NOT NULL,
  "short_link" varchar(255) NOT NULL,
  "view" integer NOT NULL,
  "author" varchar(255) NOT NULL,
  "src" varchar(255) NOT NULL,
  "danmaku" integer NOT NULL,
  "like" integer NOT NULL,
  "share" integer NOT NULL,
  "favorite" integer NOT NULL,
  "reply" integer NOT NULL,
  "pub_location" varchar(255),
  "pubdate" date
);

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS "auth_group";
CREATE TABLE "auth_group" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(150) NOT NULL,
  UNIQUE ("name" ASC)
);

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS "auth_group_permissions";
CREATE TABLE "auth_group_permissions" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "group_id" integer NOT NULL,
  "permission_id" integer NOT NULL,
  FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS "auth_permission";
CREATE TABLE "auth_permission" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "content_type_id" integer NOT NULL,
  "codename" varchar(100) NOT NULL,
  "name" varchar(255) NOT NULL,
  FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS "auth_user";
CREATE TABLE "auth_user" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "password" varchar(128) NOT NULL,
  "last_login" datetime,
  "is_superuser" bool NOT NULL,
  "username" varchar(150) NOT NULL,
  "last_name" varchar(150) NOT NULL,
  "email" varchar(254) NOT NULL,
  "is_staff" bool NOT NULL,
  "is_active" bool NOT NULL,
  "date_joined" datetime NOT NULL,
  "first_name" varchar(150) NOT NULL,
  UNIQUE ("username" ASC)
);

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS "auth_user_groups";
CREATE TABLE "auth_user_groups" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "user_id" integer NOT NULL,
  "group_id" integer NOT NULL,
  FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS "auth_user_user_permissions";
CREATE TABLE "auth_user_user_permissions" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "user_id" integer NOT NULL,
  "permission_id" integer NOT NULL,
  FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS "django_admin_log";
CREATE TABLE "django_admin_log" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "action_time" datetime NOT NULL,
  "object_id" text,
  "object_repr" varchar(200) NOT NULL,
  "change_message" text NOT NULL,
  "content_type_id" integer,
  "user_id" integer NOT NULL,
  "action_flag" smallint unsigned NOT NULL,
  FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED,
   ("action_flag" >= 0)
);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS "django_content_type";
CREATE TABLE "django_content_type" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "app_label" varchar(100) NOT NULL,
  "model" varchar(100) NOT NULL
);

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS "django_migrations";
CREATE TABLE "django_migrations" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "app" varchar(255) NOT NULL,
  "name" varchar(255) NOT NULL,
  "applied" datetime NOT NULL
);

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS "django_session";
CREATE TABLE "django_session" (
  "session_key" varchar(40) NOT NULL,
  "session_data" text NOT NULL,
  "expire_date" datetime NOT NULL,
  PRIMARY KEY ("session_key")
);

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "sqlite_sequence";
CREATE TABLE "sqlite_sequence" (
  "name",
  "seq"
);

-- ----------------------------
-- Auto increment value for BarData
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 559 WHERE name = 'BarData';

-- ----------------------------
-- Auto increment value for BarsData
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 711 WHERE name = 'BarsData';

-- ----------------------------
-- Auto increment value for Colect
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 19 WHERE name = 'Colect';

-- ----------------------------
-- Auto increment value for History
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 1898 WHERE name = 'History';

-- ----------------------------
-- Auto increment value for LintData
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 110 WHERE name = 'LintData';

-- ----------------------------
-- Auto increment value for PieData
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 794 WHERE name = 'PieData';

-- ----------------------------
-- Auto increment value for auth_group
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 2 WHERE name = 'auth_group';

-- ----------------------------
-- Auto increment value for auth_group_permissions
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 21 WHERE name = 'auth_group_permissions';

-- ----------------------------
-- Indexes structure for table auth_group_permissions
-- ----------------------------
CREATE INDEX "auth_group_permissions_group_id_b120cbf9"
ON "auth_group_permissions" (
  "group_id" ASC
);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq"
ON "auth_group_permissions" (
  "group_id" ASC,
  "permission_id" ASC
);
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e"
ON "auth_group_permissions" (
  "permission_id" ASC
);

-- ----------------------------
-- Auto increment value for auth_permission
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 48 WHERE name = 'auth_permission';

-- ----------------------------
-- Indexes structure for table auth_permission
-- ----------------------------
CREATE INDEX "auth_permission_content_type_id_2f476e4b"
ON "auth_permission" (
  "content_type_id" ASC
);
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq"
ON "auth_permission" (
  "content_type_id" ASC,
  "codename" ASC
);

-- ----------------------------
-- Auto increment value for auth_user
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 3 WHERE name = 'auth_user';

-- ----------------------------
-- Auto increment value for auth_user_groups
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 4 WHERE name = 'auth_user_groups';

-- ----------------------------
-- Indexes structure for table auth_user_groups
-- ----------------------------
CREATE INDEX "auth_user_groups_group_id_97559544"
ON "auth_user_groups" (
  "group_id" ASC
);
CREATE INDEX "auth_user_groups_user_id_6a12ed8b"
ON "auth_user_groups" (
  "user_id" ASC
);
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq"
ON "auth_user_groups" (
  "user_id" ASC,
  "group_id" ASC
);

-- ----------------------------
-- Indexes structure for table auth_user_user_permissions
-- ----------------------------
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c"
ON "auth_user_user_permissions" (
  "permission_id" ASC
);
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b"
ON "auth_user_user_permissions" (
  "user_id" ASC
);
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq"
ON "auth_user_user_permissions" (
  "user_id" ASC,
  "permission_id" ASC
);

-- ----------------------------
-- Auto increment value for django_admin_log
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 14 WHERE name = 'django_admin_log';

-- ----------------------------
-- Indexes structure for table django_admin_log
-- ----------------------------
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb"
ON "django_admin_log" (
  "content_type_id" ASC
);
CREATE INDEX "django_admin_log_user_id_c564eba6"
ON "django_admin_log" (
  "user_id" ASC
);

-- ----------------------------
-- Auto increment value for django_content_type
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 12 WHERE name = 'django_content_type';

-- ----------------------------
-- Indexes structure for table django_content_type
-- ----------------------------
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq"
ON "django_content_type" (
  "app_label" ASC,
  "model" ASC
);

-- ----------------------------
-- Auto increment value for django_migrations
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 19 WHERE name = 'django_migrations';

-- ----------------------------
-- Indexes structure for table django_session
-- ----------------------------
CREATE INDEX "django_session_expire_date_a5c62663"
ON "django_session" (
  "expire_date" ASC
);

PRAGMA foreign_keys = true;
