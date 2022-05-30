import inotify.adapters
import subprocess
import errno
import os
from pathlib import Path


def _main():
    source = Path("multirun")
    if not source.is_dir():
        raise NotADirectoryError(
            errno.ENOENT, os.strerror(errno.ENOENT), source
        )

    i = inotify.adapters.InotifyTree(f"{source}")

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        if 'IN_CLOSE_WRITE' in type_names:
            # subprocess.run(["rsync", "-r", "/workspace/source/", "/workspace/target"])
            subprocess.run([
                "aws", "s3", "sync", f"{source}", "s3://innova-conicet-output"
            ])


if __name__ == '__main__':
    _main()
