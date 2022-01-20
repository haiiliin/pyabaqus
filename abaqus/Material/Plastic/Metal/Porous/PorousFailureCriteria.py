class PorousFailureCriteria:
    """The PorousFailureCriteria object specifies the material failure criteria for a porous
    metal. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].porousMetalPlasticity.porousFailureCriteria
        - import odbMaterial
        - session.odbs[name].materials[name].porousMetalPlasticity.porousFailureCriteria

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - POROUS FAILURE CRITERIA

    """

    def __init__(self, fraction: float = 1, criticalFraction: float = 1):
        """This method creates a PorousFailureCriteria object.

        Path
        ----
            - mdb.models[name].materials[name].porousMetalPlasticity\
            - .PorousFailureCriteria
            - session.odbs[name].materials[name].porousMetalPlasticity\
            - .PorousFailureCriteria

        Parameters
        ----------
        fraction
            A Float specifying the void volume fraction at total failure, fF>0. The default value is 
            1.0. 
        criticalFraction
            A Float specifying the critical void volume fraction, fc≥0. The default value is 1.0. 

        Returns
        -------
            A PorousFailureCriteria object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the PorousFailureCriteria object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass
