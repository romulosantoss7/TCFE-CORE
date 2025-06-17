from setuptools import setup, find_packages
import os

setup(
    name="tcfe_core",
    version="1.0.0",
    author="Rômulo Santos de Carvalho",
    author_email="romuloportila2@gmail.com",
    description="Núcleo computacional para a Teoria do Campo de Força Universal (TCFE).",
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type="text/markdown",
    url="https://github.com/SeuUsuario/tcfe-core",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "matplotlib",
        "numpy",
        "qiskit"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics"
    ],
    python_requires='>=3.6',
)