from setuptools import setup, find_packages

setup(
    name="SmartHomeControl",
    version="1.2",
    description="A package to control and read inputs for a CAN device.",
    author="Gabor Szell",
    author_email="500gabor@gmail.com",
    url="https://github.com/500gabor/control_lights",
    packages=find_packages(),
    install_requires=[
        "setuptools==75.5.0",
        "pyserial==3.5",
        "matplotlib==3.9.2"
    ],
    entry_points={
        "console_scripts": [
            "control_devices=smart_home_control.control_devices:main",
            "read_data=smart_home_control.read_data:read_input_states",
            "visualize_floorplan=smart_home_control.visualize_floorplan:visualize_floorplan",

        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
