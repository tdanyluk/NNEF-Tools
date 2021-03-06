# Copyright (c) 2017 The Khronos Group Inc.
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

from __future__ import division, print_function
from ..common.types import *
from ..common import dog


class TensorFlowDN(dog.DataNode):
    pass


class TensorFlowGraph(dog.Graph):
    pass


class TensorFlowOp(dog.OperationNode):
    pass


tensorflow_factory = dog.Factory(TensorFlowGraph, TensorFlowDN, TensorFlowOp)

if has_typing:
    TensorFlowDNLike = Union[TensorFlowDN, bool, int, float]
else:
    TensorFlowDNLike = object
