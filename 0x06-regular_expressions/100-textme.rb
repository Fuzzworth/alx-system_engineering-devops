#!/usr/bin/env ruby

if ARGV.length == 1
  sender, number, flags = ARGV[0].match(/^.*\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\].*$/i).captures
  puts "#{sender},#{number},#{flags}"
  exit
end
