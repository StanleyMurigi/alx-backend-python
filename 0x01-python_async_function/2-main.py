#!/usr/bin/env python3


import asyncio
measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 12

print(measure_time(n, max_delay))

