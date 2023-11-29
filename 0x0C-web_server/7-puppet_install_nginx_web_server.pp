# Install nginx with puppet
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

file { 'Hello World':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World',
}

augeas { 'nginx-rewrite':
  context => '/files/etc/nginx/sites-available/default',
  changes => [
    'set server_name/_[last()+1] redirect_me',
    'set server_name/_[last()]/rewrite ^/redirect_me https://www.google.com 301',
  ],
  onlyif  => 'match server_name/_[last()] size == 0',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
}
