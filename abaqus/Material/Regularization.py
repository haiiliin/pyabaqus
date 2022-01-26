from abaqusConstants import *


class Regularization:
    """The Regularization object defines the tolerance to be used for regularizing material
    data. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].regularization
        - import odbMaterial
        - session.odbs[name].materials[name].regularization

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - DASHPOT

    """

    def __init__(self, rtol: float = 0, strainRateRegularization: SymbolicConstant = LOGARITHMIC):
        """This method creates a Regularization object.

        Path
        ----
            - mdb.models[name].materials[name].Regularization
            - session.odbs[name].materials[name].Regularization

        Parameters
        ----------
        rtol
            A Float specifying the tolerance to be used for regularizing material data. The default 
            value is 0.03. 
        strainRateRegularization
            A SymbolicConstant specifying the form of regularization of strain-rate-dependent 
            material data. Possible values are LOGARITHMIC and LINEAR. The default value is 
            LOGARITHMIC. 

        Returns
        -------
            A Regularization object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Regularization object.

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
