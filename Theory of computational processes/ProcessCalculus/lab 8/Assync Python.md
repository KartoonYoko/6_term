#### Как передать данные в функцию потока



Стандартная библиотека Python предоставляет библиотеку threading, которая содержит необходимые классы для работы с потоками. Основной класс в этой библиотеки **Thread**.

Чтобы запустить отдельный поток, нужно создать экземпляр потока **Thread** и затем запустить его с помощью метода **.start()**:

```python
import logging
import threading
import time
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
```



Когда вы создаете поток **Thread**, вы передаете ему функцию и список, содержащий аргументы этой функции. В нашем примере мы говорим **Thread**, чтобы он запустил функцию **thread_function()** и передаем ему 1 в качестве аргумента.

Чтобы **указать одному потоку дождаться завершения другого потока**, вам нужно вызывать **.join()**.



#### Как получить данные из функции потока?

модуль `multiprocessing` имеет хороший интерфейс для этого, используя класс `Pool` . И если вы хотите придерживаться потоков, а не процессов, вы можете просто использовать класс `multiprocessing.pool.ThreadPool` в качестве замены.

```python
def foo(bar, baz):
  print 'hello {0}'.format(bar)
  return 'foo' + baz

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo

# do some other stuff in the main process

return_val = async_result.get()  # get the return value from your function.
```



#### Пример: использование класса для организации вычислений в потоке

```python
import threading
import time


class JustClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.value = 0

    def run(self):
        while True:
            print("here")
            time.sleep(2)


if __name__ == "__main__":
    f = JustClass()
    f.start()
    while True:
        print("asdd")
        time.sleep(2)
```

Источники: 

https://webdevblog.ru/vvedenie-v-potoki-v-python/

https://coderoad.ru/6893968/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B0%D0%B5%D0%BC%D0%BE%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8%D0%B7-%D0%BF%D0%BE%D1%82%D0%BE%D0%BA%D0%B0-%D0%B2-python