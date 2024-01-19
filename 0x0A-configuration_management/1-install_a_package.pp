# Define a class to manage the installation of Flask

package { 'flask':
    ensure => '2.1.0',
    provider => 'pip3',
  }
