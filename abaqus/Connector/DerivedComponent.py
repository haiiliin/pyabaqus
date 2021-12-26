from .CDCTermArray import CDCTermArray

class DerivedComponent:

    """A DerivedComponent object describes user-customized components for use in defining 
    ConnectorFriction and Potential objects. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent
        - mdb.models[name].sections[name].behaviorOptions[i].derivedComponent
        - mdb.models[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent
        - mdb.models[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent
        - import odbSection
        - session.odbs[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent
        - session.odbs[name].sections[name].behaviorOptions[i].derivedComponent
        - session.odbs[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent
        - session.odbs[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - CONNECTOR DERIVED COMPONENT

    """

    # A CDCTermArray object. 
    cdcTerms: CDCTermArray = CDCTermArray()

    def __init__(self):
        """This method creates a DerivedComponent object.

        Path
        ----
            - mdb.models[name].sections[name].behaviorOptions[i]\
            - .connectorPotentials[i].DerivedComponent
            - mdb.models[name].sections[name].behaviorOptions[i].DerivedComponent
            - mdb.models[name].sections[name].behaviorOptions[i]\
            - .evolutionPotentials[i].DerivedComponent
            - mdb.models[name].sections[name].behaviorOptions[i]\
            - .initiationPotentials[i].DerivedComponent
            - session.odbs[name].sections[name].behaviorOptions[i]\
            - .connectorPotentials[i].DerivedComponent
            - session.odbs[name].sections[name].behaviorOptions[i].DerivedComponent
            - session.odbs[name].sections[name].behaviorOptions[i]\
            - .evolutionPotentials[i].DerivedComponent
            - session.odbs[name].sections[name].behaviorOptions[i]\
            - .initiationPotentials[i].DerivedComponent

        Parameters
        ----------

        Returns
        -------
            A DerivedComponent object. 

        Exceptions
        ----------
            ValueError and TextError. 
        """
        pass

    def setValues(self):
        """This method modifies the DerivedComponent object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            ValueError. 
        """
        pass

