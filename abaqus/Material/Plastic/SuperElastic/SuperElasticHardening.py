class SuperElasticHardening:
    """The SuperElasticHardening object specifies the dependence of the yield stress on the
    total strain to define the piecewise linear hardening of a martensite material model. 

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].superElasticity.SuperElasticHardening
        - import odbMaterial
        - session.odbs[name].materials[name].superElasticity.SuperElasticHardening

    Table Data
    ----------
        - Yield Stress.
        - Total Strain.

    Corresponding analysis keywords
    -------------------------------
        - SUPERELASTIC HARDENING

    """

    def __init__(self, table: tuple):
        """This method creates a SuperElasticHardening object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].superElasticity.SuperElasticHardening
            - session.odbs[name].materials[name].superElasticity.SuperElasticHardening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 

        Returns
        -------
            A SuperElasticHardening object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the SuperElasticHardening object.

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
