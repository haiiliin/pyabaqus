from abaqusConstants import *


class CycledPlastic:
    """The CycledPlastic object specifies cycled yield stress data for the ORNL constitutive
    model. 

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].Plastic.cycledPlastic
        - import odbMaterial
        - session.odbs[name].materials[name].Plastic.cycledPlastic

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

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].Plastic.CycledPlastic
            - session.odbs[name].materials[name].Plastic.CycledPlastic
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 

        Returns
        -------
            A CycledPlastic object. . 
        """
        pass

    def setValues(self):
        """This method modifies the CycledPlastic object.
        """
        pass
