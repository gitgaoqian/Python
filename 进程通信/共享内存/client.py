#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
#读取之前设置的共享文件
import mmap
import contextlib
import time

while True:
    with open('test.dat', 'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)) as m:
            s = m.read(1024).replace('\x00', '')
            print (s)
    time.sleep(1)

