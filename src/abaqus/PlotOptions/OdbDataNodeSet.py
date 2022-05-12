from __init__ import *
from __future__ import annotations


class OdbDataNodeSet:
    """The OdbDataNodeSet object stores node set data.

    Attributes
    ----------
    name: str
        A String specifying the set name. This attribute is read-only.
    nodes: str
        A String-to-Tuple-of-Ints Dictionary specifying the nodes in the set. This attribute is
        read-only.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import visualization
            session.odbData[name].nodeSets[i]

    """

    # A String specifying the set name. This attribute is read-only.
    name: str = ''

    # A String-to-Tuple-of-Ints Dictionary specifying the nodes in the set. This attribute is
    # read-only.
    nodes: str = ''
