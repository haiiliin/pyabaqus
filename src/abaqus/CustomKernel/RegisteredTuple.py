from .CommandRegister import CommandRegister

from __init__ import *
from __future__ import annotations


class RegisteredTuple(CommandRegister):
    """This class allows you to create a Tuple that can be queried from the GUI and is capable
    of notifying the GUI when the contents of any of the Tuple's members change. 
    The RegisteredTuple object is derived from the CommandRegister object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import customKernel

    """
    def __init__(self, Tuple: Tuple):
        """This method creates a RegisteredTuple object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            customKernel.RegisteredTuple
        
        Parameters
        ----------
        Tuple
            A Tuple of objects. These objects must be derived from the CommandRegister class. 

        Returns
        -------
            A RegisteredTuple object.
        """
        super().__init__()
        pass

    def Methods(self):
        """The RegisteredTuple object supports the same methods as a standard Python list object.
        """
        pass
