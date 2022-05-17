import os


def abs_path_from_rel_path(rel_path: str) -> str:
    """Return an absolute file path given a relative filepath"""
    return os.path.join(os.path.dirname(__file__), rel_path)
