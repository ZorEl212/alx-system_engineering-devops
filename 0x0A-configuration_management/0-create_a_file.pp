#create a file called school with some attributes
#and a text content
file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744' ,
}
