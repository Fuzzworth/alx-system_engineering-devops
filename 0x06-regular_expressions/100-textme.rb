#!/usr/bin/env ruby

if ARGV.length == 1
  sender, number, flags = ARGV[0].match(/^.*\[from:([a-z|A-Z]*)\]\s\[to:(\+\d*)\]\s\[flags:(.*)\]$/i).captures
  puts "#$sender,#$number,#$flags"
  exit
end
