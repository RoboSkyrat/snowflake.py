import setuptools
import snowflake

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="snowflake.py",
    version=snowflake.__version__,
    author="Skyrat",
    author_email="pythonProjects@skyrat.dev",
    description="Simple Twitter snowflake-like id generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RoboSkyrat/snowflake.py",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
