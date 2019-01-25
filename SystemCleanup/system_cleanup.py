# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import time

path = "C:/Users/uspolgupta/AppData/Local/Google/Chrome/user data/default"
number_of_days = 30

time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)

files = []
size = 0
for file_ in os.scandir(path):
  if file_.is_file():
    stat = file_.stat(follow_symlinks=False)
    if stat.st_mtime <= time_in_secs:
        if file_.name[-4:].lower() == '.tmp':
          if len(file_.name) == 40:
            files.append(file_)
            size += (stat.st_size/(1024**3))

for file_ in files:
  os.remove(file_.path)
