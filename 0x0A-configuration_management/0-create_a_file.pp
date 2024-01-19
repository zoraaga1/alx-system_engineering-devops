# Create the file with specified content, permissions, owner, and group
  file { '/tmp/school/school':
    ensure  => file,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
  }
