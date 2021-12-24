from abaqusConstants import *
import typing

class TransverseShearBeam:

    """The TransverseShearBeam object defines the transverse shear stiffness properties of a 
    beam section. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name].beamTransverseShear
        - import odbSection
        - session.odbs[name].sections[name].beamTransverseShear

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - TRANSVERSE SHEAR STIFFNESS

    """

    def __init__(self, scfDefinition: SymbolicConstant, k23: float = None, k13: float = None, 
                 slendernessCompensation: typing.Union[SymbolicConstant, float] = 0):
        """This method creates a TransverseShearBeam object.

        Path
        ----
            - mdb.models[name].sections[name].TransverseShearBeam
            - session.odbs[name].sections[name].TransverseShearBeam

        Parameters
        ----------
        scfDefinition
            A SymbolicConstant specifying how slenderness compensation factor of the section is 
            given. Possible values are ANALYSIS_DEFAULT, COMPUTED, and VALUE. 
        k23
            None or a Float specifying the k23 shear stiffness of the section. The default value is 
            None. 
        k13
            None or a Float specifying the k13 shear stiffness of the section. The default value is 
            None. 
        slendernessCompensation
            The SymbolicConstant COMPUTED or a Float specifying the slenderness compensation factor 
            of the section. The default value is 0.25. 

        Returns
        -------
            A TransverseShearBeam object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the TransverseShearBeam object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

