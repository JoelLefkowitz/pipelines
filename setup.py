from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=[
            "buildbot[bundle]",
            "hvac",
            "names",
            "retry",
            "requests",
            "simple_pipes",
            "buildbot_abstract>=0.3.12",
            "vault_wrapper>=0.3.4",
        ],
        extras_require={
            "tests": [
                "pytest-bdd",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-watch",
                "pytest",
                "tox",
            ],
            "tools": [
                "autoflake",
                "bandit",
                "black",
                "bump2version",
                "isort",
                "mypy",
                "pylint",
                "quickdocs",
                "twine",
                "wheel",
            ],
        },
    )
