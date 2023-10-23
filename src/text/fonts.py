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

 fonts.py

class PDFFont:
    """Represents a font in a PDF document."""
    def __init__(self, name, embedded_data=None):
        self.name = name
        self.embedded_data = embedded_data

    def is_embedded(self):
        """Check if the font is embedded in the PDF."""
        return self.embedded_data is not None
