'''
Author: Thoma411
Date: 2023-06-04 22:28:04
LastEditTime: 2023-06-09 17:20:32
Description: custom queue
'''


class FixedQueue:
    def __init__(self, length):
        self.queue = []
        self.length = length

    def add(self, item):
        self.queue.insert(0, item)
        if len(self.queue) > self.length:
            self.queue = self.queue[:-1]

    def get(self, index):
        if index >= len(self.queue):
            return None
        return self.queue[index]

    def __repr__(self):
        return str(self.queue)


if __name__ == '__main__':
    q = FixedQueue(3)
    q.add(1)
    print(q)  # [1]
    q.add(2)
    print(q)  # [2, 1]
    q.add(3)
    print(q)  # [3, 2, 1]
    q.add(4)
    print(q)  # [4, 3, 2]
    q.add('w')
    print(q)
    print(q.get(1))
