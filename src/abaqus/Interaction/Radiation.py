class Radiation:
    """The Radiation object specifies radiation for a contact interaction property.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactionProperties[name].radiation

    The corresponding analysis keywords are:

    - GAP RADIATION

    """

    def __init__(self, masterEmissivity: float, slaveEmissivity: float, table: tuple):
        """This method creates a Radiation object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].interactionProperties[name].Radiation

        Parameters
        ----------
        masterEmissivity
            A Float specifying the emissivity of the master surface.
        slaveEmissivity
            A Float specifying the emissivity of the slave surface.
        table
            A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap
            clearance, dd.

        Returns
        -------
            A Radiation object.
        """
        pass

    def setValues(self):
        """This method modifies the Radiation object."""
        pass
