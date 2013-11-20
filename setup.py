#!/usr/bin/env python

# Copyright 2013 Deutsche Telekom AG
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
    long_desc = "".join(f.readlines())

setup(
    name="radosgw_rest_admin",
    version="0.1",
    packages=find_packages(),
    scripts=['radosgw_rest_admin.py'],
    package_data={
        '': ['README.md', 'LICENSE'],
    },
    install_requires=[
        'requests-aws',
    ],
    author="Marc Koderer",
    author_email="m.koderer@telekom.de",
    description="Radosgw admin tool using the radosgw admin rest interface",
    long_description=long_desc,
    license="Apache-2.0",
    keywords="ceph radosgw",
    url="https://github.com/mkoderer/radosgw-rest-admin",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache-2.0",
        "Programming Language :: Python",
    ],
)

