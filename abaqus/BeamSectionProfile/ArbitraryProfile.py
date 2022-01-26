from .Profile import Profile

class ArbitraryProfile(Profile):

    """The ArbitraryProfile object defines the properties of an arbitrary profile. 
    The ArbitraryProfile object is derived from the Profile object. 

    Access
    ------
        - import section
        - mdb.models[name].profiles[name]
        - import odbSection
        - session.odbs[name].profiles[name]

    Table Data
    ----------
        The first sequence in the table specifies the following:
        - 1-coordinate of the first point defining the profile.
        - 2-coordinate of the first point defining the profile.
        All other sequences in the table specify the following:
        - 1–coordinate of the next point defining the profile.
        - 2–coordinate of the next point defining the profile.
        - The thickness of the segment ending at that point.

    Corresponding analysis keywords
    -------------------------------
        - BEAM SECTION

    """

    def __init__(self, name: str, table: tuple):
        """This method creates a ArbitraryProfile object.

        Path
        ----
            - mdb.models[name].ArbitraryProfile
            - session.odbs[name].ArbitraryProfile

        Parameters
        ----------
        name
            A String specifying the repository key. 
        table
            A sequence of sequences of Floats specifying the items described below. 

        Returns
        -------
            An ArbitraryProfile object. 

        Raises
        ------
            RangeError. 
            !img 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the ArbitraryProfile object.

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

