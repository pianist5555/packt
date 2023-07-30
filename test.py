from time import sleep

import psutil

while True:
    sleep(0.1)
    for process in psutil.process_iter():
        if process.name() in "python3.10.exe":
            print(
                process.name()
                + "\t"
                + str(process.pid)
                + "\t"
                + str(process.cpu_percent())
            )
