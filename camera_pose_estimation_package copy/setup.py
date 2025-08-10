"""To easily install code samples."""
from setuptools import find_packages, setup

# with open("requirements.txt") as f:
#     required = f.read().splitlines()

setup(
    name="camera_pose_estimation",
    packages=find_packages(include=["camera_pose_estimation"]),
    author="Antoine",
    description="camera pose estimation package",
    # install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
