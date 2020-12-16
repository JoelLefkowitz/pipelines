from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=[],
        extras_require={
            "master": ["safe_environ", "hvac", "buildbot[bundle]"],
            "worker": ["safe_environ", "hvac", "names", "buildbot-worker"],
            "postgres": ["safe_environ", "hvac"],
            "vault": [],
            "dev": ["black", "autoflake", "isort", "mypy"],
        },
    )
