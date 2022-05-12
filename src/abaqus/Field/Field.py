from __init__ import *
from __future__ import annotations


class Field:
    """The Field object is the abstract base type for other Field objects. The Field object has
    no explicit constructor. The methods and members of the Field object are common to all 
    objects derived from the Field. 

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    description: str
        A String specifying the description of the field. The default value is an empty string.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import fields

    """

    # A String specifying the repository key.
    name: str = ''

    # A String specifying the description of the field. The default value is an empty string.
    description: str = ''
