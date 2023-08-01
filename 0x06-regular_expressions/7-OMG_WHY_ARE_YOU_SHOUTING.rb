#!/usr/bin/env ruby

if ARGV.length == 1
  puts ARGV[0].scan(/[A-Z]/).join("")
  exit
end
