from utils import *


def to_mc(out_file):
    commands = []

    root_x = 0
    root_y = 0
    root_z = 0

    width_x = 36
    width_z = 36
    height_y = 45

    cube_size = 9




    write_commands(out_file, commands)


if __name__ == "__main__":
    to_mc("reverse_destroy.mcfunction")
