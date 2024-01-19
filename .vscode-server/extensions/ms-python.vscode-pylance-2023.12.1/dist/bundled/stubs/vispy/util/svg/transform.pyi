# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------
import re
import math
import numpy as np

# ------------------------------------------------------------------ Matrix ---

class Matrix(object):
    def __init__(self, a=1, b=0, c=0, d=1, e=0, f=0): ...
    @property
    def matrix(self): ...
    def __array__(self, *args): ...
    def __repr__(self): ...

# ---------------------------------------------------------------- Identity ---
class Identity(Matrix):
    def __init__(self): ...
    def __repr__(self): ...

# --------------------------------------------------------------- Translate ---
class Translate(Matrix):
    def __init__(self, x, y=0): ...
    def __repr__(self): ...

# ------------------------------------------------------------------- Scale ---
class Scale(Matrix):
    def __init__(self, x, y=0): ...
    def __repr__(self): ...

# ------------------------------------------------------------------- Scale ---
class Rotate(Matrix):
    def __init__(self, angle, x=0, y=0): ...
    def __repr__(self): ...

# ------------------------------------------------------------------- SkewX ---
class SkewX(Matrix):
    def __init__(self, angle): ...
    def __repr__(self): ...

# ------------------------------------------------------------------- SkewY ---
class SkewY(Matrix):
    def __init__(self, angle): ...
    def __repr__(self): ...

# --------------------------------------------------------------- Transform ---
class Transform(object):
    def __init__(self, content=""): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    @property
    def matrix(self): ...
    def __array__(self, *args): ...
    def __repr__(self): ...
    @property
    def xml(self): ...
    def _xml(self, prefix=""): ...
