# -*- coding: utf-8 -*-

import asyncio
import time

task_num = 100000

async def task(tid):
    r = await asyncio.sleep(2)
    if tid % 1000 == 0:
        print("task %d done" % tid)

start = time.time()
loop = asyncio.get_event_loop()
tasks = [task(i) for i in range(task_num)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end = time.time()
print("Time cost: %d" % (end - start))