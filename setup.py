from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=[
            "buildbot_abstract",
            "buildbot[bundle]",
            "hvac",
            "names",
            "retry",
            "simple_pipes",
            "vault_wrapper",
        ],
        extras_require={
            "dev": ["black", "autoflake", "isort", "mypy"],
        },
    )
