from .Profile import Profile

class RectangularProfile(Profile):

    """The RectangularProfile object defines the properties of a solid rectangular profile. 
    The RectangularProfile object is derived from the Profile object. 

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

    def __init__(self, name: str, a: float, b: float):
        """This method creates a RectangularProfile object.

        Path
        ----
            - mdb.models[name].RectangularProfile
            - session.odbs[name].RectangularProfile

        Parameters
        ----------
        name
            A String specifying the repository key. 
        a
            A positive Float specifying the *a* dimension of the rectangular profile. For more 
            information, see [Beam cross-section 
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all). 
        b
            A positive Float specifying the *b* dimension of the rectangular profile. 

        Returns
        -------
            A RectangularProfile object. 

        Exceptions
        ----------
            RangeError. 
            !img 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the RectangularProfile object.

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

