# Puppet script to add custom HTTP response header

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        add_header X-Served-By $hostname;
        # other configurations...
    }

    # other server configurations...
}
",
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
