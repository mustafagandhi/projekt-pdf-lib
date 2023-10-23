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

# base.py

class PDFObject:
    """Base class for all PDF objects."""
    def to_pdf(self) -> bytes:
        """Convert the object to its PDF representation."""
        raise NotImplementedError

    @staticmethod
    def from_pdf(data: bytes):
        """Create an object from its PDF representation."""
        raise NotImplementedError

class PDFIndirectObject(PDFObject):
    """Represents an indirect PDF object."""
    def __init__(self, obj_num, gen_num, value):
        self.obj_num = obj_num
        self.gen_num = gen_num
        self.value = value

    # Override to_pdf and from_pdf methods accordingly
