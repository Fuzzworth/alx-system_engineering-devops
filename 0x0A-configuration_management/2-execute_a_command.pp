# DOcs 
exec { 'pkill killmenow':
  path    => '/usr/bin/',
  command => 'pkill -x killmenow'
}
