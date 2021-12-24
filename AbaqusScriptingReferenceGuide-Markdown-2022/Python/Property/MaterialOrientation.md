# MaterialOrientation object

The MaterialOrientation object represents the orientation of the material properties and composite layups.

## Access

```
import section
mdb.models[name].parts[name].compositeLayups[i].orientation
mdb.models[name].parts[name].materialOrientations[i]
import odbAccess
session.odbs[name].parts[name].materialOrientations[i]
session.odbs[name].rootAssembly.instances[name]\
.materialOrientations[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.materialOrientations[i]
```

## MaterialOrientation(...)



This method creates a MaterialOrientation object.



### Path

mdb.models[*name*].parts[*name*].MaterialOrientation

### Required arguments

None.

### Optional arguments

- *region*

  A [Set](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) object specifying a region for which the material orientation is defined.

- *localCsys*

  A [DatumCsys](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system or None, describing the material orientation for the given region. In the ODB, this member was previously accessible using "csys," but support has now been added for localCsys and the csys member will be deprecated.

- *axis*

  A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied. For shells this axis is also the shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle*

  A Float specifying the angle of the additional rotation (if accessed from the ODB instead of the MDB, it will be a string instead of a float). The default value is 0.0.

- *stackDirection*

  A SymbolicConstant specifying the stack or thickness direction. Possible values are STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is STACK_3.

- *fieldName*

  A String specifying the name of the [DiscreteField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object specifying the orientation. The default value is an empty string.

- *orientationType*

  A SymbolicConstant specifying the method used to define the material orientation. If *orientationType*=SYSTEM, the *region* and *localCsys* arguments are required. If *orientationType*=FIELD, the *fieldName* argument is required. Possible values are GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.

- *normalAxisDirection*

  A SymbolicConstant specifying the axis that is defined by the normal axis direction for a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_3.

- *normalAxisDefinition*

  A SymbolicConstant specifying the method used to define the normal axis direction for a discrete orientation. Possible values are SURFACE, NORMAL_DATUM, and NORMAL_VECTOR. The default value is NORMAL_VECTOR.

- *normalAxisRegion*

  A [Surface](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacepyc.htm?ContextScope=all) object specifying a region whose geometric normals define the normal axis for the discrete orientation.

- *normalAxisDatum*

  A [DatumAxis](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the Datum Axis or None, describing the normal axis direction for the discrete orientation.

- *flipNormalDirection*

  A Boolean specifying the flag to reverse the direction of the defined normal axis direction. The default value is OFF.

- *normalAxisVector*

  A sequence of Floats specifying the vector that defines the direction of the normal axis of the discrete orientation.

- *primaryAxisDirection*

  A SymbolicConstant specifying the axis that is defined by the primary axis direction for a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *primaryAxisDefinition*

  A SymbolicConstant specifying the method used to define the primary axis direction for a discrete orientation. Possible values are SURFACE, PRIMARY_DATUM, and PRIMARY_VECTOR. The default value is PRIMARY_VECTOR.

- *primaryAxisRegion*

  A [Set](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) object specifying a region whose geometric tangents define the primary axis for the discrete orientation.

- *primaryAxisDatum*

  A [DatumAxis](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the Datum Axis or None, describing the primary axis direction for the discrete orientation.

- *flipPrimaryDirection*

  A Boolean specifying the flag to reverse the direction of the defined primary axis direction. The default value is OFF.

- *primaryAxisVector*

  A sequence of Floats specifying the vector that defines the direction of the primary axis of the discrete orientation.

### Return value

A MaterialOrientation object.

### Exceptions

None.



## ReferenceOrientation(...)



This method creates a MaterialOrientation object.



### Path

mdb.models[*name*].parts[*name*].compositeLayups[*name*].ReferenceOrientation

### Required arguments

None.

### Optional arguments

- *localCsys*

  A [DatumCsys](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system or None, describing the material orientation for the given region. In the ODB, this member was previously accessible using "csys," but support has now been added for localCsys and the csys member will be deprecated.

- *axis*

  A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied. For shells this axis is also the shell normal. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle*

  A Float specifying the angle of the additional rotation (if accessed from the ODB instead of the MDB, it will be a string instead of a float). The default value is 0.0.

- *stackDirection*

  A SymbolicConstant specifying the stack or thickness direction. Possible values are STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is STACK_3.

- *fieldName*

  A String specifying the name of the [DiscreteField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object specifying the orientation. The default value is an empty string.

- *orientationType*

  A SymbolicConstant specifying the method used to define the material orientation. If *orientationType*=SYSTEM, the *region* and *localCsys* arguments are required. If *orientationType*=FIELD, the *fieldName* argument is required. Possible values are GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.

- *additionalRotationField*

  A String specifying the name of the [DiscreteField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object specifying the additional rotation. The default value is an empty string.

- *additionalRotationType*

  A SymbolicConstant specifying the method used to describe the additional rotation when a valid orientation is specified. Possible values are ROTATION_NONE, ROTATION_ANGLE, and ROTATION_FIELD. The default value is ROTATION_NONE.

- *normalAxisDirection*

  A SymbolicConstant specifying the axis that is defined by the normal axis direction for a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_3.

- *normalAxisDefinition*

  A SymbolicConstant specifying the method used to define the normal axis direction for a discrete orientation. Possible values are SURFACE, DATUM, and VECTOR. The default value is VECTOR.

- *normalAxisRegion*

  A [Surface](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacepyc.htm?ContextScope=all) object specifying a region whose geometric normals define the normal axis for the discrete orientation.

- *normalAxisDatum*

  A [DatumAxis](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the Datum Axis or None, describing the normal axis direction for the discrete orientation.

- *flipNormalDirection*

  A Boolean specifying the flag to reverse the direction of the defined normal axis direction. The default value is OFF.

- *normalAxisVector*

  A sequence of Floats specifying the vector that defines the direction of the normal axis of the discrete orientation.

- *primaryAxisDirection*

  A SymbolicConstant specifying the axis that is defined by the primary axis direction for a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *primaryAxisDefinition*

  A SymbolicConstant specifying the method used to define the primary axis direction for a discrete orientation. Possible values are EDGE, DATUM, and VECTOR. The default value is VECTOR.

- *primaryAxisRegion*

  A [Set](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) object specifying a region whose geometric tangents define the primary axis for the discrete orientation.

- *primaryAxisDatum*

  A [DatumAxis](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the Datum Axis or None, describing the primary axis direction for the discrete orientation.

- *flipPrimaryDirection*

  A Boolean specifying the flag to reverse the direction of the defined primary axis direction. The default value is OFF.

- *primaryAxisVector*

  A sequence of Floats specifying the vector that defines the direction of the primary axis of the discrete orientation.

### Return value

A MaterialOrientation object.

### Exceptions

None.



## setValues(...)



This method modifies the MaterialOrientation object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [MaterialOrientation ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialorientationpyc.htm?ContextScope=all#simaker-materialorientationmaterialorientationpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The MaterialOrientation object has members with the same names and descriptions as the arguments to the [MaterialOrientation ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialorientationpyc.htm?ContextScope=all#simaker-materialorientationmaterialorientationpyc)method.

In addition, the MaterialOrientation object can have the following members:

- *additionalRotationType*

  A SymbolicConstant specifying the method used to describe the additional rotation when a valid orientation is specified. Possible values are ROTATION_NONE, ROTATION_ANGLE, and ROTATION_FIELD. The default value is ROTATION_NONE.

- *additionalRotationField*

  A String specifying the name of the [DiscreteField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object specifying the additional rotation. The default value is an empty string.