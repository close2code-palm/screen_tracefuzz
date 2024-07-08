import os

from screen_tracefuzz.triggered import save_corpus


def trace_fuzzing(pid: int, fuzz_data: str):
    waited_status = os.waitpid(pid, 0)[1]
    if os.WIFEXITED(waited_status):
        es = os.WEXITSTATUS(waited_status)
        print(f'Exited with status {es}')
    if os.WIFSIGNALED(waited_status):
        signal_code = os.WTERMSIG(waited_status)
        print(f'Killed by signal {signal_code}')
        save_corpus(str(signal_code), fuzz_data)

