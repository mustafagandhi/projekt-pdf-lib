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

# data_structures.py

class PDFObject:
    """Base class for all PDF objects."""
    def __init__(self, object_id, generation_number):
        self.id = object_id
        self.gen = generation_number

class PDFDictionary:
    """Represents a PDF dictionary object."""
    def __init__(self):
        self.entries = {}

    def get(self, key, default=None):
        return self.entries.get(key, default)

    def set(self, key, value):
        self.entries[key] = value
