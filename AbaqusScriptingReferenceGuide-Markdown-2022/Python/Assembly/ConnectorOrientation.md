# ConnectorOrientation object

The ConnectorOrientation object is used to assign a connector orientation to a connector.

## Access

```
import assembly
mdb.models[name].rootAssembly.connectorOrientations[i]
import odbAccess
session.odbs[name].rootAssembly.connectorOrientations[i]
```

## ConnectorOrientation(...)



This method creates a ConnectorOrientation object.



### Path

```
mdb.models[name].rootAssembly.ConnectorOrientation
session.odbs[name].rootAssembly.ConnectorOrientation
```

### Required arguments

- *region*

  A [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) object specifying the region to which the orientation is assigned.

### Optional arguments

- *localCsys1*

  A [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the first connector point. This value may be None, indicating the global coordinate system.

- *axis1*

  A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle1*

  A Float specifying the angle of the additional rotation. The default value is 0.0.

- *orient2sameAs1*

  A Boolean specifying whether or not the second connector point is to use the same local coordinate system, axis, and angle as the first point. The default value is ON.

- *localCsys2*

  A [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the second connector point. This value may be None, indicating the global coordinate system.

- *axis2*

  A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle2*

  A Float specifying the angle of the additional rotation. The default value is 0.0.

### Return value

A ConnectorOrientation object.

### Exceptions

None.



## setValues(...)



This method modifies the ConnectorOrientation object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorOrientation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectororientationpyc.htm?ContextScope=all#simaker-connectororientationconnectororientationpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The ConnectorOrientation object has members with the same names and descriptions as the arguments to the [ConnectorOrientation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectororientationpyc.htm?ContextScope=all#simaker-connectororientationconnectororientationpyc)method.