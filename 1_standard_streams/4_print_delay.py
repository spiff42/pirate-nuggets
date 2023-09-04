#!/usr/bin/env python3
import time
for i in range(100):
  print("This is line", i, end='')
  time.sleep(0.1)
  if i % 10 == 9:
    print("hej");
