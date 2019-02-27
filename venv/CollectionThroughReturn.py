import time

def my_collection():
    results = []
    for i in range(1, 10):
        time.sleep(1)
        results.append(i * i + 1)
        
    return results
        
for result in my_collection():
    print('Got result {}'.format(result))
