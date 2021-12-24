# PlyStackPlot object

The PlyStackPlot object is used to plot the stacking of plies in a composite layup or in a composite shell section.

## Access

```
import
section import visualization
```

## MdbPlyStackPlot(...)



This method creates a PlyStackPlot object from a region of a part that contains a composite shell layup.



### Path

section.MdbPlyStackPlot

### Required arguments

- *part*

  A [Part](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object.

- *region*

  A [Region](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object which contains a composite shell layup.

### Optional arguments

None.

### Return value

A PlyStackPlot object.

### Exceptions

None.



## OdbPlyStackPlot(...)



This method creates a PlyStackPlot object from a composite shell section of an Odb object.



### Path

visualization.OdbPlyStackPlot

### Required arguments

- *odb*

  An [Odb](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?ContextScope=all) object.

- *sectionName*

  A String specifying the section name that contains a composite shell section.

### Optional arguments

- *offset*

  A Float specifying the shell offset. The default value is 0.0.

### Return value

A PlyStackPlot object.

### Exceptions

None.



## Members

The PlyStackPlot object has no members.