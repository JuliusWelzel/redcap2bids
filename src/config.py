from pathlib import Path

def define_dir(root, *names):
    """Creates a directory and ensures it exists."""
    path = root
    for name in names:
        path = path / name  # use pathlib's '/' operator to join paths
    path.mkdir(parents=True, exist_ok=True)
    return path

# Get the current directory where the script is executed
dir_proj = Path.cwd().parent
