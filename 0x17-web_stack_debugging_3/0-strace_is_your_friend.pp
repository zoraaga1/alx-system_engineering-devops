# puppet scipt that automat fixing 500 error

file { '/path/to/file':
  ensure  => 'file',
  owner   => 'apache',
  group   => 'apache',
  mode    => '0644',
}
