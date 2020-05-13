import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="lichess-terminal",
    version="1.0",
    author="Casimir Rönnlöf",
    author_email="casimirr04@gmail.com",
    description="Play chess against other real players in your terminal using Lichess",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)