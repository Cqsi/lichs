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
    url="https://github.com/Cqsi/lichess_terminal",
    packages=["lichess_terminal"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    install_requires=["python-chess", "berserk"],
    entry_points={
        "console_scripts": [
            "lichess=lichess_terminal.__main__:main",
        ]
    },
    
)