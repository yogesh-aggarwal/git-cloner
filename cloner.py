import os
import click

try:
    os.system("python Source/runtime.py")
except Exception:
    os.system("python3 Source/runtime.py")
