from aniblock.cubes import *


def render_enderman(datapack_dir: str, scene_dir: str):
    enderman_cube = AnimatedMovingCube(
        init_lower_right=[1, 1, 1],
        init_upper_left=[40, 40, 40],
        run_seconds=50,
        out_file=f"{scene_dir}/enderman.mcfunction",
        tick_rate=10,
        is_stay=False,
        velocity=[-1, 0, 0]
    )
    enderman_cube.render()


def render_creeper(datapack_dir: str, scene_dir: str):
    print(f"f2 {datapack_dir}, {scene_dir}")
