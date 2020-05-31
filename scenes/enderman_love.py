from aniblock.cubes import *
from aniblock.utils import *


def render_enderman(datapack_dir: str, scene_dir: str):
    cubes = [
        # AnimatedMovingCube(
        #     init_lower_right=[1, 1, 1],
        #     init_upper_left=[40, 40, 40],
        #     run_steps=5,
        #     out_file=f"{scene_dir}/move_enderman.mcfunction",
        #     tick_rate=10,
        #     is_stay=False,
        #     velocity=[-1, 0, 0]
        # ),
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
            first_delay_ticks=40,
            delete_y_size=4,
        )
    ]

    do_render_cubes(cubes)


def render_creeper(datapack_dir: str, scene_dir: str):
    print(f"f2 {datapack_dir}, {scene_dir}")
