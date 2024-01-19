# Create the file with specified content, permissions, owner, and group
  file { '/tmp/school/school':
    ensure  => file,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
  }


# Include the class in the main node configuration
node 'example_node' {
  include create_school_file
}
