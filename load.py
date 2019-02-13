#!/usr/bin/env python

import uuid
n = 10
while True:
    x = []
    for i in range(n):
        x.append(uuid.uuid4())
    for a in x:
        print a
        x.remove(a)



