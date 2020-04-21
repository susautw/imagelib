from pathlib import Path

from setuptools import setup, find_packages

requires = []
requirement_file = Path('./requirement.txt')
assert requirement_file.is_file()
with requirement_file.open() as fp:
    for line in fp.readlines():
        stripped = line.strip()
        requires.append(stripped)

print('found requirements: ')
print(*requires, sep=' ', end='\n')

setup(
    name="imagelib",
    version='0.3.0',
    author='Rin,Su',
    license='MIT',
    packages=find_packages(), install_requires=requires
)
