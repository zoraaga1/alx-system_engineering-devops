#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method

pattern = /School/
input_string = ARGV[0]

matches = input_string.scan(pattern)

concatenated_result = matches.join

puts concatenated_result
