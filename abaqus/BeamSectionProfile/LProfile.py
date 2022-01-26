from .Profile import Profile

class LProfile(Profile):

    """The LProfile object defines the properties of a L profile. 
    The LProfile object is derived from the Profile object. 

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

    def __init__(self, name: str, a: float, b: float, t1: float, t2: float):
        """This method creates a LProfile object.

        Path
        ----
            - mdb.models[name].LProfile
            - session.odbs[name].LProfile

        Parameters
        ----------
        name
            A String specifying the repository key. 
        a
            A positive Float specifying the *a* dimension (flange length) of the L profile. For more 
            information, see [Beam cross-section 
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all). 
        b
            A positive Float specifying the *b* dimension (flange length) of the L profile. 
        t1
            A positive Float specifying the *t1* dimension (flange thickness) of the L profile (*t1 
            < b*). 
        t2
            A positive Float specifying the *t2* dimension (flange thickness) of the L profile (*t2< 
            a*). 

        Returns
        -------
            A LProfile object. 

        Raises
        ------
            RangeError. 
            !img 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the LProfile object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Raises
        ------
            RangeError. 
            !img 
        """
        pass

