from .Section import Section
from .TransverseShearShell import TransverseShearShell

from __init__ import *
from __future__ import annotations


class ShellSection(Section):
    """The ShellSection object defines the properties of a shell section. The ShellSection
    object is derived from the Section object. The ShellSection object has no explicit 
    constructor and no methods or members. 
    The ShellSection object is derived from the Section object. 

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    transverseShear: TransverseShearShell
        A :py:class:`~abaqus.Section.TransverseShearShell.TransverseShearShell` object specifying the transverse shear stiffness properties.

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

    # A TransverseShearShell object specifying the transverse shear stiffness properties.
    transverseShear: TransverseShearShell = None
