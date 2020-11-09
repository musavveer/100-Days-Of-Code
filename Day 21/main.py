import time
from jokes import jokes
from random import randint

while True:
    print(jokes[randint(0, len(jokes) - 1)])
    time.sleep(5)