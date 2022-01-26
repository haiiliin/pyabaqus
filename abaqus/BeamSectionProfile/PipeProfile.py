from .Profile import Profile

class PipeProfile(Profile):

    """The PipeProfile object defines the properties of a circular pipe profile. 
    The PipeProfile object is derived from the Profile object. 

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

    def __init__(self, name: str, r: float, t: float):
        """This method creates a PipeProfile object.

        Path
        ----
            - mdb.models[name].PipeProfile
            - session.odbs[name].PipeProfile

        Parameters
        ----------
        name
            A String specifying the repository key. 
        r
            A Float specifying the outer radius of the pipe. For more information, see [Beam 
            cross-section 
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all). 
        t
            A Float specifying the wall thickness of the pipe. 

        Returns
        -------
            A PipeProfile object. 

        Raises
        ------
            RangeError. 
            !img 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the PipeProfile object.

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

