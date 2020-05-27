from aniblock.utils import *


def to_mc(out_file):
    commands = []

    first_pos = [28, 4, 27]
    second_pos = [63, 42, 62]

    cube_size = 9

    def get_num_parts(n, m):
        return n // m + int(n % m != 0)

    num_y_parts = get_num_parts(
        abs(second_pos[1] - first_pos[1]) + 1, cube_size)
    num_x_parts = get_num_parts(
        abs(second_pos[0] - first_pos[0]) + 1, cube_size)
    num_z_parts = get_num_parts(
        abs(second_pos[2] - first_pos[2]) + 1, cube_size)

    def get_lower_upper(i, size, min_l, max_u):
        lower = i * size + min_l
        upper = lower + size - 1
        if upper > max_u:
            upper = max_u
        return lower, upper

    count = 1
    for yi in reversed(range(0, num_y_parts)):
        lower_y, upper_y = get_lower_upper(yi, cube_size, first_pos[1], second_pos[1])
        for xi in range(0, num_x_parts):
            lower_x, upper_x = get_lower_upper(xi, cube_size, first_pos[0], second_pos[0])
            for zi in range(0, num_z_parts):
                lower_z, upper_z = get_lower_upper(zi, cube_size, first_pos[2], second_pos[2])

                sub_commands = [
                    f"setblock ~ 4 ~{-count} minecraft:chain_command_block",
                    f"data modify block ~ 4 ~{-count} Command set value \"summon minecraft:area_effect_cloud ~ ~ ~-1 {{Tags:[\\\"TickCounter\\\"],Age:-10}}\"",
                    f"setblock ~ 4 ~{-(count + 1)} minecraft:command_block",
                    f"data modify block ~ 4 ~{-(count + 1)} Command set value \"fill {lower_x} {lower_y} {lower_z} {upper_x} {upper_y} {upper_z} minecraft:air destroy\"",
                    f"setblock ~ 4 ~{-(count + 2)} minecraft:chain_command_block",
                    f"data modify block ~ 4 ~{-(count + 2)} Command set value \"kill @e[type=minecraft:item]\"",
                ]

                commands = commands + sub_commands

                count += 3

    total_cube = num_x_parts * num_y_parts * num_z_parts
    print(f"{total_cube} cubes, {total_cube * cube_size * cube_size * cube_size} blocks, {len(commands)} commands")

    write_commands(out_file, commands)


if __name__ == "__main__":
    to_mc("D:/games/Twitch/Minecraft/Instances/SinhBlack/saves/Data pack/datapacks/sinhblack/data/sinhblack/functions/reverse_destroy.mcfunction")
