"""
Setup script for fake-review-detection package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="fake-review-detection",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Detection of fake online reviews using semi-supervised and supervised learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fake-review-detection",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pandas>=2.2.0",
        "numpy>=1.26.0",
        "scikit-learn>=1.4.0",
        "nltk>=3.8.1",
        "matplotlib>=3.8.0",
        "seaborn>=0.13.0",
        "tqdm>=4.66.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.12.0",
            "flake8>=7.0.0",
            "mypy>=1.7.0",
        ],
    },
)
