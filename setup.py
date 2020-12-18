from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=["hvac", "simple_pipes", "buildbot[bundle]", "names"],
        extras_require={
            "dev": ["black", "autoflake", "isort", "mypy"],
        },
    )
