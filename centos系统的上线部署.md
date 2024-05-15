1.安装centos系统

2.创建管理员用户（可以参考这个链接 https://www.cnblogs.com/liujinjing521/p/10967990.html）

3.安装Nginx； 官网下载(http://nginx.org/en/download.html)

   先安装依赖,然后解压，解压之后  切换到解压后的文件夹目录中，执行编译和安装。

安装完成之后启动Nginx。

注意：如果中途报错很可能需要重新安装依赖。

```shell
sudo wget http://nginx.org/en/download.html
sudo yum -y install gcc gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel
sudo tar -zxvf nginx-1.22.0.tar.gz
sudo ./configure --prefix=/usr/local/nginx
sudo make
sudo make install
nginx sudo ./nginx
```

4.安装python

```shell
sudo yum -y install python3
```

5.安装虚拟环境

```shell
sudo pip3 install virtualenv -i https://mirrors.aliyun.com/pypi/simple
sudo pip3 install virtualenvwrapper -i https://mirrors.aliyun.com/pypi/simple
```

安装完成之后需要检查一下是否在家目录中有.envs或.virtualenv隐藏文件夹，没有的话自己创建；

然后配置bashrc文件

```shell
sudo vim ~/.bashrc
```

```bash
"""
export WORKON_HOME = ~/.envs
VIRTUALENVWRAPPER_PYTHON = /usr/bin/python3.6
source /usr/local/bin/virturalenvwrapper.sh
"""
```

6. 使用虚拟环境

   ```
   source ~/.bashrc		# 运行配置文件
   mkvirtualenv flask_envs			# 创建虚拟环境
   ./activate			# 运行虚拟环境
   workon flask_envs		# 切换虚拟环境
   flask_envs deactivate		# 退出虚拟环境
   rmvirtualenv		# 删除虚拟环境
   ```

   

7.安装MySQL

先从官网下载压缩包，在指定位置解压，然后一个一个包安装(其他方法百度)

```shell
sudo tar -xvf mysql-8.0.30-1.el8.x86_64.rpm-bundle.tar -C /usr/local/mysql

sudo rpm -ivh mysql-community-common-8.0.30-1.el8.x86_64.rpm --nodeps --force
sudo rpm -ivh mysql-community-libs-8.0.30-1.el8.x86_64.rpm --nodeps --force 
sudo rpm -ivh mysql-community-server-8.0.30-1.el8.x86_64.rpm --nodeps --force
sudo rpm -ivh mysql-community-client-8.0.30-1.el8.x86_64.rpm --nodeps --force
```

查看安装好的包

```shell
rpm -qa | grep mysql
```



8.使用MySQL并设置开机启动

```shell
# 初始化
sudo mysqld --initialize
# 设置mysql权限
sudo chown mysql:mysql /var/lib/mysql -R
# 启动mysql服务
sudo systemctl start mysqld.service
# 设置开机启动
sudo systemctl enable mysqld
```

一切设置好之后，登录MySQL并设置密码

首先查询系统的默认密码，然后登录mysql，进去之后将密码改成root123，退出mysql重新登录再试试

```shell
sudo cat /var/log/mysqld.log | grep password
mysql -uroot -p
ALTER USER "root"@"localhost" IDENTIFIED WITH mysql_native_password BY "root123";
exit;
```

9.设置远程连接mysql

```mysql
use mysql;
select host, user from user;
update user set host="%" where user="root" and host="localhost";
flush privileges;
```

10. 上线

```shell
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```

导入我们需要的模块，然后安装；

安装uwsgi

```
sudo yum install python36-devel
pip3 install uwsgi
```

安装完成之后配置uwsgi

```
mkdir log touch uwsgi.log
sudo vim uwsgi.ini
"""
[uwsgi]socket=127.0.0.1:7070
wsgi-file=app.py		# 执行文件的名字
callable=app		# 应用的名字
daemonize=/home/ljj/log/uwsgi.log		# 日志的路径
"""
uwsgi --ini uwsgi.ini

ps -ef | grep uwsgi		# 查看状态
```

配置Nginx文件

```
cp nginx.conf nginx.conf.bak		# 备份配置文件
sudo vim nginx.conf
"""
server{
	listen 80;		# 端口尽量不要与其他重复
	server_name 120.48.54.137;		#自己有域名的话，填自己的域名。没有就写当前电脑的ip
	location / {
		root /home/ljj/blog/;      # 站点根目录
		uwsgi_pass 127.0.0.1:7070		#与uwsgi的ip一致
		include uwsgi_params;
	}
	location /blog/static/{alias /home/ljj/blog/static/;}			#静态资源目录
}
"""
```



那么我们的上线配置完成了，访问试试看吧

```
python app.py runserver -h 0.0.0.0
```

-h表示设置host，0.0.0.0 表示使用本机的ip 所以我们访问时拿我自己的百度云服务器来说，直接复制云服务器的ip+运行成功提示的端口号 即可访问





























































































