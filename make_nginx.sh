#!/bin/bash
# make install nginx
# 2019-07-04

Nginx_package=$1
Nginx_tar_dir=`echo ${Nginx_package%.tar*}`
Nginx_install_dir=/usr/local/nginx

echo $Nginx_package
echo $Nginx_tar_dir
echo $Nginx_install_dir

[ -f ${Nginx_package} ] || exit 10

if [ $UID -eq 0 ];then
   yum -y install make gcc gcc-c++ zlib zlib-devel openssl openssl-devel pcre pcre-devel
else
   echo -e "033[32mNeed to be executed by the root user\033[0m"
   exit 127
fi

id nginx &>/dev/null

if [ $? -eq 0 ];then
    useradd -M -s /sbin/nologin nginx &>/dev/null
fi

tar xf ${Nginx_package} 

cd ./${Nginx_tar_dir}/

./configure --prefix=${Nginx_install_dir}  \
--user=nginx  \
--group=nginx  \
--with-pcre \
--with-http_stub_status_module  \
--with-http_ssl_module  \
--with-http_gzip_static_module \
--without-http_memcached_module

make && make install

chown -R nginx:nginx ${Nginx_install_dir}

ln -s ${Nginx_install_dir}/sbin/nginx /usr/local/bin && source /etc/profile

cat > /usr/lib/systemd/system/nginx.service <<set
[Unit]
Description=nginx - high performance web server
Documentation=http://nginx.org/en/docs/
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=${Nginx_install_dir}/logs/nginx.pid
ExecStart=${Nginx_install_dir}/sbin/nginx -c ${Nginx_install_dir}/conf/nginx.conf
ExecReload=/bin/kill -s HUP \$MAINPID
ExecStop=/bin/kill -s TERM \$MAINPID

[Install]
WantedBy=multi-user.target
set

systemctl daemon-reload && systemctl start nginx

if [ $? -eq 0 ];then
    echo -e "\033[32mNginx installed successfully...\033[0m"
else
    echo -e "\033[31mNginx installed failed...\033[0m"
fi
