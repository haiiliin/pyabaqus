from .Section import Section


class AcousticInterfaceSection(Section):
    """The AcousticInterfaceSection object defines the properties of an acoustic section.
    The AcousticInterfaceSection object is derived from the Section object. 

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
        - INTERFACE

    """

    def __init__(self, name: str, thickness: float = 1):
        """This method creates an AcousticInterfaceSection object.

        Path
        ----
            - mdb.models[name].AcousticInterfaceSection
            - session.odbs[name].AcousticInterfaceSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        thickness
            A Float specifying the thickness of the section. Possible values are *thickness* >> 0.0. 
            The default value is 1.0. 

        Returns
        -------
            An AcousticInterfaceSection object. 

        Exceptions
        ----------
            InvalidNameError and RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, thickness: float = 1):
        """This method modifies the AcousticInterfaceSection object.

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section. Possible values are *thickness* >> 0.0. 
            The default value is 1.0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass
