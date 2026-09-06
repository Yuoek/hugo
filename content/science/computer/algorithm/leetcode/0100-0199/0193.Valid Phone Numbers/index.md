---
title: 0193 有效电话号码
date: 2026-09-06
---

## Solution

```bash
# Read from the file file.txt and output all valid phone numbers to stdout.
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt
```
