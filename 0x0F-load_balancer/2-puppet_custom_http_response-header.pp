# Install and configure an Nginx server with custom HTTP header

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install nginx']
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header']
}

exec { 'add_header':
  provider    => shell,
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf',
  before   => Exec['restart nginx']
}

exec { 'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart'
}
