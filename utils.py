
def write_commands(out_file, commands):
    with open(out_file, "w") as f:
        for c in commands:
            f.write(f"{c}\n")
    print(f"Write file {out_file}")
