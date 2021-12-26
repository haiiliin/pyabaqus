from abaqusConstants import *
from .SaturationDependence import SaturationDependence
from .VelocityDependence import VelocityDependence


class Permeability:

    """The Permeability object defines permeability for pore fluid flow. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].permeability
        - import odbMaterial
        - session.odbs[name].materials[name].permeability

    Table Data
    ----------
        If *type*=ISOTROPIC, the table data specify the following:
        - k.
        - Void ratio, e.
        - Temperature, if the data depend on temperature.
        If *type*=ORTHOTROPIC, the table data specify the following:
        - k11.
        - k22.
        - k33.
        - Void ratio, e.
        - Temperature, if the data depend on temperature.
        If *type*=ANISOTROPIC, the table data specify the following:
        - k11.
        - k12.
        - k22.
        - k13.
        - k23.
        - k33.
        - Void ratio, e.
        - Temperature, if the data depend on temperature.

    Corresponding analysis keywords
    -------------------------------
        - PERMEABILITY

    """

    # A SaturationDependence object specifying the dependence of the permeability of a 
    # material on the saturation of the wetting liquid. 
    saturationDependence: SaturationDependence = SaturationDependence(((), ))

    # A VelocityDependence object specifying the dependence of the permeability of a material 
    # on the velocity of fluid flow. 
    velocityDependence: VelocityDependence = VelocityDependence(((), ))

    def __init__(self, specificWeight: float, inertialDragCoefficient: float, table: tuple, 
                 type: SymbolicConstant = ISOTROPIC, temperatureDependency: Boolean = OFF, 
                 dependencies: int = 0):
        """This method creates a Permeability object.

        Path
        ----
            - mdb.models[name].materials[name].Permeability
            - session.odbs[name].materials[name].Permeability

        Parameters
        ----------
        specificWeight
            A Float specifying the specific weight of the wetting liquid, γwγw. 
        inertialDragCoefficient
            A Float specifying The inertial drag coefficient of the wetting liquid, γwγw. 
        table
            A sequence of sequences of Floats specifying the items described below. 
        type
            A SymbolicConstant specifying the type of permeability. Possible values are ISOTROPIC, 
            ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A Permeability object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Permeability object.

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

