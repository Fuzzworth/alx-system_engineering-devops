#!/usr/bin/env ruby

if ARGV.length == 1
  puts ARGV[0].scan(/\d{10}/).join("")
  exit
end
