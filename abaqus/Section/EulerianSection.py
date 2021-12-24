from .Section import Section

class EulerianSection(Section):

    """The EulerianSection object defines the properties of a Eulerian section. 
    The EulerianSection object is derived from the Section object. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name]
        - import odbSection
        - session.odbs[name].sections[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - EULERIAN SECTION

    """

    def __init__(self, name: str, data: str):
        """This method creates a EulerianSection object.

        Path
        ----
            - mdb.models[name].EulerianSection
            - session.odbs[name].EulerianSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        data
            A String-to-String Dictionary specifying a dictionary mapping Material instance names to 
            Material names. Internally the specified mapping gets sorted on Material instance name. 

        Returns
        -------
            An EulerianSection object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the EulerianSection object.

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

