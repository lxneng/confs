server{
         listen 80;
         server_name xstock.lxneng.com;
         location / {
             include fastcgi_params;
             fastcgi_param SCRIPT_FILENAME "";
             fastcgi_param PATH_INFO $fastcgi_script_name;
             fastcgi_pass unix:/tmp/flask_test_app.sock;
                 }

         }