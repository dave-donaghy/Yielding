import time

def my_collection():
    for i in range(1, 10000):
        time.sleep(1)
        yield i * i + 1
        
for result in my_collection():
    print('Got result {}'.format(result))
