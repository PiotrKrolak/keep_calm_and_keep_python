import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0

    def start(self):
        self.start_time = time.time()
        return self.start_time

    def stop(self):
        self.stop_time = time.time()
        return self.stop_time

    def elapsed_time(self):
        return self.stop_time - self.start_time



class Zbior:
    def __init__(self):
        self.lista = []

    def sortowanie(self):
        pass

    def sortowanie_binarne(self):
        pass
        
    def sortowanie_all(self):
        pass

###### TESTS #####

#t1 = Timer()

#t1.start()

#for i in range(100):
#   print(i)

#t1.stop()

#x = t1.elapsed_time()
#print(f"Elapsed time: {x} seconds")
