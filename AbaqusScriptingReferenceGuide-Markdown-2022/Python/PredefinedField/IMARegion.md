# IMARegion object

A IMARegion is an object used to define material instance name volume fractions for the [MaterialAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialassignmentpyc.htm?ContextScope=all) predefined field.

## Access

```
import load
mdb.models[name].predefinedFields[name].assignmentList
```

## Members

The IMARegion object can have the following members:

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the sub-region of the selected part instance to which the volume fractions will be applied.

- *fractionList*

  A tuple of Floats specifying the volume fractions, per material instance name. The length of the tuple corresponds to the number of material instance names, as established by the assigned Eulerian section.