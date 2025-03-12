# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from . import research, utils
from .autograd._functions import (
    MatmulLtState,
    bmm_cublas,
    matmul,
    matmul_4bit,
    matmul_cublas,
    mm_cublas,
)
from .nn import modules
from .optim import adam

__pdoc__ = {
    "libbitsandbytes": False,
    "optim.optimizer.Optimizer8bit": False,
    "optim.optimizer.MockArgs": False,
}

__version__ = "0.45.4.dev0"

# Debug prints
import sys
print("=" * 50)
print(f"bitsandbytes version: {__version__}")
print(f"bitsandbytes module path: {__file__}")
print(f"matmul_4bit in dir(bitsandbytes): {'matmul_4bit' in dir()}")
print(f"All available functions: {[name for name in dir() if not name.startswith('__')]}")
print("=" * 50)
