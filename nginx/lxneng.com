server {
        listen       80;
        server_name  lxneng.com *.lxneng.com;
        root /var/www/lxneng.com;
       }