import time
import threadpool


def say_hello(name):
    print("Hello ", name)
    time.sleep(1)


name_list = ['aa', 'bb', 'cc', 'dd', 'aa', 'bb', 'cc', 'dd']
start_time = time.time()
pool = threadpool.ThreadPool(4)
requests = threadpool.makeRequests(say_hello, name_list)
[pool.putRequest(req) for req in requests]
pool.wait()
print('%d second' % (time.time() - start_time))
