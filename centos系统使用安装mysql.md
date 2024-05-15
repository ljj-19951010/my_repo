1.下载mysql

```shell
[ljj@ls ~]$ sudo wget https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.29-1.el8.x86_64.rpm-bundle.tar
```

然后解压

```shell
# 切换位置
[ljj@ls ~]$ cd /usr/local
# 新建一个mysql文件夹，存储解压文件
[ljj@ls local]$ sudo mkdir mysql
# 将解压的文件保存到mysql目录中
[ljj@ls local]$ sudo tar -xvf mysql-8.0.29-1.el8.x86_64.rpm-bundle.tar -C mysql
```

2.安装依赖

```shell
# 查看解压的文件
[ljj@ls mysql]$ ls
# 安装包和对应的依赖
[ljj@ls mysql]$ sudo rpm -ivh mysql-community-common-8.0.29-1.el8.x86_64.rpm --nodeps --force
[ljj@ls mysql]$ sudo rpm -ivh mysql-community-libs-8.0.29-1.el8.x86_64.rpm --nodeps --force 
[ljj@ls mysql]$ sudo rpm -ivh mysql-community-client-8.0.29-1.el8.x86_64.rpm --nodeps --force 
[ljj@ls mysql]$ sudo rpm -ivh mysql-community-server-8.0.29-1.el8.x86_64.rpm --nodeps --force 
# 查看安装好的包
[ljj@ls mysql]$ rpm -qa | grep mysql
```

3.打开mysql和设置开机启动

```shell
# 初始化mysql
[ljj@ls mysql]$ sudo mysqld --initialize
# 设置mysql权限
[ljj@ls mysql]$ sudo chown mysql:mysql /var/lib/mysql -R
# 启动mysql服务
[ljj@ls mysql]$ sudo systemctl start mysqld.service
# 设置开机启动
[ljj@ls mysql]$ sudo systemctl enable mysqld
```

4.登录mysql

由于系统设置了默认密码，所以我们要先获取密码，然后改了密码才能登录

```shell
#  查看mysql的初始密码
[ljj@ls mysql]$ sudo cat /var/log/mysqld.log | grep password
# 用初始化密码登录
[ljj@ls ~]$ mysql -uroot -p
# 登录进去之后设置root用户的密码为root123
mysql> ALTER USER "root"@"localhost" IDENTIFIED WITH mysql_native_password BY "root123";
# 退出mysql ，然后可以用新修改的密码试试
mysql> exit
```



PS：使用finalshell远程连接centos系统的mysql

先设置数据库权限:

```shell
use mysql;		# 使用mysql数据库
select host,user from user;		# 查看数据库权限
update user set host='%' where user='root' and host='localhost';		# %表示任意ip都可以访问
flush privileges;		# 刷新数据库权限
```

设置完之后就可以用mysql可视化软件连接了(native)





参考 https://blog.csdn.net/mzl87/article/details/125872051即可