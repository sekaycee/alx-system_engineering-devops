# Install an Nginx server and run a redirect

exec {'install':
  provider => shell,
  command  => 'apt-get -y update ; apt-get -y install nginx ; echo "Hello World!" | tee /var/www/html/index.nginx-debian.html ; sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/sekaycee permanent;/" /etc/nginx/sites-available/default ; service nginx start',
}
