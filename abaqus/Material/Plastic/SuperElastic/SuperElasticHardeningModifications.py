class SuperElasticHardeningModifications:
    """The SuperElasticHardeningModifications object specifies the variation of the
    transformation stress levels of a material model. 

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].superElasticity.SuperElasticHardening
        - import odbMaterial
        - session.odbs[name].materials[name].superElasticity.SuperElasticHardening

    Table Data
    ----------
        - Start of Transformation (Loading).
        - End of Transformation (Loading).
        - Start of Transformation (Unloading).
        - End of Transformation (Unloading).
        - Plastic Strain.

    Corresponding analysis keywords
    -------------------------------
        - SUPERELASTIC HARDENING MODIFICATIONS

    """

    def __init__(self, table: tuple):
        """This method creates a SuperElasticHardeningModifications object.

        Path
        ----
            - mdb.models[name].materials[name].superElasticity.SuperElasticHardeningModifications
            - session.odbs[name].materials[name].superElasticity.SuperElasticHardeningModifications

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below or user-defined 
            data if the dependence of the transformation stress levels on Plastic strain is
            specified in a user subroutine. 

        Returns
        -------
            A SuperElasticHardeningModifications object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the SuperElasticHardeningModifications object.

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
