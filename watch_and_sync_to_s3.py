import inotify.adapters
import subprocess
import errno
import os
from pathlib import Path
import typer


def _main(
        source: Path = typer.Argument(..., help="The local path to watch and sync"),
        bucket: str = typer.Argument(..., help="The s3 bucket where to sync up")
):
    """Watch SOURCE for IN_CLOSE_WRITE events and sync to a s3 bucket when triggered."""

    if not source.is_dir():
        raise NotADirectoryError(
            errno.ENOENT, os.strerror(errno.ENOENT), source
        )

    i = inotify.adapters.InotifyTree(f"{source}")

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        if ('IN_CLOSE_WRITE' in type_names) or ('IN_MOVED_TO' in type_names):
            subprocess.run([
                "aws", "s3", "sync", f"{source}", f"{bucket}"
            ])


if __name__ == '__main__':
    typer.run(_main)
