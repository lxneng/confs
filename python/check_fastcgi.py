#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

def main():
	
    proc = os.popen("ps -e|grep php5-cgi", "r")
    out_inf = proc.read()
    if 'php5-cgi' not in out_inf:
        os.system("/usr/bin/spawn-fcgi -a 127.0.0.1 -p 9000 -C 4 -u www-data -g www-data -f /usr/bin/php5-cgi -P /var/run/fastcgi-php.pid")
        log_file = open('/root/python/check_fastcgi.log','a')
        log_file.write(time.asctime()+'\n')
        log_file.close()

if __name__ == '__main__':
    main()