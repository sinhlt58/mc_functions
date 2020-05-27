import numpy as np

from blocks import *
from utils import *
from constants import *
from blocks_writers import *


def move_cube(out_file):
    # First cube's position
    cube_start = np.array([1, 1, 1])
    cube_end = np.array([5, 5, 5])

    # Configs
    velocity = np.array([-1, 0, 0])
    run_second = 5
    run_ticks = run_second * 20
    tick_rate = 10

    # Number of frame will be displayed
    num_frames = run_ticks // tick_rate

    blocks = []
    for i in range(0, num_frames):
        pos_begin_str = pos_to_str(cube_start, relative=POS_ABSOLUTE)
        pos_end_str = pos_to_str(cube_end, relative=POS_ABSOLUTE)
        des_pos = cube_start + velocity
        des_pos_str = pos_to_str(des_pos, relative=POS_ABSOLUTE)

        # Clone frame, Delay
        blocks.extend([
            CommandBlock(f"clone {pos_begin_str} {pos_end_str} {des_pos_str} replace move"),
            CommandBlockDelay(delay_ticks=tick_rate)
        ])

        cube_start = des_pos
        cube_end = cube_end + velocity

    print(f"Num frames = {num_frames}")
    write_command_blocks(out_file, blocks)


if __name__ == "__main__":
    move_cube("move_cube.mcfunction")
