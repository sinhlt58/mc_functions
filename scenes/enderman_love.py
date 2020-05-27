from aniblock.cubes import *


def enderman(datapack_dir: str, scene_dir: str):
    enderman_cube = AnimatedMovingCube(
        init_lower_right=[1, 1, 1],
        init_upper_left=[5, 5, 5],
        run_seconds=5,
        out_file=f"{scene_dir}/enderman.mcfunction",
        tick_rate=10,
        is_stay=False,
        velocity=[-1, 0, 0]
    )
    enderman_cube.render()


def creeper(datapack_dir: str, scene_dir: str):
    print(f"f2 {datapack_dir}, {scene_dir}")
