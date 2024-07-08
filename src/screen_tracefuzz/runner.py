import os
import re

import pexpect

from screen_tracefuzz.input_generation.mutations import mutate_input_for_buffer
from screen_tracefuzz.input_generation.take_seeds import get_seeds
from screen_tracefuzz.prompt import PasswordPrompt


def generate_random_input():
    return 'a' * 3200 + '\0\n\0' + 'b' * 5000
    # return 'prettysecure!!1)0))'


def make_input(data: str):
    with PasswordPrompt('fuzz', data) as child:

        try:
            child.expect("Password:")
        except pexpect.exceptions.EOF:
            print("Error on getting password prompt. Maybe the problem is with screen instances?")
            return
        child.sendline(data)
        match_index = child.expect([re.compile(r".*\$"), "Password incorrect."])
        if match_index == 1:
            print("Incorrect pass attempt recorded")
            os.system("screen -XS fuzz quit")
            return
        child.sendline('exit')
        print("Correct pass, exiting...")
        child.expect(pexpect.EOF)


def fuzzing_process():
    for seed in get_seeds():
        try:
            i = seed.decode('utf-8')
        except UnicodeDecodeError:
            i = seed.decode('utf-16')
        for split in '\0', '\r\n', 'x00':
            fuzz_input = mutate_input_for_buffer(i, split)
            make_input(fuzz_input)


if __name__ == '__main__':
    fuzzing_process()
