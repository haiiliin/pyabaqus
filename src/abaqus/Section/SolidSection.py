from .Section import Section

from __init__ import *
from __future__ import annotations


class SolidSection(Section):
    """The ShellSection object defines the properties of a shell section. The ShellSection
    object is derived from the Section object. The ShellSection object has no explicit 
    constructor and no methods or members. 
    The ShellSection object is derived from the Section object. 

    Attributes
    ----------
    name: str
        A String specifying the repository key.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

    """

    # A String specifying the repository key.
    name: str = ''
