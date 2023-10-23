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

# xref.py

class CrossReferenceTable:
    """Handles the PDF's cross-reference table."""
    def __init__(self):
        self.entries = []

    def to_pdf(self) -> bytes:
        """Serialize the table to its PDF representation."""
        pass

    @staticmethod
    def from_pdf(data: bytes):
        """Deserialize the table from its PDF representation."""
        pass

class PDFTrailer:
    """Handles the PDF's trailer."""
    def to_pdf(self) -> bytes:
        """Serialize the trailer to its PDF representation."""
        pass

    @staticmethod
    def from_pdf(data: bytes):
        """Deserialize the trailer from its PDF representation."""
        pass
