# puppet script to set up os conf
file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton - nofile 65535\n",
}
