# Multiprocessing
여러 개의 프로세스를 동시에 실행하여 시스템 자원을 효과적으로 활용하는 기술\
각 프로세스는 독립된 메모리 공간을 사용하여 다른 프로세스와 격리된 상태에서 실행\
멀티프로세스를 통해 CPU 집약적인 작업을 병렬로 처리하여 성능을 향상시킬 수 있음

## `multiprocessing` Library in Python
멀티프로세스를 쉽게 구현할 수 있도록 다양한 도구와 클래스를 제공

### Process
독립적인 프로세스를 생성하고 관리하는 데 사용
```python
from multiprocessing import Process

def worker():
    print("Worker function")

if __name__ == '__main__':
    p = Process(target=worker)
    p.start()
    p.join()
```

### Pool
다른 매개변수의 동일한 작업을 여러 프로세스에 분배하는 데 사용
```python
from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == '__main__':
    with Pool(4) as p:
        results = p.map(square, [1, 2, 3, 4, 5])
    print(results)
```

### Queue
프로세스 간 통신을 한 FIFO 큐\
collections.Queue와 달리 멀티프로세스 간 통신이 가능
```python
from multiprocessing import Process, Queue

def worker(q):
    q.put('Hello from worker')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    p.join()
    print(q.get())  # 'Hello from worker'
```