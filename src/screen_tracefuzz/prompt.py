import os

import pexpect

from screen_tracefuzz.tracer import trace_fuzzing


class PasswordPrompt:

    def __init__(self, session_name: str, fuzz_data: str):
        self.fuzz_data = fuzz_data
        self.session_name = session_name
        self.prompt_process: pexpect.spawn | None = None

    def __enter__(self):
        os.system(f'screen -dm {self.session_name}')
        self.prompt_process = pexpect.spawn(f"screen -r {self.session_name}")
        return self.prompt_process

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.prompt_process is None:
            return
        trace_fuzzing(self.prompt_process.pid, fuzz_data=self.fuzz_data)
