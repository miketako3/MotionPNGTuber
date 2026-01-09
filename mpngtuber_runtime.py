#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Runtime helpers for bundled/CLI execution.
"""

from __future__ import annotations

import os
import sys
from typing import List


def app_dir() -> str:
    """Return the base directory that contains bundled scripts/assets."""
    if getattr(sys, "frozen", False):
        return getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


def resolve_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    return os.path.join(app_dir(), path)


def python_cmd(script_path: str) -> List[str]:
    """Return command to run a script, compatible with frozen builds."""
    if getattr(sys, "frozen", False):
        # Run via the GUI exe in script mode
        return [sys.executable, "--run-script", script_path]
    return [sys.executable, script_path]
