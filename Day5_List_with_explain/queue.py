# to work with very laree list it is useful to use queues

from collections import deque
queue = deque([])
for i in range(100):

    queue.append(i)
print(queue)
queue.popleft()  # this method is only available in deque.
print(queue)
if not queue:   # if queue is empty then this will true
    print("queue is empty")
