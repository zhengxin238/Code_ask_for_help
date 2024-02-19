from gurobipy import *


def dict_to_preflib_format(approval_data, directory, filename):
    full_path = os.path.join(directory, filename)
    with open(full_path, 'w') as f:
        for candidate, approval in approval_data.items():
            if approval == 1:
                f.write(candidate + '\n')
    return None


