from .ConcreteCompressionDamage import ConcreteCompressionDamage
from .ConcreteCompressionHardening import ConcreteCompressionHardening
from .ConcreteTensionDamage import ConcreteTensionDamage
from .ConcreteTensionStiffening import ConcreteTensionStiffening
from abaqusConstants import *

class ConcreteDamagedPlasticity:

    """The ConcreteDamagedPlasticity object specifies the concrete damaged plasticity model. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].concreteDamagedPlasticity
        - import odbMaterial
        - session.odbs[name].materials[name].concreteDamagedPlasticity

    Table Data
    ----------
        The table data specify the following:
        - Dilation angle, ψ (in degrees) in the p–q plane.
        - Flow potential eccentricity, ϵ. The default value is 0.1.
        - σb0/σt0σb⁢0/σt⁢0, the ratio of initial equibiaxial compressive yield stress to initial uniaxial compressive yield stress. The default value is 1.16.
        - Kc, the ratio of the second stress invariant on the tensile meridian, to that on the compressive meridian, at initial yield for any given value of the pressure invariant p such that the maximum principal stress is negative. The default value is 2/3.
        - Viscosity parameter, μ, used for the viscoplastic regularization of the concrete constitutive equations in an Abaqus/Standard analysis. This parameter is ignored in an Abaqus/Explicit analysis. The default value is 0.0.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CONCRETE DAMAGED PLASTICITY

    """

    # A ConcreteCompressionHardening object. 
    concreteCompressionHardening: ConcreteCompressionHardening = None

    # A ConcreteTensionStiffening object. 
    concreteTensionStiffening: ConcreteTensionStiffening = None

    # A ConcreteCompressionDamage object. 
    concreteCompressionDamage: ConcreteCompressionDamage = None

    # A ConcreteTensionDamage object. 
    concreteTensionDamage: ConcreteTensionDamage = None

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a ConcreteDamagedPlasticity object.

        Path
        ----
            - mdb.models[name].materials[name].ConcreteDamagedPlasticity
            - session.odbs[name].materials[name].ConcreteDamagedPlasticity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A ConcreteDamagedPlasticity object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the ConcreteDamagedPlasticity object.

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

