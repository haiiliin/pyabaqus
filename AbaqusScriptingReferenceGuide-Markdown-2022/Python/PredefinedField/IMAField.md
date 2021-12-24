# IMAField object

A IMAField is an object used to define material instance name volume fractions for the [MaterialAssignment](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialassignmentpyc.htm?ContextScope=all) predefined field.

## Access

```
import load
mdb.models[name].predefinedFields[name].fieldList
```

## Members

The IMAField object can have the following members:

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the sub-region of the selected part instance to which the volume fractions will be applied.

- *discFieldList*

  A tuple of Strings specifying the name of the discrete fields that contain the volume fraction data. The length of the tuple corresponds to the number of material instance names, as established by the assigned Eulerian section.