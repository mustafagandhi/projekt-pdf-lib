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

class PDFEncryptor:
    """Base class for PDF encryption."""

    def encrypt(self, data, key):
        """Encrypt data using the provided key."""
        raise NotImplementedError

    def decrypt(self, data, key):
        """Decrypt data using the provided key."""
        raise NotImplementedError

class PDFDecryptor:
    """Base class for PDF decryption."""

    def decrypt(self, data, key):
        """Decrypt data using the provided key."""
        raise NotImplementedError

# Constants related to encryption, e.g., key lengths, encryption modes, etc.
KEY_LENGTH = 128
