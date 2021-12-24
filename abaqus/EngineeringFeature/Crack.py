from abaqusConstants import *

class Crack:

    """The Crack object is the abstract base type for ContourIntegral and future crack objects. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].engineeringFeatures.cracks[name]
        - import assembly
        - mdb.models[name].rootAssembly.engineeringFeatures.cracks[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. 
    name: str = ''

    # A Boolean specifying whether the crack is suppressed or not. The default value is OFF. 
    suppressed: Boolean = OFF

    def resume(self):
        """This method resumes the crack that was previously suppressed.

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
        """This method suppresses the crack.

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

