from aniblock.cubes import *
from aniblock.blocks_writers import *
from aniblock.animation import *


def render_drop(datapack_dir: str, scene_dir: str):
    count_cube = AnimatedMovingCube(
        init_lower_right=[10, 52, 70],
        init_upper_left=[14, 58, 70],
        run_steps=5,
        tick_rate=20,
        out_file=f"{scene_dir}/count.mcfunction",
        is_stay=True,
        velocity=[0, 0, 0],
        animation=Animation(
            init_lower_right=[25, 52, 37],
            init_upper_left=[29, 58, 37],
            num_frame=5,
            frame_space_x=1,
            max_x_frames=5,
        ),
        replace_diamond_block_with_air=True,
    )
    destroy_cube = ReversedDestroyCube(
        init_lower_right=[18, 59, 56],
        init_upper_left=[32, 61, 72],
        tick_rate=10,
        out_file=f"{scene_dir}/destroy.mcfunction",
        first_delay_ticks=20,
        delete_z_size=3,
    )

    do_render_cubes_together(
        [count_cube, destroy_cube],
        out_file=f"{scene_dir}/drop_villagers.mcfunction",
        delay_ticks=0,
        render_before=True,
        loop_pos=None,
    )
