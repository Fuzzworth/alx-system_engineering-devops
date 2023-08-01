#!/usr/bin/env ruby

if ARGV.length == 1
  sender, number, flags = ARGV[0].match(/^.*\[from:\s([a-z|A-Z]*)\].*\[to:\s(\+\d*)\].*\[flags:\s(.*)\]$/)
  puts "#$sender,#$number,#$flags"
  exit
end
