#!/usr/bin/env ruby

def extract_info(log_entry)
  sender = log_entry.scan(/\[from:([^\]]+)\]/).flatten.first
  receiver = log_entry.scan(/\[to:([^\]]+)\]/).flatten.first
  flags = log_entry.scan(/\[flags:([^\]]+)\]/).flatten.first

  "#{sender},#{receiver},#{flags}"
end

if ARGV.length == 1
  log_entry = ARGV[0]
  result = extract_info(log_entry)
  puts result
else
  puts "Usage: #{$PROGRAM_NAME} 'log_entry'"
end

