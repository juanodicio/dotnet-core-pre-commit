import sys
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser("dotnet pre-commit hooks")
    parser.add_argument(
        '--target',
        type=str,
        help="Solution or project path",
        default=""
    )

    return parser.parse_args()


def main():
    args = parse_args()
    cmd = "dotnet test " + args.target

    if sys.platform == 'win32':
        import subprocess

        if sys.version_info < (3, 7):
            raise SystemExit(subprocess.Popen(cmd).wait())
        else:
            raise SystemExit(subprocess.call(cmd))
    else:
        os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    main()
