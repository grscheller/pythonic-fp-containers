# Copyright 2023-2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Three types of queues.

+------------------------------------+-----------+--------------------------+
| module                             | Class     | description              |
+====================================+===========+==========================+
| pythonic_fp.containers.queues.fifo | FIFOQueue | First-In-First-Out queue |
+------------------------------------+-----------+--------------------------+
| pythonic_fp.containers.queues.lifo | LIFOQueue | Last-In-First-Out queue  |
+------------------------------------+-----------+--------------------------+
| pythonic_fp.containers.queues.de   | DEQueue   | Double-Ended queue       |
+------------------------------------+-----------+--------------------------+

"""

__author__ = 'Geoffrey R. Scheller'
__copyright__ = 'Copyright (c) 2023-2025 Geoffrey R. Scheller'
__license__ = 'Apache License 2.0'
