# SectionAssignment object

The SectionAssignment object is used to specify a section assignment on an assembly or part. Section assignments on the assembly are limited to connector elements only.

## Access

```
import section
mdb.models[name].parts[name].sectionAssignments[i]
import assembly
mdb.models[name].rootAssembly.sectionAssignments[i]
import odbAccess
session.odbs[name].parts[name].sectionAssignments[i]
session.odbs[name].rootAssembly.instances[name].sectionAssignments[i]
session.odbs[name].rootAssembly.sectionAssignments[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.sectionAssignments[i]
```

## SectionAssignment(...)



This method creates a SectionAssignment object.



### Path

mdb.models[*name*].parts[*name*].SectionAssignment

mdb.models[*name*].rootAssembly.SectionAssignment

### Required arguments

- *region*

  A [Set](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) object specifying the region to which the section is assigned.

- *sectionName*

  A String specifying the name of the section.

### Optional arguments

- *thicknessAssignment*

  A SymbolicConstant specifying section thickness assignment method. Possible values are FROM_SECTION and FROM_GEOMETRY. The default value is FROM_SECTION.

- *offset*

  A Float specifying the offset of the shell section. The default value is 0.0.

- *offsetType*

  A SymbolicConstant specifying the method used to define the shell offset. If *offsetType* is set to OFFSET_FIELD the *offsetField* must have a value. Possible values are SINGLE_VALUE, MIDDLE_SURFACE, TOP_SURFACE, BOTTOM_SURFACE, FROM_GEOMETRY, and OFFSET_FIELD. The default value is SINGLE_VALUE.

- *offsetField*

  A String specifying the name of the field specifying the offset. The default value is "".

### Return value

A SectionAssignment object.

### Exceptions

None.



## resume()



This method resumes the section assignment that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the section assignment.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## getVertices(...)



This method is only valid for connector section assignments. This method returns a sequence consisting of tuples of coordinates of the connector's endpoints.



### Arguments

None.

### Return value

A sequence of tuples of floats.

### Exceptions

- An exception is thrown if getVertices() is called on any section assignment except connector section assignment.

  This method is valid only for connector section assignments.



## setValues(...)



This method modifies the SectionAssignment object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SectionAssignment ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionassignmentpyc.htm?ContextScope=all#simaker-sectionassignmentsectionassignmentpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The SectionAssignment object has members with the same names and descriptions as the arguments to the [SectionAssignment ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionassignmentpyc.htm?ContextScope=all#simaker-sectionassignmentsectionassignmentpyc)method.

In addition, the SectionAssignment object has the following member:

- *suppressed*

  A Boolean specifying whether the section assignment is suppressed or not. The default value is OFF.