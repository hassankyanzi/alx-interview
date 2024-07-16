#!/usr/bin/python3
"""
Log parsing
"""

import sys
import signal

# Constants
codes = {"200", "301", "400", "401", "403", "404", "405", "500"}

# Initialize variables
filesize = 0
count = 0
stats = {code: 0 for code in codes}

def print_stats(stats: dict, filesize: int) -> None:
    """
    Print statistics including total file size and status code counts.
    """
    print("File size: {:d}".format(filesize))
    for code in sorted(stats):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))

def signal_handler(sig, frame):
    """
    Signal handler for KeyboardInterrupt (Ctrl+C).
    """
    print_stats(stats, filesize)
    sys.exit(0)

# Register signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        count += 1
        data = line.split()
        
        # Ensure line has at least two elements (status code and file size)
        if len(data) < 2:
            continue
        
        # Extract status code and file size
        try:
            status_code = data[-2]
            if status_code in stats:
                stats[status_code] += 1
        except (IndexError, ValueError):
            continue
        
        # Extract file size and accumulate
        try:
            filesize += int(data[-1])
        except (IndexError, ValueError):
            continue
        
        # Print statistics every 10 lines
        if count % 10 == 0:
            print_stats(stats, filesize)

    # Print final statistics after all lines are processed
    print_stats(stats, filesize)

except KeyboardInterrupt:
    # Handle manual interruption (Ctrl+C)
    print_stats(stats, filesize)
    sys.exit(0)
