from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fluxi",
    version="0.2.0",
    description="A library for FLUX ControlNet inpainting models based on https://github.com/alimama-creative/FLUX-Controlnet-Inpainting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/flux-controlnet",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "diffusers==0.30.2",
        "transformers",
        "numpy",
    ],
)