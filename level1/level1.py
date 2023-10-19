from pathlib import Path


def solve(beidl: str):
    return str(beidl.count("A"))


def main():
    workdir: Path = Path(__file__).resolve().parent
    for i in range(1, 6):
        infile = workdir.joinpath(Path(f"input{i}.txt"))
        outfile = workdir.joinpath(Path(f"out{i}.txt"))
        with open(infile) as f:
            beidl = f.read()
        out = solve(beidl)
        with open(outfile, "w+") as f:
            f.write(out)


if __name__ == '__main__':
    main()
