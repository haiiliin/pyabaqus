from abaqusConstants import *


class TensionStiffening:
    """The TensionStiffening object defines the retained tensile stress normal to a crack in a
    Concrete model. 

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].concrete.tensionStiffening
        - import odbMaterial
        - session.odbs[name].materials[name].concrete.tensionStiffening

    Table Data
    ----------
        If *type*=STRAIN, the table data specify the following:
        - Fraction of remaining stress to stress at cracking.
        - Absolute value of the direct strain minus the direct strain at cracking.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=DISPLACEMENT, the table data specify the following:
        - Displacement, u0u0, at which a linear loss of strength after cracking gives zero stress.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - TENSION STIFFENING

    """

    def __init__(self, table: tuple, type: SymbolicConstant = STRAIN, temperatureDependency: Boolean = OFF,
                 dependencies: int = 0):
        """This method creates a TensionStiffening object.

        Path
        ----
            - mdb.models[name].materials[name].concrete.TensionStiffening
            - session.odbs[name].materials[name].concrete.TensionStiffening

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        type
            A SymbolicConstant specifying how the postcracking behavior is defined. Possible values 
            are DISPLACEMENT and STRAIN. The default value is STRAIN. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A TensionStiffening object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the TensionStiffening object.

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
