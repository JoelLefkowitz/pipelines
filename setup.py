from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=[
            "buildbot[bundle]",
            "safe_environ",
            "simple_pipes",
        ],
        extras_require={"dev": ["black", "autoflake", "isort", "mypy"]},
    )
