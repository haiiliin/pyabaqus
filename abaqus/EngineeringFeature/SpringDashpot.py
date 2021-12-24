from abaqusConstants import *

class SpringDashpot:

    """The SpringDashpot object is the abstract base type for the SpringDashpotToGround and 
    TwoPointSpringDashpot objects. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].engineeringFeatures.springDashpots[name]
        - import assembly
        - mdb.models[name].rootAssembly.engineeringFeatures.springDashpots[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. 
    name: str = ''

    # A Boolean specifying whether the spring/dashpot is suppressed or not. The default value 
    # is OFF. 
    suppressed: Boolean = OFF

    def resume(self):
        """This method resumes the spring/dashpot that was previously suppressed.

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
        """This method suppresses the spring/dashpot.

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

