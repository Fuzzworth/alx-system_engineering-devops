# Step 1: Modify the wp-settings.php file
exec { 'modify-wp-settings':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin',
  onlyif  => "test -e /var/www/html/wp-settings.php",
  require => File['/var/www/html/wp-settings.php'], # Ensure this runs after the file is present.
}

# Step 2: Restart the Apache2 service using Upstart
exec { 'restart-apache':
  command     => 'initctl restart apache2',
  path        => '/sbin:/usr/sbin:/bin',
  refreshonly => true, # Only run this command when notified by another resource.
  subscribe   => Exec['modify-wp-settings'], # Subscribe to the previous step.
}
