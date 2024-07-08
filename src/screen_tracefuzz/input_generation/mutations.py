from screen_tracefuzz.consts import PASSWORD_BUF_SIZE


def mutate_input_for_buffer(seed: str, split: str):
    # one to go outside buffer, second to place there a split char
    seed_times = PASSWORD_BUF_SIZE // len(seed) + 2
    return split.join([seed] * seed_times)
