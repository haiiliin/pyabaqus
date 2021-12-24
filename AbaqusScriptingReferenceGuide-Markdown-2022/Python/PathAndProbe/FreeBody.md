# FreeBody object

The FreeBody object defines a section across which resultant forces and moments are computed.

## Access

```
import visualization
session.freeBodies[name]
```

## FreeBodyFromEdges(...)



This method creates a FreeBody object and places it in the freeBodies repository.



### Path

```
session.FreeBodyFromEdges
```

### Required arguments

- *name*

  A string name for the free body.

- *edges*

  A [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) leaf object that specifies the physical constituents of the free body.

### Optional arguments

- *summationLoc*

  A SymbolicConstant specifying the location of the summation point. Possible values are CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID.

- *summationPoint*

  A tuple of 3 floats specifying the summation point.

- *componentResolution*

  A SymbolicConstant specifying the component resolution. Possible values are NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.

- *csysName*

  A string specifying the name of the coordinate system.

### Return value

A FreeBody object.

### Exceptions

None.



## FreeBodyFromFaces(...)



This method creates a FreeBody object and places it in the freeBodies repository.



### Path

```
session.FreeBodyFromFaces
```

### Required arguments

- *name*

  A string name for the free body.

- *faces*

  A [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) leaf object that specifies the physical constituents of the free body.

### Optional arguments

- *summationLoc*

  A SymbolicConstant specifying the location of the summation point. Possible values are CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID.

- *summationPoint*

  A tuple of 3 floats specifying the summation point.

- *componentResolution*

  A SymbolicConstant specifying the component resolution. Possible values are NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.

- *csysName*

  A string specifying the name of the coordinate system.

### Return value

A FreeBody object.

### Exceptions

None.



## FreeBodyFromNodesElements(...)



This method creates a FreeBody object and places it in the freeBodies repository.



### Path

```
session.FreeBodyFromNodesElements
```

### Required arguments

- *name*

  A string name for the free body.

- *elements*

  A [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) leaf object that specifies the physical constituents of the free body.

- *nodes*

  A [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) leaf object that specifies the physical constituents of the free body.

### Optional arguments

- *summationLoc*

  A SymbolicConstant specifying the location of the summation point. Possible values are CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID.

- *summationPoint*

  A tuple of 3 floats specifying the summation point.

- *componentResolution*

  A SymbolicConstant specifying the component resolution. Possible values are NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.

- *csysName*

  A string specifying the name of the coordinate system.

### Return value

A FreeBody object.

### Exceptions

None.



## Members

The FreeBody object has no members.