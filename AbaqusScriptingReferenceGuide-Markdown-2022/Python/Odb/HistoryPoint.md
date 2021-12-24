# HistoryPoint object

The HistoryPoint object specifies the point at which history data will be collected. The HistoryPoint object is a temporary object used as an argument to the HistoryRegion method.

## Access

```
import odbAccess
session.odbs[name].steps[name].historyRegions[name].point
```

## HistoryPoint(...)



This method creates a HistoryPoint object for a node.



### Path

```
odbAccess.HistoryPoint
```

### Required arguments

- *node*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object specifying the node for which the data are to be collected.

### Optional arguments

None.

### Return value

A HistoryPoint object.

### Exceptions

None.

## HistoryPoint(...)



This method creates a HistoryPoint object for an element.



### Path

```
odbAccess.HistoryPoint
```

### Required arguments

- *element*

  An [OdbMeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) object specifying the element for which the data are to be collected.

### Optional arguments

- *ipNumber*

  An Int specifying the integration point. This argument is used to define a history output position of INTEGRATION_POINT or ELEMENT_FACE_INTEGRATION_POINT. The default value is 0.

- *sectionPoint*

  A [SectionPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?ContextScope=all) object.

- *face*

  A SymbolicConstant specifying the element face. This argument is used to define a history output position of ELEMENT_FACE or ELEMENT_FACE_INTEGRATION_POINT. Possible values are:

  - FACE_UNKOWN, specifying this value indicates that no value has been specified.
  - FACE1, specifying this value indicates that element face 1 has been specified.
  - FACE2, specifying this value indicates that element face 2 has been specified.
  - FACE3, specifying this value indicates that element face 3 has been specified.
  - FACE4, specifying this value indicates that element face 4 has been specified.
  - FACE5, specifying this value indicates that element face 5 has been specified.
  - FACE6, specifying this value indicates that element face 6 has been specified.
  - SIDE1, specifying this value indicates that element side 1 has been specified.
  - SIDE2, specifying this value indicates element side 2 has been specified.
  - END1, specifying this value indicates that element end 1 has been specified.
  - END2, specifying this value indicates that element end 2 has been specified.
  - END3, specifying this value indicates that element end 3 has been specified.

  The default value is FACE_UNKNOWN.

- *node*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object specifying the node for which the data are to be collected.

### Return value

A HistoryPoint object.

### Exceptions

None.

## HistoryPoint(...)



This method creates a HistoryPoint object for a region.



### Path

```
odbAccess.HistoryPoint
```

### Required arguments

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the region for which the data are to be collected.

### Optional arguments

None.

### Return value

A HistoryPoint object.

### Exceptions

None.

## HistoryPoint(...)



This method creates a HistoryPoint object for the [OdbAssembly](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbassemblypyc.htm?ContextScope=all) object.



### Path

```
odbAccess.HistoryPoint
```

### Required arguments

- *assembly*

  An [OdbAssembly](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbassemblypyc.htm?ContextScope=all) object specifying the assembly for which the data are to be collected.

### Optional arguments

None.

### Return value

A HistoryPoint object.

### Exceptions

None.

## HistoryPoint(...)



This method creates a HistoryPoint object for the [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) object.



### Path

```
odbAccess.HistoryPoint
```

### Required arguments

- *instance*

  An [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) object specifying the instance for which the data are to be collected.

### Optional arguments

None.

### Return value

A HistoryPoint object.

### Exceptions

None.



## Members

The HistoryPoint object has members with the same names and descriptions as the arguments to the [HistoryPoint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historypointpyc.htm?ContextScope=all#simaker-historypointhistorypointpyc)method.

In addition, the HistoryPoint object can have the following members:

- *ipNumber*

  An Int specifying the integration point. This argument is used to define a history output position of INTEGRATION_POINT or ELEMENT_FACE_INTEGRATION_POINT. The default value is 0.

- *face*

  A SymbolicConstant specifying the element face. This argument is used to define a history output position of ELEMENT_FACE or ELEMENT_FACE_INTEGRATION_POINT. Possible values are:

  - FACE_UNKOWN, specifying this value indicates that no value has been specified.
  - FACE1, specifying this value indicates that element face 1 has been specified.
  - FACE2, specifying this value indicates that element face 2 has been specified.
  - FACE3, specifying this value indicates that element face 3 has been specified.
  - FACE4, specifying this value indicates that element face 4 has been specified.
  - FACE5, specifying this value indicates that element face 5 has been specified.
  - FACE6, specifying this value indicates that element face 6 has been specified.
  - SIDE1, specifying this value indicates that element side 1 has been specified.
  - SIDE2, specifying this value indicates element side 2 has been specified.
  - END1, specifying this value indicates that element end 1 has been specified.
  - END2, specifying this value indicates that element end 2 has been specified.
  - END3, specifying this value indicates that element end 3 has been specified.

  The default value is FACE_UNKNOWN.

- *position*

  A SymbolicConstant specifying the result position of the history point. Possible values are:

  - NODAL, specifying the values calculated at the nodes.
  - ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at the integration points.
  - INTEGRATION_POINT, specifying the values calculated at the integration points.
  - ELEMENT_FACE, specifying the results obtained for surface variables such as cavity radiation that are defined for the surface facets of an element.
  - ELEMENT_FACE_INTEGRATION_POINT, specifying the results obtained for surface variables such as cavity radiation that are defined for the surface facets of an element when the surface facets have integration points.
  - WHOLE_ELEMENT, specifying the results obtained for whole element variables.
  - WHOLE_REGION, specifying the results for an entire region of the model.
  - WHOLE_PART_INSTANCE, specifying the results for an entire part instance of the model.
  - WHOLE_MODEL, specifying the results for the entire model.

- *element*

  An [OdbMeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) object specifying the element for which the data are to be collected.

- *sectionPoint*

  A [SectionPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?ContextScope=all) object.

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the region for which the data are to be collected.

- *assembly*

  An [OdbAssembly](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbassemblypyc.htm?ContextScope=all) object specifying the assembly for which the data are to be collected.

- *instance*

  An [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) object specifying the instance for which the data are to be collected.