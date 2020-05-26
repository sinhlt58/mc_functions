from blocks import *
from constants import *
from utils import *


def write_command_blocks(blocks: CommandBlock):
    """
        Write a list set minecraft:command_block commands
        World relative to the executor's position
        facing north (-z), west (-x), up (+y) to stack the command blocks

        maximum size: 4 chunks (16*16*4*200 blocks)
    """
    max_z_size = 4 * 2  # 2 chunks
    max_x_size = 4 * 2  # 2 chunks
    max_y_size = 200

    #    -x(west)
    #    |                      ^->->->
    #    |                      |<-<-<-^
    #    |________ -z(north)    ->->->|

    for i, block in enumerate(blocks):
        z_col_idx = i % max_z_size
        x_col_idx = i // max_z_size
        y_col_idx = i // (max_z_size * max_x_size)

        is_y_even = y_col_idx % 2 == 0
        is_x_even = x_col_idx % 2 == 0

        # IMPORTANT: the order is important here
        # Normal case
        if is_x_even == is_y_even:
            facing = NORTH
        else:
            facing = SOUTH

        # Overwrite edge z=last case
        if z_col_idx == max_z_size - 1:
            if is_y_even and is_x_even:
                facing = WEST
            if not is_y_even and not is_x_even:
                facing = EAST

        # Overwirte edge z=0 case
        if z_col_idx == 0:
            if is_y_even and not is_x_even:
                facing = WEST
            if not is_y_even and is_x_even:
                facing = EAST


        # Overwrite for the first block in z-x plane case
        if z_col_idx == 0 and x_col_idx == 0 and not is_y_even:
            facing = UP

        is_end_plane = False
        # Overwrite for the last block in z-x plane case
        if z_col_idx == max_z_size - 1 and x_col_idx == max_x_size - 1 and is_y_even:
            facing = UP
            is_end_plane = True

        print(f"(x: {x_col_idx}, y: {y_col_idx}, z: {z_col_idx} - {facing}")
        if is_end_plane:
            print("----------------------------")


if __name__ == "__main__":
    write_command_blocks([CommandBlock("hello") for i in range(0, 1000)])
