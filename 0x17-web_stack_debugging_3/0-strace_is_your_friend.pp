# Ensure the replacement is made in the wp-settings.php file
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => replace('class-wp-locale.phpp', 'class-wp-locale.php'),
}

# Restart the Apache2 service
service { 'apache2':
  ensure    => 'running',
  enable    => true,
  provider  => 'service',
  subscribe => File['/var/www/html/wp-settings.php'],
}
