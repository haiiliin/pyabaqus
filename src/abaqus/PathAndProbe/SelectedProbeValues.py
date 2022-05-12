from abaqusConstants import *

from __init__ import *
from __future__ import annotations


class SelectedProbeValues:
    """The SelectedProbeValues object has no constructor. The SelectedProbeValues object is
    created when you import the Visualization module. 

    Attributes
    ----------
    length: int
        An Int specifying the length of the **values** member.
    fieldOutputAvailable: Boolean
        A Boolean specifying whether any probe values have been selected (as is necessary prior
        to writing to a file).
    values: float
        A Tuple of tuples of Floats specifying the selected probe values.
    lastValues: Tuple
        A Tuple of Floats specifying the last sequence of the **values** member.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import visualization
            session.selectedProbeValues

    """

    # An Int specifying the length of the *values* member.
    length: int = None

    # A Boolean specifying whether any probe values have been selected (as is necessary prior
    # to writing to a file).
    fieldOutputAvailable: Boolean = OFF

    # A Tuple of tuples of Floats specifying the selected probe values.
    values: float = None

    # A Tuple of Floats specifying the last sequence of the *values* member.
    lastValues: Tuple = ()
