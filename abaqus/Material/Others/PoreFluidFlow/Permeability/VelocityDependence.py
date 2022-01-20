class VelocityDependence:
    """The VelocityDependence object specifies the dependence of the permeability of a material
    on the velocity of fluid flow. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].permeability.velocityDependence
        - import odbMaterial
        - session.odbs[name].materials[name].permeability.velocityDependence

    Table Data
    ----------
        - β. Only β> 0.0 is allowed.
        - Void ratio, ee.

    Corresponding analysis keywords
    -------------------------------
        - PERMEABILITY

    """

    def __init__(self, table: tuple):
        """This method creates a VelocityDependence object.

        Path
        ----
            - mdb.models[name].materials[name].permeability.VelocityDependence
            - session.odbs[name].materials[name].permeability.VelocityDependence

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 

        Returns
        -------
            A VelocityDependence object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the VelocityDependence object.

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
