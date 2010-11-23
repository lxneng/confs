server {
     listen  80;
     server_name blog.lxneng.com;
     access_log /var/www/blog.lxneng.com/logs/access.log;
     error_log /var/www/blog.lxneng.com/logs/error.log;

     root /var/www/blog.lxneng.com;

     location / {
         index  index.php;
     }

     location ~ \.php$ {
         fastcgi_pass   127.0.0.1:9000;
         fastcgi_index  index.php;
         include /etc/nginx/fastcgi_params;
     }
}