import os


def get_seeds():
    files_count = len(os.listdir('../seeds/'))
    fc = 1
    for file in os.listdir():
        print(f"working with file {fc} from {files_count}")
        fc += 1
        with open(os.path.join('../seeds/', file), 'r') as fd:
            lines = fd.readlines()
            lines_total = len(lines)
            lines_counter = 1
            for l in lines:
                print(f"working with str {lines_counter} of {lines_total}")
                yield l
                l += 1

