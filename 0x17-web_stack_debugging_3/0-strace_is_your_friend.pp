# Step 1: Ensure the replacement is made in the wp-settings.php file
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub("class-wp-locale.phpp", "class-wp-locale.php") %>'),
}

# Step 2: Restart the Apache2 service using Upstart
exec { 'restart-apache':
  command     => 'initctl restart apache2',
  path        => '/sbin:/usr/sbin:/bin',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
