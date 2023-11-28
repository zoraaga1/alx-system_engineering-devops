#!/usr/bin/env ruby
#  Ruby script that accepts one argument and pass it to a regular expression matching method.
# only strings with more than twice t and less than 5

matches = ARGV[0].scan(/t{2,5}n/)

# Check if the number of matches is within the desired range (2 to 4)
if (2..4).include?(matches.length)
  puts matches.join
end
