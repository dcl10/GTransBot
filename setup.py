from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="gtransbot",
    version="0.1.0",
    description="A Discord bot which helps making conversation between people who speak different languages simpler.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    packages=["gtransbot"],
    install_requires=[
        "google-cloud-translate==2.0.1",
        "discord.py==1.7.3",
        "python-dotenv==0.19.2",
    ],
    extras_require={
        "dev": [
            "black==22.1.0",
            "flake8==4.0.1",
            "build==0.7.0",
        ]
    },
    entry_points={
        "console_scripts": ["gtransbot=gtransbot.main:main"],
    },
)
