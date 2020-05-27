import argparse
import importlib
import inspect
from pathlib import Path
from distutils.dir_util import copy_tree


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--render", action="store_true", help="Render")
    parser.add_argument("--scene", type=str, help="Secene name")
    parser.add_argument("--function", type=str, help="Function in the scene")
    parser.add_argument("--world", type=str, help="Path to the world folder")
    parser.add_argument("--sync", action="store_true", help="Sync to the world folder")

    args = parser.parse_args()

    if args.render:
        module_path = args.scene.replace("./", "")
        module_path = module_path.replace("/", ".")
        module_path = module_path.replace(".py", "")
        print(f"module_path: {module_path}")
        m = importlib.import_module(module_path)

        if args.function:
            funcs_to_run = [args.function]
        else:  # Run all functions
            funcs_to_run = [f[0] for f in inspect.getmembers(m, inspect.isfunction) if f[0].startswith("render_")]

        scene_name = module_path.split(".")[-1]
        datapacks_dir = "./datapacks/sinhblack/data"
        scene_dir = f"{datapacks_dir}/aniblock/functions/{scene_name}"
        Path(scene_dir).mkdir(parents=True, exist_ok=True)

        print(funcs_to_run)
        for f in funcs_to_run:
            getattr(m, f)(datapacks_dir, scene_dir)
            print(f"Run function {f}")

        args.sync = True

    if args.sync and args.world:
        copy_tree(src="./datapacks", dst=f"{args.world}/datapacks")
        print(f"Synced folder {args.world}")
