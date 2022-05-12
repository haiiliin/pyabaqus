from abaqusConstants import *
from .ContactProperty import ContactProperty

from __init__ import *
from __future__ import annotations


class CavityRadiationProp(ContactProperty):
    """The CavityRadiationProp object is an interaction property that defines emissivity as a
    function of temperature and field variables. 
    The CavityRadiationProp object is derived from the InteractionProperty object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactionProperties[name]

    The corresponding analysis keywords are:
        - EMISSIVITY

    """
    def __init__(self,
                 name: str,
                 temperatureDependency: Boolean = OFF,
                 dependencies: int = 0,
                 property: Tuple = ()):
        """This method creates a CavityRadiationProp object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].CavityRadiationProp
        
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
        """
        super().__init__(name)
        pass

    def setValues(self,
                  temperatureDependency: Boolean = OFF,
                  dependencies: int = 0,
                  property: Tuple = ()):
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
        """
        pass
