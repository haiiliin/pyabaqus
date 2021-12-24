

class OdbLoadCase:

    """The OdbLoadCase object describes a load case. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].steps[name].frames[i].loadCase
        - session.odbs[name].steps[name].historyRegions[name].loadCase
        - session.odbs[name].steps[name].loadCases[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def LoadCase(self, name: str):
        """This method creates an OdbLoadCase object.

        Path
        ----
            - session.odbs[*name*].steps[*name*].LoadCase

        Parameters
        ----------
        name
            A String specifying the name of the OdbLoadCase object. 

        Returns
        -------
            An OdbLoadCase object. 

        Exceptions
        ----------
            None. 
        """
        pass

