from abaqusConstants import *
from abaqus.Material.Others.MassDiffusion.PressureEffect import PressureEffect
from abaqus.Material.Others.MassDiffusion.SoretEffect import SoretEffect


class Diffusivity:
    """The Diffusivity object specifies mass diffusivity.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].diffusivity
        - import odbMaterial
        - session.odbs[name].materials[name].diffusivity

    Table Data
    ----------
        If *type*=ISOTROPIC, the table data specify the following:
        - Diffusivity, D.
        - Concentration, c.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=ORTHOTROPIC, the table data specify the following:
        - D11.
        - D22.
        - D33.
        - Concentration, c.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=ANISOTROPIC, the table data specify the following:
        - D11.
        - D12.
        - D22.
        - D13.
        - D23.
        - D33.
        - Concentration, c.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - DIFFUSIVITY

    """

    # A PressureEffect object. 
    pressureEffect: PressureEffect = PressureEffect(((),))

    # A SoretEffect object. 
    soretEffect: SoretEffect = SoretEffect(((),))

    def __init__(self, table: tuple, type: SymbolicConstant = ISOTROPIC, law: SymbolicConstant = GENERAL,
                 temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a Diffusivity object.

        Path
        ----
            - mdb.models[name].materials[name].Diffusivity
            - session.odbs[name].materials[name].Diffusivity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        type
            A SymbolicConstant specifying the type of diffusivity. Possible values are ISOTROPIC, 
            ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC. 
        law
            A SymbolicConstant specifying the diffusion behavior. Possible values are GENERAL and 
            FICK. The default value is GENERAL. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A Diffusivity object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Diffusivity object.

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
