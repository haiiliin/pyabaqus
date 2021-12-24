from abaqusConstants import *

class Constraint:

    """The Constraint object is the abstract base type for other Constraint objects. The 
    Constraint object has no explicit constructor. The members of the Constraint object are 
    common to all objects derived from the Constraint. 

    Access
    ------
        - import interaction
        - mdb.models[name].constraints[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the constraint repository key. 
    name: str = ''

    # A Boolean specifying whether the constraint is suppressed or not. The default value is 
    # OFF. 
    suppressed: Boolean = OFF

    def resume(self):
        """This method resumes the constraint that was previously suppressed.

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

    def suppress(self):
        """This method suppresses the constraint.

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

    def delete(self, indices: tuple):
        """This method allows you to delete existing constraints.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each constraint to delete. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

