#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

# Input comes from STDIN (sorted by key)
for line in sys.stdin:
    line = line.strip()
    # Parse the input from mapper.py (word <tab> 1)
    word, count = line.split('\t', 1)
    
    try:
        count = int(count)
    except ValueError:
        continue

    # Logic to aggregate counts for identical keys
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write final word count to STDOUT
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Output the last word
if current_word == word:
    print(f"{current_word}\t{current_count}")

