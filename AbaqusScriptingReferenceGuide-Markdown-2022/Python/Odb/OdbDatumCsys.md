# OdbDatumCsys object

The OdbDatumCsys object contains a coordinate system that can be stored in an output database. You can create the datum coordinate system in the Visualization module during an Abaqus/CAE session and save the datum coordinate system to the output database before you exit Abaqus/CAE. Alternatively, the analysis code can write the datum coordinate system to the output database.

## Access

```
import odbAccess
session.odbs[name].rootAssembly.datumCsyses[name]
```

## DatumCsysByThreePoints(...)



This method creates an OdbDatumCsys object using three points. A datum coordinate system created with this method results in a fixed system.



### Path

```
session.odbs[name].rootAssembly.DatumCsysByThreePoints
```

### Required arguments

- *name*

  A String specifying the repository key.

- *coordSysType*

  A SymbolicConstant specifying the type of coordinate system. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL.

- *origin*

  A sequence of Floats specifying the coordinates of the origin of the datum coordinate system.

- *point1*

  A sequence of Floats specifying the coordinates of a point on the local 1- or rr-axis.

- *point2*

  A sequence of Floats specifying the coordinates of a point in the 1–2 or rr–θθ plane.

### Optional arguments

None.

### Return value

An OdbDatumCsys object.

### Exceptions

None.



## DatumCsysByThreeNodes(...)



This method creates an OdbDatumCsys object using the coordinates of three [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) objects. A datum coordinate system created with this method results in a system that follows the position of the three nodes. Results, such as those for displacement, are resolved into the orientation of the datum coordinate system without regard to the position of its origin. The last three arguments are given in the form of an [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object.



### Path

```
session.odbs[name].rootAssembly.DatumCsysByThreeNodes
```

### Required arguments

- *name*

  A String specifying the repository key.

- *coordSysType*

  A SymbolicConstant specifying the type of coordinate system. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL.

- *origin*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object specifying a node at the origin of the datum coordinate system.

- *point1*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object specifying a node on the local 1- or rr-axis.

- *point2*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object specifying a node in the 1–2 or rr–θθ plane.

### Optional arguments

None.

### Return value

An OdbDatumCsys object.

### Exceptions

None.



## DatumCsysByThreeCircNodes(...)



This method is convenient to use where there are no nodes along the axis of a hollow cylinder or at the center of a hollow sphere. The three nodes that you provide as arguments determine a circle in space. The center of the circle is the origin of the datum coordinate system. The normal to the circle is parallel to the zz-axis of a cylindrical coordinate system or to the ϕϕ-axis of a spherical coordinate system. The line from the origin to the first node defines the rr-axis.



### Path

```
session.odbs[name].rootAssembly.DatumCsysByThreeCircNodes
```

### Required arguments

- *name*

  A String specifying the repository key.

- *coordSysType*

  A SymbolicConstant specifying the type of coordinate system. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL.

- *node1Arc*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object that lies on the circular arc.

- *node2Arc*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object that lies on the circular arc.

- *node3Arc*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object that lies on the circular arc.

### Optional arguments

None.

### Return value

An OdbDatumCsys object.

### Exceptions

None.



## DatumCsysBy6dofNode(...)



A datum coordinate system created with this method results in a system that follows the position of a node. The node location defines the origin of the datum coordinate system. The rotational displacement (UR1, UR2, UR3) of the node defines the orientation of the coordinate system axes. Results, such as those for displacement, are resolved into the orientation of the datum coordinate system without regard to the position of its origin. The last argument is given in the form of an [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object.



### Path

```
session.odbs[name].rootAssembly.DatumCsysBy6dofNode
```

### Required arguments

- *name*

  A String specifying the repository key.

- *coordSysType*

  A SymbolicConstant specifying the type of coordinate system. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL.

- *origin*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object specifying the origin of the datum coordinate system.

### Optional arguments

None.

### Return value

An OdbDatumCsys object.

### Exceptions

None.



## DatumCsys(...)



This method copies oneOdbDatumCsys object to a new OdbDatumCsys object.



### Path

```
session.odbs[name].rootAssembly.DatumCsys
```

### Required arguments

- *name*

  A String specifying the repository key.

- *datumCsys*

  An OdbDatumCsys object specifying the object to be copied.

### Optional arguments

None.

### Return value

An OdbDatumCsys object.

### Exceptions

None.



## Members

The OdbDatumCsys object has the following members:

- *name*

  A String specifying the repository key.

- *coordSysType*

  A SymbolicConstant specifying the type of coordinate system. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL.

- *origin*

  A tuple of Floats specifying the coordinates of the origin of the datum coordinate system.

- *xAxis*

  A tuple of Floats specifying a point on the *X*-axis.

- *yAxis*

  A tuple of Floats specifying a point on the *Y*-axis.

- *zAxis*

  A tuple of Floats specifying a point on the *Z*-axis.