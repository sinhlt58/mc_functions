from aniblock.blocks import *
from aniblock.constants import *
from aniblock.utils import *


def write_command_blocks(out_file, blocks: CommandBlock):
    """
        Write a list set minecraft:command_block commands
        World relative to the executor's position
        facing north (-z), west (-x), up (+y) to stack the command blocks

        maximum size: 4 chunks (16*16*4*200 blocks)
    """
    f = open(out_file, "w")

    max_z_size = 16 * 2  # 2 chunks
    max_x_size = 16 * 2  # 2 chunks
    max_y_size = 200

    #    -x(west)
    #    |                      ^->->->
    #    |                      |<-<-<-^
    #    |________ -z(north)    ->->->|

    commands_count = 0

    plane_size = max_z_size * max_x_size
    for i, block in enumerate(blocks):
        z_col_idx = (i % plane_size) % max_z_size
        x_col_idx = (i % plane_size) // max_z_size
        y_col_idx = i // plane_size

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

        print(f"(x: {-x_col_idx}, y: {y_col_idx}, z: {-z_col_idx} - {facing}")
        if is_end_plane:
            print("----------------------------")

        # Write to file
        # We negative x and z to write in west and north in Minecraft
        commands = block.to_mc_commands([-x_col_idx, y_col_idx, -z_col_idx-1], facing, POS_RELATIVE_W)
        for c in commands:
            f.write(f"{c}\n")
        commands_count += len(commands)

    f.close()
    print(f"Write {len(blocks)} blocks, {commands_count} commands to file {out_file}")


if __name__ == "__main__":
    write_command_blocks(
        "test_block_writers.mcfunction",
        [CommandBlock("hello") if i % 2 == 0 else CommandBlockDelay(30) for i in range(0, 1000)]
    )
