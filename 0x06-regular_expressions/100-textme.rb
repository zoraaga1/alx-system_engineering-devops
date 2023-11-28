#!/usr/bin/env ruby

# Ruby script that extracts information from log entries and formats it.
# Outputs: SENDER,RECEIVER,FLAGS

log_entry = ARGV[0]

# Extract sender, receiver, and flags from the log entry
sender = log_entry.match(/\[from:(.+?)\]/)&.captures&.first
receiver = log_entry.match(/\[to:(.+?)\]/)&.captures&.first
flags = log_entry.match(/\[flags:(.+?)\]/)&.captures&.first

# Format and output the result
puts "#{sender},#{receiver},#{flags}"
