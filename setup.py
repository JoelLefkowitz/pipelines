from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=[
            "buildbot[bundle]",
            "hvac",
            "names",
            "retry",
            "simple_pipes",
            "buildbot_abstract==0.3.6",
            "vault_wrapper==0.3.0",
        ],
        extras_require={
            "dev": ["black", "autoflake", "isort", "mypy"],
            "docs": [
                "sphinx",
                "pyimport",
                "pypandoc",
                "sphinxcontrib.apidoc",
                "sphinxcontrib.pandoc_markdown",
                "sphinx-autodoc-annotation",
                "yummy_sphinx_theme",
            ],
            "tests": [
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
                "pytest-watch",
            ],
        },
    )
