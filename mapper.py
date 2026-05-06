#!/usr/bin/env python3
import sys

# Input comes from STDIN
for line in sys.stdin:
    # Remove whitespace and split line into words
    words = line.strip().split()
    for word in words:
        # Write results to STDOUT (word followed by a count of 1)
        # Hadoop will sort these by key (word) before the Reducer step
        print(f"{word}\t1")

