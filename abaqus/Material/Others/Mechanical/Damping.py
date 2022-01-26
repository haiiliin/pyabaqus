class Damping:
    """The Damping object specifies material damping.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].damping
        - import odbMaterial
        - session.odbs[name].materials[name].damping

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - DAMPING

    """

    def __init__(self, alpha: float = 0, beta: float = 0, composite: float = 0, structural: float = 0):
        """This method creates a Damping object.

        Path
        ----
            - mdb.models[name].materials[name].Damping
            - session.odbs[name].materials[name].Damping

        Parameters
        ----------
        alpha
            A Float specifying the αRαR factor to create mass proportional damping in 
            direct-integration and explicit dynamics. The default value is 0.0. 
        beta
            A Float specifying the βRβR factor to create stiffness proportional damping in 
            direct-integration and explicit dynamics. The default value is 0.0. 
        composite
            A Float specifying the fraction of critical damping to be used with this material in 
            calculating composite damping factors for the modes (for use in modal dynamics). The 
            default value is 0.0.This argument applies only to Abaqus/Standard analyses. 
        structural
            A Float specifying the structural factor to create material damping in 
            direct-integration and explicit dynamics. The default value is 0.0. 

        Returns
        -------
            A Damping object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Damping object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Raises
        ------
            RangeError. 
        """
        pass
