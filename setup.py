from setuptools import setup

setup(
    name="gtransbot",
    version="0.0.1",
    packages=["gtransbot"],
    install_requires=[
        "google-cloud-translate==2.0.1",
        "discord.py==1.7.3",
    ],
    extras_require={"dev": ["black==22.1.0", "flake8==4.0.1", "build==0.7.0"]},
)
