

class SaturationDependence:

    """The SaturationDependence object specifies the dependence of the permeability of a 
    material on the saturation of the wetting liquid. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].permeability.saturationDependence
        - import odbMaterial
        - session.odbs[name].materials[name].permeability.saturationDependence

    Table Data
    ----------
        - ks. (Dimensionless.)
        - Saturation, s. (Dimensionless.)

    Corresponding analysis keywords
    -------------------------------
        - PERMEABILITY

    """

    def __init__(self, table: tuple):
        """This method creates a SaturationDependence object.

        Path
        ----
            - mdb.models[name].materials[name].permeability.SaturationDependence
            - session.odbs[name].materials[name].permeability.SaturationDependence

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 

        Returns
        -------
            A SaturationDependence object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the SaturationDependence object.

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

