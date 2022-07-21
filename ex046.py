# Counts down from 10

from time import sleep
print("Tempo até a queima de fogos: ")
for c in range(10, -1, -1):
    sleep(1)
    print(f"{c}!")
