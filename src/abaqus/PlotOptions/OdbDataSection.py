from __init__ import *
from __future__ import annotations


class OdbDataSection:
    """The OdbDataSection object stores section data.

    Attributes
    ----------
    name: str
        A String specifying the set name. This attribute is read-only.
    elements: str
        A String-to-Tuple-of-Ints Dictionary specifying the elements in the set. This attribute
        is read-only.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import visualization
            session.odbData[name].sections[i]

    """

    # A String specifying the set name. This attribute is read-only.
    name: str = ''

    # A String-to-Tuple-of-Ints Dictionary specifying the elements in the set. This attribute
    # is read-only.
    elements: str = ''
