#!/usr/bin/env ruby
#  Ruby script that accepts one argument and pass it to a regular expression matching method.
# only strings with more than twice t and less than 5

puts ARGV[0].scan(/hbt{2,5}n/).join
