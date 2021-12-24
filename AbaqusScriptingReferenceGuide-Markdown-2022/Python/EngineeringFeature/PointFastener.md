# PointFastener object

The PointFastener object defines a point fastener.

The PointFastener object is derived from the [Fastener](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fastenerpyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.fasteners[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.fasteners[name]
```

## PointFastener(...)



This method creates a PointFastener object. Although the constructor is available both for parts and for the assembly, PointFastener objects are currently supported only under the assembly.



### Path

```
mdb.models[name].parts[name].engineeringFeatures.PointFastener
mdb.models[name].rootAssembly.engineeringFeatures.PointFastener
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which fasteners are applied.

- *physicalRadius*

  A Float specifying the physical fastener radius.

### Optional arguments

- *directionVector*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object of length 2 specifying the direction of projection. Instead of through a [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), each point may be specified through a tuple of coordinates. The default value is None.

- *targetSurfaces*

  A [RegionArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying surfaces to be fastened. The default value is MODEL.

- *ur1*

  A Boolean specifying whether to constrain rotational displacement component about the 1-direction. The default value is ON.

- *ur2*

  A Boolean specifying whether to constrain rotational displacement component about the 2-direction. The default value is ON.

- *ur3*

  A Boolean specifying whether to constrain rotational displacement component about the 3-direction. The default value is ON.

- *attachmentMethod*

  A SymbolicConstant specifying the method used to locate points for attaching fasteners. Possible values are FACETOFACE, EDGETOFACE, FACETOEDGE, and EDGETOEDGE. The default value is FACETOFACE.

- *influenceRadius*

  The SymbolicConstant DEFAULT or a Float specifying the maximum distance from the projection point on a connected surface within which the nodes on that surface must lie to contribute to the motion of the projection point. If the value is DEFAULT, a radius is computed from the fastener diameter and the surface facet lengths. The default value is DEFAULT.

- *searchRadius*

  The SymbolicConstant DEFAULT or a Float specifying the distance from the positioning points within which the connected points must lie. The default value is DEFAULT.

- *maximumLayers*

  The SymbolicConstant ALL or an Int specifying the maximum number of layers for each fastener. If the value is ALL, the maximum possible number of layers within the searchRadius will be used for each fastener. The default value is ALL.

- *coupling*

  A SymbolicConstant specifying the coupling method used to couple the displacement and rotation of each attachment point to the average motion of the surface nodes within the radius of influence from the fastener projection point. Possible values are CONTINUUM and STRUCTURAL. The default value is CONTINUUM.

- *weightingMethod*

  A SymbolicConstant specifying the weighting scheme to be used to weight the contribution of the displacements of the surface nodes within the radius of influence to the motion of the fastener projection point. UNIFORM, LINEAR, QUADRATIC, and CUBIC indicate uniform, linear decreasing, quadratic polynomial decreasing, and cubic polynomial monotonic decreasing weight distributions. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC. The default value is UNIFORM.

- *additionalMass*

  A Float specifying the mass that will be distributed to fastener attachment points. The default value is 0.0.

- *adjustOrientation*

  A Boolean specifying whether to adjust localCsys such that the local z-axis for each fastener is normal to the surface that is closest to the reference node for that fastener. The default value is ON.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system. If *localCsys*=None, the global coordinate system is used. When this member is queried, it returns an Int. The default value is None.

- *connectionType*

  A SymbolicConstant specifying the fastener connection type. Possible values are CONNECTOR and BEAM_MPC. The default value is CONNECTOR.

- *sectionName*

  A String specifying the connector section assigned to generated connectors. The default value is an empty string.

- *connectorOrientationLocalCsys1*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the first connector point in generated connectors. If *connectorOrientationLocalCsys1*=None, the degrees of freedom are defined in the global coordinate system. When this member is queried, it returns an Int. The default value is None.

- *axis1*

  A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied for the first point in generated connectors. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle1*

  A Float specifying the angle of the additional rotation for the first point in generated connectors. The default value is 0.0.

- *orient2SameAs1*

  A Boolean specifying whether or not the second connector point in generated connectors is to use the same local coordinate system, axis, and angle as the first point. The default value is ON.

- *connectorOrientationLocalCsys2*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of the second connector point in generated connectors. If *connectorOrientationLocalCsys2*=None, the degrees of freedom are defined in the global coordinate system. When this member is queried, it returns an Int. The default value is None.

- *axis2*

  A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied for the second point in generated connectors. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle2*

  A Float specifying the angle of the additional rotation for the second point in generated connectors. The default value is 0.0.

- *unsorted*

  A Boolean specifying whether the analysis product should leave targetSurfaces in the given unsorted order, or sort them by proximity to determine the connectivity of fastening points. The default value is OFF.

### Return value

A PointFastener object.

### Exceptions

None.



## setValues(...)



This method modifies the PointFastener object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PointFastener ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pointfastenerpyc.htm?ContextScope=all#simaker-pointfastenerpointfastenerpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The PointFastener object has members with the same names and descriptions as the arguments to the [PointFastener ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pointfastenerpyc.htm?ContextScope=all#simaker-pointfastenerpointfastenerpyc)method.

In addition, the PointFastener object has the following member:

- *suppressed*

  A Boolean specifying whether the fastener is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [FASTENER](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-fastener.htm?ContextScope=all#simakey-r-fastener)