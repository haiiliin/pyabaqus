from abaqusConstants import *

class GapConvection:

    """The GapConvection object specifies the Nusselt number (Nu) to calculate the convective 
    coefficient for heat transfer between the gap flow and both the top and bottom surfaces 
    of a coupled temperature-pore pressure cohesive element. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].gapConvection
        - import odbMaterial
        - session.odbs[name].materials[name].gapConvection

    Table Data
    ----------
        For *type*=TABULAR the table data specify the following:
        - Nusselt number (Nu)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - GAP CONVECTION

    """

    def __init__(self, type: str, table: tuple = (), temperatureDependency: Boolean = OFF, 
                 dependencies: int = 0):
        """This method creates a GapConvection object.

        Path
        ----
            - mdb.models[name].materials[name].GapConvection
            - session.odbs[name].materials[name].GapConvection

        Parameters
        ----------
        type
            An odb_String specifying the type of gap convection. Possible values are FLUX, 
            TEMPERATURE, and TABULAR. The default value is FLUX. 
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A GapConvection object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the GapConvection object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
        """
        pass

