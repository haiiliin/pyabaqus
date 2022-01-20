from abaqusConstants import *
from .ContactProperty import ContactProperty


class CavityRadiationProp(ContactProperty):
    """The CavityRadiationProp object is an interaction property that defines emissivity as a
    function of temperature and field variables. 
    The CavityRadiationProp object is derived from the InteractionProperty object. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactionProperties[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - EMISSIVITY

    """

    def __init__(self, name: str, temperatureDependency: Boolean = OFF, dependencies: int = 0,
                 property: tuple = ()):
        """This method creates a CavityRadiationProp object.

        Path
        ----
            - mdb.models[name].CavityRadiationProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        property
            A sequence of sequences of Floats specifying the following:The emissivity, 
            ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if 
            the data depend on field variables.Value of the second field variable.Etc. 

        Returns
        -------
            A CavityRadiationProp object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__(name)
        pass

    def setValues(self, temperatureDependency: Boolean = OFF, dependencies: int = 0, property: tuple = ()):
        """This method modifies the CavityRadiationProp object.

        Parameters
        ----------
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        property
            A sequence of sequences of Floats specifying the following:The emissivity, 
            ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if 
            the data depend on field variables.Value of the second field variable.Etc. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
