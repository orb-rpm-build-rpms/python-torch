#!/usr/bin/env python3
"""
inject_build_options.py

Runtime stub for injecting PyTorch CMake build flags.
Designed to be called pre-build (e.g., via a wrapper script or sitecustomize.py).
"""
import os
from typing import Dict, Any

def read_environment() -> Dict[str, str]:
    """Reads and prints environment variables in dictionary format."""
    # Using double quotes to match the MOCK_DEFAULTS dictionary style exactly
    print("# Current Environment Variables (Formatted for injection):")
    use_variables: Dict[str, Any] = {}

    for key in sorted(os.environ.keys()):
        if key.startswith("USE_") or key.startswith("CMAKE_") :
            value = os.environ[key]
            print(f'    "{key}": "{value}",')
            use_variables[key] = value
    return use_variables

def build_options(build_options: Dict[str, Any]) -> Dict[str, Any] :
    """
    Injects build configuration into the PyTorch CMake build process.

    """
    options = read_environment()
    build_options.update(options)
    return build_options

if __name__ == "__main__":
    MOCK_DEFAULTS = {
        # Core CMake
        "CMAKE_BUILD_TYPE": "RelWithDebInfo",
        "CMAKE_FIND_PACKAGE_PREFER_CONFIG": "ON",
        "CAFFE2_LINK_LOCAL_PROTOBUF": "OFF",
    }

    new_options = build_options(MOCK_DEFAULTS)

    for key in new_options:
        print(f"{key}: {new_options[key]}")
