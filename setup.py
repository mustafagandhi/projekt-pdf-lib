# Copyright 2023 Mustafa Gandhi & Ten98 Studios
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name="projekt-pdf-lib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add your library's dependencies here. For example:
        'pytest==7.4.2',
    ],
    author="Mustafa Gandhi",
    author_email="148590629+mustafagandhi@users.noreply.github.com",
    description="A Python based PDF manipulation library.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mustafagandhi/projekt-pdf-lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 with Commons Clause Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

