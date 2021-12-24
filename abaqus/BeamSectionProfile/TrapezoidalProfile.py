from .Profile import Profile

class TrapezoidalProfile(Profile):

    """The TrapezoidalProfile object defines the properties of a trapezoidal profile. 
    The TrapezoidalProfile object is derived from the Profile object. 

    Access
    ------
        - import section
        - mdb.models[name].profiles[name]
        - import odbSection
        - session.odbs[name].profiles[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - BEAM SECTION

    """

    def __init__(self, name: str, a: float, b: float, c: float, d: float):
        """This method creates a TrapezoidalProfile object.

        Path
        ----
            - mdb.models[name].TrapezoidalProfile
            - session.odbs[name].TrapezoidalProfile

        Parameters
        ----------
        name
            A String specifying the repository key. 
        a
            A positive Float specifying the *a* dimension of the Trapezoidal profile. For more 
            information, see [Beam cross-section 
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all). 
        b
            A positive Float specifying the *b* dimension of the Trapezoidal profile. 
        c
            A positive Float specifying the *c* dimension of the Trapezoidal profile. 
        d
            A Float specifying the *d* dimension of the Trapezoidal profile. 

        Returns
        -------
            A TrapezoidalProfile object. 

        Exceptions
        ----------
            RangeError. 
            !img 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the TrapezoidalProfile object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
            !img 
        """
        pass

