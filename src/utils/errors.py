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

# errors.py

class PDFError(Exception):
    """Base error for all PDF related exceptions."""
    pass

class PDFParsingError(PDFError):
    """Raised when there's an issue parsing a PDF."""
    pass

class PDFValidationError(PDFError):
    """Raised when a PDF doesn't conform to expected standards."""
    pass
