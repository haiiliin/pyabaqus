from .CommandRegister import CommandRegister

class RegisteredList(CommandRegister):

    """This class allows you to create a list that can be queried from the GUI and is capable 
    of notifying the GUI when the contents of the list change. 
    The RegisteredList object is derived from the CommandRegister object. 

    Access
    ------
        - import customKernel

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self):
        """This method creates a RegisteredList object.

        Path
        ----
            - customKernel.RegisteredList

        Parameters
        ----------

        Returns
        -------
            A RegisteredList object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def Methods(self):
        """The RegisteredList object supports the same methods as a standard Python list object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

