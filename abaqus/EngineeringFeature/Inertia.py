from abaqusConstants import *

class Inertia:

    """The Inertia object is the abstract base type for HeatCapacitance, NonstructuralMass, and 
    PointMassInertia. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].engineeringFeatures.inertias[name]
        - import assembly
        - mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. 
    name: str = ''

    # A Boolean specifying whether the inertia is suppressed or not. The default value is OFF. 
    suppressed: Boolean = OFF

    def resume(self):
        """This method resumes the inertia that was previously suppressed.

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
        """This method suppresses the inertia.

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

