from .ConnectorOptions import ConnectorOptions
from abaqusConstants import *

class CDCTerm:

    """The CDCTerm object is used to create contributing terms for a DerivedComponent object. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent.cdcTerms[i]
        - mdb.models[name].sections[name].behaviorOptions[i].derivedComponent.cdcTerms[i]
        - mdb.models[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent.cdcTerms[i]
        - mdb.models[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent.cdcTerms[i]
        - import odbSection
        - session.odbs[name].sections[name].behaviorOptions[i].connectorPotentials[i].derivedComponent.cdcTerms[i]
        - session.odbs[name].sections[name].behaviorOptions[i].derivedComponent.cdcTerms[i]
        - session.odbs[name].sections[name].behaviorOptions[i].evolutionPotentials[i].derivedComponent.cdcTerms[i]
        - session.odbs[name].sections[name].behaviorOptions[i].initiationPotentials[i].derivedComponent.cdcTerms[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A ConnectorOptions object specifying the ConnectorOptions used to define tabular options 
    # for this ConnectorBehaviorOption. 
    options: ConnectorOptions = None

    def __init__(self, intrinsicComponents: tuple, table: tuple, termOperator: SymbolicConstant = RSS, 
                 termSign: SymbolicConstant = POSITIVE, localDependency: Boolean = OFF, 
                 indepCompType: SymbolicConstant = POSITION, indepComponents: tuple = (), 
                 tempDependency: Boolean = OFF, fieldDependencies: int = 0):
        """This method creates a CDCTerm object.

        Path
        ----
            - mdb.models[name].sections[name].behaviorOptions[i]\
            - .connectorPotentials[i].derivedComponent.CDCTerm
            - mdb.models[name].sections[name].behaviorOptions[i].derivedComponent\
            - .CDCTerm
            - mdb.models[name].sections[name].behaviorOptions[i]\
            - .evolutionPotentials[i].derivedComponent.CDCTerm
            - mdb.models[name].sections[name].behaviorOptions[i]\
            - .initiationPotentials[i].derivedComponent.CDCTerm
            - session.odbs[name].sections[name].behaviorOptions[i]\
            - .connectorPotentials[i].derivedComponent.CDCTerm
            - session.odbs[name].sections[name].behaviorOptions[i].derivedComponent\
            - .CDCTerm
            - session.odbs[name].sections[name].behaviorOptions[i]\
            - .evolutionPotentials[i].derivedComponent.CDCTerm
            - session.odbs[name].sections[name].behaviorOptions[i]\
            - .initiationPotentials[i].derivedComponent.CDCTerm

        Parameters
        ----------
        intrinsicComponents
            A sequence of Ints specifying the components of relative motion for which the 
            contributing term is defined. Possible values are 1 ≤≤ *intrinsicComponents* ≤≤ 6. Only 
            available components can be specified if the DerivedComponent object is being referenced 
            by a Potential object. This is not the case if the DerivedComponent object is referenced 
            by a ConnectorFriction object directly. The default value is an empty sequence. 
        table
            A sequence of sequences of Floats specifying components numbers and temperature and 
            field values. Each sequence of the table data specifies:The first intrinsic component 
            number.If applicable, the second intrinsic component number.Etc.If applicable, the first 
            independent component number.If applicable, the second independent component 
            number.Etc.If applicable, the temperature value.If applicable, the value of the first 
            field variable.If applicable, the value of the second field variable.Etc.The default 
            value is an empty sequence. 
        termOperator
            A SymbolicConstant specifying the method for combining contributing terms: square root 
            of a sum of the squares, direct sum, or Macauley sum. Possible values are RSS, SUM, and 
            MACAULEY. The default value is RSS. 
        termSign
            A SymbolicConstant specifying the overall sign for the contributing term. Possible 
            values are POSITIVE and NEGATIVE. The default value is POSITIVE. 
        localDependency
            A Boolean specifying whether the table data depend on either components of relative 
            position or components of constitutive relative motion. The default value is OFF. 
        indepCompType
            A SymbolicConstant specifying whether localDependency refers to components of relative 
            position or components of constitutive relative motion. Possible values are POSITION and 
            MOTION. The default value is POSITION.The *indepCompType* argument applies only if 
            *localDependency*=ON. 
        indepComponents
            A sequence of Ints specifying the independent components included in the derived 
            component definition. Possible values are 1 ≤≤ *indepComponents* ≤≤ 6. Only available 
            components can be specified. The *indepComponents* argument applies only if 
            *localDependency*=ON. The default value is an empty sequence. 
        tempDependency
            A Boolean specifying whether the table data depend on temperature. The default value is 
            OFF. 
        fieldDependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A CDCTerm object. 

        Exceptions
        ----------
            ValueError and TextError. 
        """
        pass

    def setValues(self):
        """This method modifies the CDCTerm object.

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

