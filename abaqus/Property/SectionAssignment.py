from abaqusConstants import *
from ..Region.Set import Set


class SectionAssignment:
    """The SectionAssignment object is used to specify a section assignment on an assembly or
    part. Section assignments on the assembly are limited to connector elements only. 

    Access
    ------
        - import section
        - mdb.models[name].parts[name].sectionAssignments[i]
        - import assembly
        - mdb.models[name].rootAssembly.sectionAssignments[i]
        - import odbAccess
        - session.odbs[name].parts[name].sectionAssignments[i]
        - session.odbs[name].rootAssembly.instances[name].sectionAssignments[i]
        - session.odbs[name].rootAssembly.sectionAssignments[i]
        - session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.sectionAssignments[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Boolean specifying whether the section assignment is suppressed or not. The default 
    # value is OFF. 
    suppressed: Boolean = OFF

    def __init__(self, region: Set, sectionName: str, thicknessAssignment: SymbolicConstant = FROM_SECTION,
                 offset: float = 0, offsetType: SymbolicConstant = SINGLE_VALUE, offsetField: str = ''):
        """This method creates a SectionAssignment object.

        Path
        ----
            - mdb.models[*name*].parts[*name*].SectionAssignment
            - mdb.models[*name*].rootAssembly.SectionAssignment

        Parameters
        ----------
        region
            A Set object specifying the region to which the section is assigned. 
        sectionName
            A String specifying the name of the section. 
        thicknessAssignment
            A SymbolicConstant specifying section thickness assignment method. Possible values are 
            FROM_SECTION and FROM_GEOMETRY. The default value is FROM_SECTION. 
        offset
            A Float specifying the offset of the shell section. The default value is 0.0. 
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If 
            *offsetType* is set to OFFSET_FIELD the *offsetField* must have a value. Possible values 
            are SINGLE_VALUE, MIDDLE_SURFACE, TOP_SURFACE, BOTTOM_SURFACE, FROM_GEOMETRY, and 
            OFFSET_FIELD. The default value is SINGLE_VALUE. 
        offsetField
            A String specifying the name of the field specifying the offset. The default value is 
            "". 

        Returns
        -------
            A SectionAssignment object. . 
        """
        pass

    def resume(self):
        """This method resumes the section assignment that was previously suppressed.

        Parameters
        ----------
        """
        pass

    def suppress(self):
        """This method suppresses the section assignment.

        Parameters
        ----------
        """
        pass

    def getVertices(self):
        """This method is only valid for connector section assignments. This method returns a
        sequence consisting of tuples of coordinates of the connector's endpoints.

        Parameters
        ----------

        Returns
        -------
            A sequence of tuples of floats. 

        Exceptions
        ----------
            - An exception is thrown if getVertices() is called on any section assignment except 
            connector section assignment. 
              This method is valid only for connector section assignments. 
        """
        pass

    def setValues(self):
        """This method modifies the SectionAssignment object.

        Parameters
        ----------
        """
        pass
