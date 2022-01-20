from abaqusConstants import *
from .Inertia import Inertia
from ..Region.Region import Region


class HeatCapacitance(Inertia):
    """The HeatCapacitance object defines point heat capacitance on a part or an assembly
    region. 
    The HeatCapacitance object is derived from the Inertia object. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].engineeringFeatures.inertias[name]
        - import assembly
        - mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]

    Table Data
    ----------
        The table data specify the following:
        - Heat capacitance magnitude, ρcVρ⁢c⁢V (density × specific heat × volume).
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - HEATCAP

    """

    # A Boolean specifying whether the inertia is suppressed or not. The default value is OFF. 
    suppressed: Boolean = OFF

    def __init__(self, name: str, region: Region, table: tuple, temperatureDependency: Boolean = OFF,
                 dependencies: int = 0):
        """This method creates a HeatCapacitance object.

        Path
        ----
            - mdb.models[name].parts[name].engineeringFeatures.HeatCapacitance
            - mdb.models[name].rootAssembly.engineeringFeatures.HeatCapacitance

        Parameters
        ----------
        name
            A String specifying the repository key. 
        region
            A Region object specifying the region to which the heat capacitance is applied. 
        table
            A sequence of sequences of Floats specifying heat capacitance properties. The items in 
            the table data are described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A HeatCapacitance object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method modifies the HeatCapacitance object.

        Parameters
        ----------
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
