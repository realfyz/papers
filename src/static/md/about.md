

## PAPERS文献管理与阅读工具

这里是Papers的官方页面。

本项目在[@fyz/papers](https://www.github.com/)开源，欢迎参与贡献。不定时进行issue review.

## Self-hosted

使用Git进行源码下载，运行如下命令

``` 
$ git clone https://github.com/fangyaozheng/papers
```

请预先安装Python3环境，并运行如下命令启动服务端

``` 
$ cd papers/
```

```
$ python3 main.py
```

Papers的Web服务将会运行在[http://0.0.0.0:80](http://0.0.0.0:80)或[http://127.0.0.1:80](http://127.0.0.1:80)

主要依赖：

``` 
$ pip3 install timeago
```

```
$ pip3 install flask
```

```
$ pip3 install Flask-Markdown
```

## 主要功能

### 基础类
  - 登陆
  - 注册
  - Sessions
  - 基于Sqlite3的持久化存储
  - Pdf Parser (开发中)
  - 验证码 (开发中)
  - 个人资料 (开发中)
### 核心类
  - 文献在线浏览
  - 文献添加
  - 文献资料修改（开发中）
  - 文献删除
### 其它
  - 关于
  - 电影资源
  - 关键字搜索（开发中）

## 设计

Papers基于B/S架构，提供轻量级部署和数据浏览。它的组件都是基于开源的框架或扩展。

### A. 前端

- Primer CSS @plung/primer

### B. 后端

#### 插件

- Flask @Flask
- Sqlite3
- Pdfplug
- Timeago @timeago
- Flask-Markdown [@flask-markdown](https://pythonhosted.org/Flask-Markdown/)

#### 数据库设计


## Bugs

- 文件名称不支持中文
- footer位置