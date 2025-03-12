from ._functions import get_inverse_transform_indices, undo_layout, matmul_4bit

# Debug prints
import sys
print("=" * 50)
print("bitsandbytes.autograd module loaded")
print(f"autograd module path: {__file__}")
print(f"Available functions: {[name for name in dir() if not name.startswith('__')]}")
print(f"matmul_4bit in dir(): {'matmul_4bit' in dir()}")
print("=" * 50)
