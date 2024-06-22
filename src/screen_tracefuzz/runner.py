import os
import re

import pexpect

from src.screen_tracefuzz.prompt import PasswordPrompt


def generate_random_input():
    return 'a' * 3200 + '\0\n\0' + 'b' * 5000
    # return 'prettysecure!!1)0))'


def make_input():
    with PasswordPrompt('fuzz') as child:

        try:
            child.expect("Password:")
        except pexpect.exceptions.EOF:
            print("Error on getting password prompt. Maybe the problem is with screen instances?")
            return
        child.sendline(generate_random_input())
        match_index = child.expect([re.compile(r".*\$"), "Password incorrect."])
        if match_index == 1:
            print("Incorrect pass attempt recorded")
            os.system("screen -XS fuzz quit")
            return
        child.sendline('exit')
        print("Correct pass, exiting...")
        child.expect(pexpect.EOF)


if __name__ == '__main__':
    make_input()
