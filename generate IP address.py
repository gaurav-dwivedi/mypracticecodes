import random

for x in range(1000):
    ip = "192.168."
    ip += '.'.join(map(str, (random.randint(0, 255) for _ in range(2))))
    print(ip)
