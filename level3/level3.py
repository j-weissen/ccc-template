from pathlib import Path


def solve(beidl: str) -> str:
   return beidl


if __name__ == '__main__':
    workdir: Path = Path(__file__).resolve().parent
    for i in range(1, 6):
        infile = workdir.joinpath(Path(f"input{i}.txt"))
        outfile = workdir.joinpath(Path(f"out{i}.txt"))
        with open(infile) as f:
            beidl = f.read()
        out = solve(beidl)
        with open(outfile, "w+") as f:
            f.write(out)
