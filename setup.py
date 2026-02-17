from setuptools import setup, find_packages

setup(
    name="Topsis-Dixant-102316022",
    version="1.0.0",
    author="Dixant",
    description="TOPSIS implementation in Python",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
)
