from abaqusConstants import *

class CycledPlastic:

    """The CycledPlastic object specifies cycled yield stress data for the ORNL constitutive 
    model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].plastic.cycledPlastic
        - import odbMaterial
        - session.odbs[name].materials[name].plastic.cycledPlastic

    Table Data
    ----------
        - Yield stress.
        - Plastic strain.
        - Temperature, if the data depend on temperature.

    Corresponding analysis keywords
    -------------------------------
        - CYCLED PLASTIC

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF):
        """This method creates a CycledPlastic object.

        Path
        ----
            - mdb.models[name].materials[name].plastic.CycledPlastic
            - session.odbs[name].materials[name].plastic.CycledPlastic

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 

        Returns
        -------
            A CycledPlastic object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the CycledPlastic object.

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

