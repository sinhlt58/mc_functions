import numpy as np

from aniblock.constants import *


def pos_to_str(pos, relative=POS_RELATIVE_W):
    if relative == POS_RELATIVE_W:
        return f"~{pos[0]} ~{pos[1]} ~{pos[2]}"
    elif relative == POS_RELATIVE_S:
        return f"^{pos[0]} ^{pos[1]} ^{pos[2]}"
    elif relative == POS_ABSOLUTE:
        return f"{pos[0]} {pos[1]} {pos[2]}"
    else:
        raise Exception(f"Unknow relative {relative}")


def facing_to_vec(facing, np_array=True):
    if facing == EAST:
        res = [1, 0, 0]
    elif facing == WEST:
        res = [-1, 0, 0]
    elif facing == SOUTH:
        res = [0, 0, 1]
    elif facing == NORTH:
        res = [0, 0, -1]
    elif facing == UP:
        res = [0, 1, 0]
    elif facing == DOWN:
        res = [0, -1, 0]
    else:
        raise Exception(f"Unknow facing {facing}")

    if np_array:
        return np.array(res)

    return res


def write_commands(out_file, commands):
    with open(out_file, "w") as f:
        for c in commands:
            f.write(f"{c}\n")
    print(f"Write file {out_file}")
