# Ensure the replacement is made in the wp-settings.php file
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => replace('class-wp-locale.phpp', 'class-wp-locale.php'),
}

# Restart the Apache2 service
service { 'apache2':
  ensure    => 'running',
  enable    => true,
  provider  => 'systemd', # Use the appropriate provider for your system.
  subscribe => File['/var/www/html/wp-settings.php'], # Ensure the service restarts when the file changes.
}
