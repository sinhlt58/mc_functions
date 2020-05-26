import numpy as np

from blocks import *
from utils import *
from constants import *


def move_cube(out_file):
    commands = []

    cube_start = np.array([1, 1, 1])
    cube_end = np.array([5, 5, 5])

    velocity = np.array([1, 0, 0])
    run_second = 5
    run_ticks = run_second * 20
    tick_rate = 10

    num_frames = run_ticks // tick_rate

    for i in range(0, num_frames):
        pos_begin_str = pos_to_str(cube_start, relative=POS_ABSOLUTE)
        pos_end_str = pos_to_str(cube_end, relative=POS_ABSOLUTE)
        des_pos = cube_start + velocity
        des_pos_str = pos_to_str(des_pos, relative=POS_ABSOLUTE)

        # Clone frame
        commands.append(
            CommandBlock(f"clone {pos_begin_str} {pos_end_str} {des_pos_str} replace move")
        )
        # Delay
        commands.extend([
            CommandBlockDelay(delay_ticks=tick_rate)
        ])

        cube_start = des_pos
        cube_end = cube_end + velocity

    write_commands(out_file, commands)


if __name__ == "__main__":
    move_cube("move_cube.mcfunction")
