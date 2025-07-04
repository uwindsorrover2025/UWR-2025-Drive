from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'diff_drive_can'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mars Rover Team',
    maintainer_email='rover2025@mars.rover',
    description='ROS 2 package for differential drive control via CAN bus using PS4 controller',
    license='Apache-2.0',
    tests_require=['pytest'],
    scripts=['scripts/test_can_communication.py', 'scripts/debug_ps4_to_can.py'],
    entry_points={
        'console_scripts': [
            'ps4_twist_node = diff_drive_can.ps4_twist_node:main',
            'twist_to_can_node = diff_drive_can.twist_to_can_node:main',
        ],
    },
)