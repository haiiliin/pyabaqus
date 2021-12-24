from .InteractionProperty import InteractionProperty

class ActuatorSensorProp(InteractionProperty):

    """The ActuatorSensorProp object is an interaction property that defines the properties 
    referred to by an ActuatorSensor object. 
    The ActuatorSensorProp object is derived from the InteractionProperty object. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactionProperties[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - UEL PROPERTY

    """

    def __init__(self, name: str, realProperties: tuple = (), integerProperties: tuple = ()):
        """This method creates an ActuatorSensorProp object.

        Path
        ----
            - mdb.models[name].ActuatorSensorProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key. 
        realProperties
            A sequence of Floats specifying the PROPS array used by user subroutine UEL. The default 
            value is an empty sequence. 
        integerProperties
            A sequence of Ints specifying the JPROPS array used by user subroutine UEL. The default 
            value is an empty sequence. 

        Returns
        -------
            An ActuatorSensorProp object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, realProperties: tuple = (), integerProperties: tuple = ()):
        """This method modifies the ActuatorSensorProp object.

        Parameters
        ----------
        realProperties
            A sequence of Floats specifying the PROPS array used by user subroutine UEL. The default 
            value is an empty sequence. 
        integerProperties
            A sequence of Ints specifying the JPROPS array used by user subroutine UEL. The default 
            value is an empty sequence. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

