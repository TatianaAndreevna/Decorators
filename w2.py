import hashlib
from w1 import decorator


@decorator('C:\\Users\\Пользователь\\PycharmProjects\\Decorators\\')
def my_generators(path):
    with open(path) as f:
        for line in f:
            h = hashlib.md5(line.encode('utf-8'))
            yield h.hexdigest()


for item in my_generators('c_file.txt'):
    print(item)