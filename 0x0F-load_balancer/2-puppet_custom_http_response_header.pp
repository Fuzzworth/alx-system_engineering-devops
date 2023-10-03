package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file_line { 'Creating header':
  	ensure => present,
  	path   => '/etc/nginx/sites-available/default',
  	line   => "\tadd_header X-Served-By ${hostname};",
  	after  => 'server_name _;',
	require => Service['nginx'],
}
