from abaqusConstants import *
from .Section import Section
from .SectionLayerArray import SectionLayerArray


class CompositeSolidSection(Section):
    """The CompositeSolidSection object defines the properties of a composite solid section.
    The CompositeSolidSection object is derived from the Section object. 

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
        - SOLID SECTION

    """

    def __init__(self, name: str, layup: SectionLayerArray, symmetric: Boolean = OFF, layupName: str = ''):
        """This method creates a CompositeSolidSection object.

        Path
        ----
            - mdb.models[name].CompositeSolidSection
            - session.odbs[name].CompositeSolidSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        layup
            A SectionLayerArray object specifying the solid cross-section. 
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis. 
            The default value is OFF. 
        layupName
            A String specifying the layup name for this section. The default value is an empty 
            string. 

        Returns
        -------
            A CompositeSolidSection object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, symmetric: Boolean = OFF, layupName: str = ''):
        """This method modifies the CompositeSolidSection object.

        Parameters
        ----------
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis. 
            The default value is OFF. 
        layupName
            A String specifying the layup name for this section. The default value is an empty 
            string. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass
