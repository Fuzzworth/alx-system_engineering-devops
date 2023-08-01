#!/usr/bin/env ruby

if ARGV.length == 1
  sender, number, flags = ARGV[0].match(/^.*\[from:([a-z|A-Z]*)\].*\[to:(\+\d*)\].*\[flags:(.*)\]$/)
  puts "#$sender,#$number,#$flags"
  exit
end
