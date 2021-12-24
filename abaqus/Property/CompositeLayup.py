from ..Section.GeometryShellSection import GeometryShellSection
from .MaterialOrientation import MaterialOrientation
from abaqusConstants import *

class CompositeLayup:

    """The CompositeLayup object is used to specify a composite layup on a part. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].compositeLayups[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - SHELL SECTION
        - SHELL GENERAL SECTION
        - SOLID SECTION

    """

    # A GeometryShellSection object. 
    section: GeometryShellSection = None

    # A MaterialOrientation object. 
    orientation: MaterialOrientation = None

    # A CompositePlyArray object specifying the plies that make up this composite layup. 
    plies: CompositePlyArray = None

    def __init__(self, name: str, description: str = '', offsetType: SymbolicConstant = GLOBAL, 
                 offsetField: str = '', offsetValues: float = 0, elementType: SymbolicConstant = SHELL, 
                 symmetric: Boolean = OFF):
        """This method creates a CompositeLayup object.

        Path
        ----
            - mdb.models[*name*].parts[*name*].CompositeLayup

        Parameters
        ----------
        name
            A String specifying the repository key. 
        description
            A String specifying a description of the composite layup. 
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If 
            *offsetType*=OFFSET_FIELD the *offsetField* argument is required. This member is valid 
            only if *elementType*=SHELL. Possible values are SINGLE_VALUE, MIDDLE_SURFACE, 
            TOP_SURFACE, BOTTOM_SURFACE, OFFSET_FIELD, and GLOBAL. The default value is GLOBAL. 
        offsetField
            A String specifying The name of the field specifying the offset. This member is valid 
            only if *elementType*=SHELL. The default value is an empty string. 
        offsetValues
            A Float specifying The offset of the shell section. This member is valid only if 
            *elementType*=SHELL. The default value is 0.0. 
        elementType
            A SymbolicConstant specifying the type of element in the composite layup. Possible 
            values are SHELL, CONTINUUM_SHELL, and SOLID. The default value is SHELL. 
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis. 
            The default value is OFF. 

        Returns
        -------
            A CompositeLayup object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

    def suppress(self):
        """This method suppresses a composite layup.

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

    def resume(self):
        """This method resumes a composite layup that was previously suppressed.

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

    def deletePlies(self):
        """This method deletes all of the plies from a composite layup.

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

    def setValues(self, description: str = '', offsetType: SymbolicConstant = GLOBAL, offsetField: str = '', 
                  offsetValues: float = 0, elementType: SymbolicConstant = SHELL, 
                  symmetric: Boolean = OFF):
        """This method modifies the CompositeLayup object.

        Parameters
        ----------
        description
            A String specifying a description of the composite layup. 
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If 
            *offsetType*=OFFSET_FIELD the *offsetField* argument is required. This member is valid 
            only if *elementType*=SHELL. Possible values are SINGLE_VALUE, MIDDLE_SURFACE, 
            TOP_SURFACE, BOTTOM_SURFACE, OFFSET_FIELD, and GLOBAL. The default value is GLOBAL. 
        offsetField
            A String specifying The name of the field specifying the offset. This member is valid 
            only if *elementType*=SHELL. The default value is an empty string. 
        offsetValues
            A Float specifying The offset of the shell section. This member is valid only if 
            *elementType*=SHELL. The default value is 0.0. 
        elementType
            A SymbolicConstant specifying the type of element in the composite layup. Possible 
            values are SHELL, CONTINUUM_SHELL, and SOLID. The default value is SHELL. 
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis. 
            The default value is OFF. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

