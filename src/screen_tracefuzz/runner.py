import os
import pty
import subprocess
import time


def trace_fuzzing():
    pid: int


def generate_random_input():
    return 'a' * 3200 + '\0\n\0' + 'b' * 5000


def make_input():
    os.system('screen -dm fuzz')
    master, slave = pty.openpty()
    process = subprocess.Popen('screen -r fuzz', stdin=slave, stdout=subprocess.PIPE, shell=True)
    time.sleep(0.5)
    with os.fdopen(master, 'w') as pin:
        pin.write(generate_random_input())
        pin.flush()
    print(process.communicate())
    os.close(master)
    os.close(slave)


if __name__ == '__main__':
    make_input()