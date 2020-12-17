from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=["hvac", "simple_pipes"],
        extras_require={
            "master": ["buildbot[bundle]"],
            "worker": ["names", "buildbot-worker"],
            "postgres": [],
            "vault": [],
            "dev": ["black", "autoflake", "isort", "mypy"],
        },
    )
