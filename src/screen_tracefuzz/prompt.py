import os

import pexpect


class PasswordPrompt:

    def __init__(self, session_name: str):
        self.session_name = session_name
        self.prompt_process: pexpect.spawn | None = None

    def __enter__(self):
        os.system(f'screen -dm {self.session_name}')
        self.prompt_process = pexpect.spawn(f"screen -r {self.session_name}")
        return self.prompt_process

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.prompt_process is None:
            return
        self.prompt_process.close()
