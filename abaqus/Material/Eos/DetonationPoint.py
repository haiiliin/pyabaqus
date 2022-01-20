class DetonationPoint:
    """A DetonationPoint object specifies a suboption of the Eos object. The DetonationPoint
    object defines either isotropic linear elastic shear or linear viscous shear behavior 
    for a hydrodynamic material. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].eos.detonationPoint
        - import odbMaterial
        - session.odbs[name].materials[name].eos.detonationPoint

    Table Data
    ----------
        - X value for coordinate of detonation point.
        - Y value for coordinate of detonation point.
        - Z value for coordinate of detonation point.
        - Detonation delay time.

    Corresponding analysis keywords
    -------------------------------
        - DETONATION POINT

    """

    def __init__(self, table: tuple):
        """This method creates a DetonationPoint object.

        Path
        ----
            - mdb.models[name].materials[name].eos.DetonationPoint
            - session.odbs[name].materials[name].eos.DetonationPoint

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 

        Returns
        -------
            A DetonationPoint object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the DetonationPoint object.

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
