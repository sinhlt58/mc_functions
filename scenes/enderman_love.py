from aniblock.cubes import *
from aniblock.utils import *


def render_enderman(datapack_dir: str, scene_dir: str):
    cubes = [
        AnimatedMovingCube(
            init_lower_right=[-12, 4, 84],
            init_upper_left=[-4, 16, 98],
            run_steps=7,
            tick_rate=10,
            out_file=f"{scene_dir}/move_child_sheep.mcfunction",
            is_stay=False,
            velocity=[0, 1, 0]
        ),
        ReversedDestroyCube(
            init_lower_right=[-12, 10, 84],
            init_upper_left=[-4, 22, 98],
            tick_rate=10,
            out_file=f"{scene_dir}/delete_child_sheep.mcfunction",
            first_delay_ticks=20,
            delete_y_size=4,
        ),
        ReversedDestroyCube(
            init_lower_right=[17, 31, 95],
            init_upper_left=[26, 38, 95],
            tick_rate=10,
            out_file=f"{scene_dir}/delete_sheep_heart.mcfunction",
            first_delay_ticks=20,
            delete_y_size=1,
        ),
        AnimatedMovingCube(
            init_lower_right=[0, 4, 88],
            init_upper_left=[26, 28, 100],
            run_steps=3,
            tick_rate=10,
            out_file=f"{scene_dir}/move_sheep_up.mcfunction",
            is_stay=False,
            velocity=[0, 1, 0]
        ),
        AnimatedMovingCube(
            init_lower_right=[0, 6, 88],
            init_upper_left=[26, 30, 100],
            run_steps=3,
            tick_rate=10,
            out_file=f"{scene_dir}/move_sheep_down.mcfunction",
            is_stay=False,
            velocity=[0, -1, 0]
        ),
        ReversedDestroyCube(
            init_lower_right=[34, 31, 95],
            init_upper_left=[43, 38, 95],
            tick_rate=10,
            out_file=f"{scene_dir}/delete_enderman_heart.mcfunction",
            first_delay_ticks=20,
            delete_y_size=1,
        ),
        AnimatedMovingCube(
            init_lower_right=[28, 4, 86],
            init_upper_left=[42, 27, 101],
            run_steps=15,
            tick_rate=20,
            out_file=f"{scene_dir}/move_enderman_backward.mcfunction",
            is_stay=False,
            velocity=[3, 0, 0]
        )
    ]

    do_render_cubes(cubes)


def render_creeper(datapack_dir: str, scene_dir: str):
    print(f"f2 {datapack_dir}, {scene_dir}")
