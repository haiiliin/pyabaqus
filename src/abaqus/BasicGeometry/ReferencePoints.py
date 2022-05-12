from .ReferencePoint import ReferencePoint

from __init__ import *
from __future__ import annotations


class ReferencePoints(dict[int, ReferencePoint]):
    def __getitem__(self, key: int) -> ReferencePoint:
        if key in self.keys():
            return self.get(key)
        else:
            return ReferencePoint(point=(0., 0., 0.))
