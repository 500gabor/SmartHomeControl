from setuptools import setup, find_packages

setup(
    name="control_lights",
    version="1.0.0",
    description="A package to control and read inputs for a CAN device.",
    author="Gabor Szell",
    author_email="500gabor@gmail.com",
    url="https://github.com/yourusername/control_lights",  # Update with your repo
    packages=find_packages(),
    install_requires=[
        "pyserial",  # Add other dependencies if required
    ],
    entry_points={
        "console_scripts": [
            "control_lights=control_lights.control_lights:main",
            "read_inputs=control_lights.read_inputs:read_input_states",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
