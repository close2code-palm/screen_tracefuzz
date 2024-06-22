import os
import re

import pexpect


def trace_fuzzing():
    pid: int


def generate_random_input():
    # return 'a' * 3200 + '\0\n\0' + 'b' * 5000
    return 'mysecretpass'


def make_input():
    os.system('screen -dm fuzz')
    child = pexpect.spawn("screen -r fuzz")
    child.expect("Password:")
    child.sendline(generate_random_input())
    match_index = child.expect([re.compile(r".*\$"), "Password incorrect."])
    if match_index == 1:
        os.system("screen -XS fuzz quit")
        # child.expect([re.compile(r".*\$")])
        child.close()
        return
    child.sendline('exit')
    child.expect(pexpect.EOF)
    child.close()


if __name__ == '__main__':
    make_input()
