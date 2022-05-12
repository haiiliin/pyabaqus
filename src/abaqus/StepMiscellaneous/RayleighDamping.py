from .RayleighDampingComponentArray import RayleighDampingComponentArray

from __init__ import *
from __future__ import annotations


class RayleighDamping:
    """A RayleighDamping object contains Rayleigh Damping parameters.

    Attributes
    ----------
    components: RayleighDampingComponentArray
        A :py:class:`~abaqus.StepMiscellaneous.RayleighDampingComponentArray.RayleighDampingComponentArray` object.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
        
           import step
           mdb.models[name].steps[name].rayleighDamping

    """

    # A RayleighDampingComponentArray object.
    components: RayleighDampingComponentArray = RayleighDampingComponentArray()
