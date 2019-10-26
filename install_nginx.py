#!/usr/bin/env python3
# -*- enconding: utf-8 -*-


# import module

import os

import sys



# Judge the executive user

if os.getuid() != 0:

	print("Please use the root user to perform the installation...")

	sys.exit(1)



# Defined install dir and version

De_Ver = '1.16.1'

De_Dir = '/usr/local/nginx'

Cu_Ver = input("Please enter a version number,default is %s :"%(De_Ver))

Cu_Dir = input("Please enter the installation directory,default is \"%s\" :"%(De_Dir))

Ver = Cu_Ver or De_Ver

Dir = Cu_Dir or De_Dir



# download install source code package

# http://nginx.org/download/nginx-1.13.11.tar.gz

url = "http://nginx.org/download/nginx-%s.tar.gz"%(Ver)

cmd = 'wget ' + url

package = "nginx-%s.tar.gz"%(Ver)

if os.path.exists(package):

	os.remove(package)

if os.system(cmd) != 0:

	print("Download failed...")

	sys.exit(1)



# tar source code package

cmd = "tar xf nginx-%s.tar.gz"%(Ver)

if os.system(cmd) != 0:

	print("tar file failed...")

	sys.exit(1)




# Install dependency package

cmd = 'yum -y install zlib zlib-devel openssl openssl-devel pcre pcre-devel autoconf'

if os.system(cmd) != 0:

	print("install failed...")

	sys.exit(1)




# start make install nginx

cmd = 'cd nginx-%s && ./configure --prefix=%s --with-http_ssl_module'%(Ver,Dir)

if os.system(cmd) != 0:

	print("install failed...")

	sys.exit(1)

else:
	cmd = 'cd nginx-%s && make && make install'%(Ver)

	os.system(cmd)

	print("Installation successful...")




