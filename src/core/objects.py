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

# objects.py

class PDFDictionary(PDFObject):
    """Represents a PDF dictionary."""
    def __init__(self):
        self.items = {}

    # Override to_pdf and from_pdf methods

class PDFArray(PDFObject):
    """Represents a PDF array."""
    def __init__(self):
        self.items = []

    # Override to_pdf and from_pdf methods

class PDFString(PDFObject):
    """Represents a PDF string."""
    def __init__(self, value=""):
        self.value = value

    # Override to_pdf and from_pdf methods

class PDFNumber(PDFObject):
    """Represents a PDF number."""
    def __init__(self, value=0):
        self.value = value

    # Override to_pdf and from_pdf methods
