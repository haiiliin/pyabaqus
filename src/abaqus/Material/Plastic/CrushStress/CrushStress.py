from abaqusConstants import *

from .CrushStressVelocityFactor import CrushStressVelocityFactor


class CrushStress:
    """The CrushStress object specifies the crush stress of a material.

    Attributes
    ----------
    crushStressTable: tuple[tuple[float, ...]]
        A sequence of sequences of Floats specifying the items described below.
    temperatureDependency: Boolean
        A Boolean specifying whether the data depend on temperature. The default value is OFF.
    dependencies: int
        An Int specifying the number of field variable dependencies. The default value is 0.
    crushStressVelocityFactor: CrushStressVelocityFactor
        A :py:class:`~abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor.CrushStressVelocityFactor` object.


    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].crushStress
        import odbMaterial
        session.odbs[name].materials[name].crushStress

    The table data for this object are:

    - Scaling factor.
    - Relative velocity.

    The corresponding analysis keywords are:

    - CRUSH STRESS
    """

    # A sequence of sequences of Floats specifying the items described below.
    crushStressTable: tuple[tuple[float, ...]]

    # A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    # An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    # A :py:class:`~abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor.CrushStressVelocityFactor` object.
    crushStressVelocityFactor: CrushStressVelocityFactor = CrushStressVelocityFactor(((),))

    def __init__(self, crushStressTable: tuple[tuple[float, ...]], temperatureDependency: Boolean = OFF,
                 dependencies: int = 0):
        """This method creates a CrushStress object.

        Notes
        -----
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].CrushStress
                session.odbs[name].materials[name].CrushStress

        Parameters
        ----------
        crushStressTable
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        """
        self.crushStressTable = crushStressTable
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies

    def setValues(self, crushStressTable: tuple[tuple[float, ...]] = ((), ), temperatureDependency: Boolean = OFF,
                  dependencies: int = 0):
        """This method creates a CrushStress object.

        Notes
        -----
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].CrushStress
                session.odbs[name].materials[name].CrushStress

        Parameters
        ----------
        crushStressTable
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        """
        self.crushStressTable = crushStressTable
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
