---
title: 0192 统计词频
date: 2026-09-06
---

## Solution

```bash
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
```
