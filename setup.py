# SPDX-FileCopyrightText: 2024 Toki Makabe <s23c1130sm@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'mypkg'
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Toki Makabe',
    maintainer_email='s23c1130sm@s.chibakoudai.jp',
    description='mypkg',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'MousePointPub = mypkg.MousePointPub:main',
            'listener = mypkg.listener:main',
        ],
    },
)