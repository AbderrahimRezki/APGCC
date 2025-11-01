from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()


def parse_requirements(fname="requirements.txt"):
    reqs = []
    with open(
        os.path.join(os.path.dirname(__file__), fname), "r", encoding="utf-8"
    ) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            reqs.append(line)
    return reqs


setup(
    name="apgcc",
    version="0.1.0",
    author="I-Hsiang Chen & others",
    author_email="your_email@example.com",
    description="Improving point-based crowd counting and localization via Auxiliary Point Guidance (APGCC)",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/AaronCIH/APGCC",
    license="MIT",
    packages=find_packages(exclude=["tests", "figures"]),
    install_requires=parse_requirements(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Computer Vision",
    ],
    include_package_data=True,
    entry_points={},
)
