from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=[
            "buildbot",
            "buildbot-worker",
            "buildbot-www",
            "buildbot-waterfall-view",
            'buildbot-console-view',
            "buildbot-grid-view",
            "safe_environ",
            "simple_pipes",
        ]
    )
