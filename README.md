# 智慧公交管理系统

基于 Django 与 MySQL 实现的智慧交通管理系统，支持用户管理、车辆管理、线路管理、站点管理以及公交排班信息管理等功能。

## 介绍

本项目为数据库系统课程设计项目，围绕“智慧城市交通管理”场景进行设计与实现。系统采用 Django 作为后端框架，MySQL 作为关系型数据库，通过 Web 页面实现对交通系统核心数据的统一管理与查询。

项目重点包括：

* 数据库 E-R 模型设计
* 关系模式设计与第三范式规范化
* 数据索引优化
* Django ORM 数据管理
* 权限控制与角色管理
* 公交排班与线路管理

## 特点

### 用户管理模块

* 用户注册与登录
* 管理员登录
* 用户权限控制
* 用户状态管理

### 信息管理模块

* 员工信息管理
* 管理员信息管理
* 用户信息增删改查
* 角色权限分配

### 数据管理模块

* 车辆信息管理
* 公交线路管理
* 站点信息管理
* 排班信息管理

### 查询模块

* 线路查询
* 站点查询
* 车辆状态查询
* 角色与权限关系查看
* 线路与站点关系查看

## 数据库设计

系统主要实体包括：

```text
User
Vehicle
Station
Route
Info
Manager
```

数据库设计遵循第三范式（3NF），并通过主键、外键及联合索引优化系统查询性能。

项目中实现了：

* E-R 图设计
* 关系模型转换
* 主外键约束
* 联合索引优化
* 数据规范化设计

## 技术栈

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

### Backend

* Django
* Django ORM

### Database

* MySQL

## 项目组成结构

```text
├── Mysite/               # Django project configuration
├── Shujuku/              # database application modules
├── Static/               # static resources
├── Templates/            # HTML templates
├── manage.py             # project entry
├── docs/                 # experiment reports and ER diagrams
└── README.md
```

## 核心功能

系统实现了完整的交通信息管理流程，包括：

* 用户登录与权限验证
* 员工与管理员管理
* 公交车辆管理
* 线路与站点管理
* 排班冲突处理
* 数据关系展示

管理员能够对系统数据进行统一维护，而普通用户仅具备查询权限，以保证系统数据的安全性与一致性。

## 开发环境

* Windows 11
* Python
* Django
* MySQL
* Visual Studio Code
