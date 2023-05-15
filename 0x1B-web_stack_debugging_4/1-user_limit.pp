# Change the OS config to make it posible to login with the holberton user and open a file without any error message

exec {'change soft':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['change hard'],
}

exec {'change hard':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
