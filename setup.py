from setuptools import setup, find_packages

setup(
    name="emotion-inference",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "gdown",
    ],
    entry_points={
        "console_scripts": [
            "inference=emotion_inference.cli:main",
        ],
    },
    author="Paula Candiles",
    description="CLI tool for Twitter emotion classification",
)
