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

# metadata.py

class PDFHeader:
    """Handles the PDF's header."""
    def __init__(self, version="1.7"):
        self.version = version

    def to_pdf(self) -> bytes:
        return f"%PDF-{self.version}".encode()

class PDFMetadata(PDFDictionary):
    """Represents the PDF's metadata."""