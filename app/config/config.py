from pathlib import Path


class ProjectDirs:
    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]

    @classmethod
    def get_dir(cls, name: str) -> Path:
        return getattr(cls, name.upper())
