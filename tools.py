import time

class Timer:
    def __init__(self, start = 0, stop = 0):
        self.start = start
        self.stop = stop

    def time(self):
        return self.start - self.stop
    

t1 = Timer()

#x = t1.time()

'''
y = time.time()

print(y)

z = time.time()

print(z)

a = z - y

print(a)

################################################

b = time.thread_time()

print(b)

################################################

'''
y = time.time_ns()

print(y)

z = time.time_ns()

print(z)

a = (z - y)

print(a)