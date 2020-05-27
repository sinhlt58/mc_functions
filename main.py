import argparse
import importlib
import inspect
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--render", action="store_true", help="Render")
    parser.add_argument("--scene", type=str, help="Secene name")
    parser.add_argument("--function", type=str, help="Function in the scene")

    args = parser.parse_args()

    if args.render:
        module_path = args.scene.replace("/", ".")
        module_path = module_path.replace(".py", "")
        print(f"module_path: {module_path}")
        m = importlib.import_module(module_path)

        if args.function:
            funcs_to_run = [args.function]
        else:  # Run all function
            funcs_to_run = [f[0] for f in inspect.getmembers(m, inspect.isfunction)]

        scene_name = module_path.split(".")[-1]
        datapacks_dir = "./datapacks/sinhblack/data"
        scene_dir = f"{datapacks_dir}/aniblock/functions/{scene_name}"
        Path(scene_dir).mkdir(parents=True, exist_ok=True)

        for f in funcs_to_run:
            getattr(m, f)(datapacks_dir, scene_dir)
            print(f"Run function {f}")
