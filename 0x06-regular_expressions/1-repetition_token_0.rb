#!/usr/bin/env ruby
#  Ruby script that accepts one argument and pass it to a regular expression matching method.
# only strings with more than twice t and less than 5

pattern = /t{3,4}/
input_string = ARGV[0]

matches = input_string.scan(pattern)

concatenated_result = matches.join
if (3..4).include?(matches.length)
    puts input_string
end