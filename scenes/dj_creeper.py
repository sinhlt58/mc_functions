from aniblock.cubes import *
from aniblock.blocks_writers import *
from aniblock.animation import *


def render_creeper(datapack_dir: str, scene_dir: str):
    cube = AnimatedMovingCube(
        init_lower_right=[-19, 63, 242],
        init_upper_left=[0, 83, 242],
        run_steps=64,
        tick_rate=10,
        out_file=f"{scene_dir}/creeper.mcfunction",
        is_stay=True,
        velocity=[0, 0, 0],
        animation=Animation(
            init_lower_right=[-23, 88, 145],
            init_upper_left=[-4, 108, 145],
            num_frame=8,
            frame_space_x=4,
            frame_space_z=13,
            max_x_frames=4,
        ),
        replace_diamond_block_with_air=True,
    )

    cube.render()
