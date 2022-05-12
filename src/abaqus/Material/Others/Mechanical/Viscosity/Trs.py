from abaqusConstants import *

from __init__ import *
from __future__ import annotations


class Trs:
    """The Trs object defines the temperature-time shift for time history viscoelastic
    analysis. 

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import material
            mdb.models[name].materials[name].viscoelastic.trs
            mdb.models[name].materials[name].viscosity.trs
            import odbMaterial
            session.odbs[name].materials[name].viscoelastic.trs
            session.odbs[name].materials[name].viscosity.trs

        The table data for this object are:
            - Reference temperature, θ0θ0.
            - Calibration constant, C1C1.
            - Calibration constant, C2C2.

    The corresponding analysis keywords are:
        - TRS

    """
    def __init__(self, definition: SymbolicConstant = WLF, table: Tuple = ()):
        """This method creates a Trs object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].viscoelastic.Trs
                mdb.models[name].materials[name].viscosity.Trs
                session.odbs[name].materials[name].viscoelastic.Trs
                session.odbs[name].materials[name].viscosity.Trs
        
        Parameters
        ----------
        definition
            A SymbolicConstant specifying the definition of the shift function. Possible values are 
            WLF, ARRHENIUS, and USER. The default value is WLF. 
        table
            A sequence of sequences of Floats specifying the items described below. The default 
            value is an empty sequence.This argument is valid only when *definition*=WLF. 

        Returns
        -------
            A Trs object.
        """
        pass

    def setValues(self):
        """This method modifies the Trs object.
        """
        pass
