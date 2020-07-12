import time
class Secundomer:
    def __init__(self,iters):
        self.iters = iters

    def __call__(self,f):
        def wrapper(*args, **kwargs):
            avg_time = 0
            for i in range(self.iters) :
                t0 = time.time()
                return_value = f(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.iters
            print("Выполнение заняло %.5f секунд" % avg_time)
            return return_value
        return wrapper

    def __enter__(self):
        self.t0 = time.time
        return self.t0

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t1 = time.time

print("Пожалуиста, введите количество циклов для расчета скорости")
a=int(input())
@Secundomer(iters=a)
def Hrono():
     for i in range(1,1000000):
         pass
Hrono()


