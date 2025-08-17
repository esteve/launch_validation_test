from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'launch_validation_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Esteve Fernandez',
    maintainer_email='esteve.fernandez@tier4.jp',
    description='Test case for launch description validation',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'launch_validation_node = launch_validation_publisher.launch_validation_node:main'
        ],
    },
)
