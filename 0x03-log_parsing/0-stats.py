#!/usr/bin/python3
import re
import sys
from collections import defaultdict, Counter
from signal import signal, SIGINT

# Define the input format as a regular expression
pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'

# Initialize the variables to store the statistics
total_size = 0
status_codes = defaultdict(int)

# Define a function to print the statistics
def print_stats():
    print("File size: {}".format(total_size))
    for code, count in sorted(Counter(status_codes).items()):
        print("{}: {}".format(code, count))

# Define a handler for the keyboard interruption
def handler(signum, frame):
    print_stats()
    sys.exit(0)

# Register the handler for the SIGINT signal
signal(SIGINT, handler)

# Read stdin line by line
for line in sys.stdin:
    # Match the line with the input format
    match = re.search(pattern, line)
    # If the line matches, extract the information
    if match:
        ip, date, status, size = match.groups()
        # Update the statistics
        total_size += int(size)
        status_codes[status] += 1
        # If 10 lines have been read, print the statistics and reset the counter
        if line_count == 10:
            print_stats()
            line_count = 0
    # If the line does not match, skip it
    else:
        continue
    