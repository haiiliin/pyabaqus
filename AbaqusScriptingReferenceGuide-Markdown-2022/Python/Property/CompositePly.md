# CompositePly object

The CompositePly object defines the material layers in a composite layup.

## Access

```
import section
mdb.models[name].parts[name].compositeLayups[i].plies[i]
```

## CompositePly(...)



This method creates a CompositePly object.



### Path

mdb.models[*name*].parts[*name*].compositeLayups[*name*].CompositePly

### Required arguments

- *thickness*

  A Float specifying the thickness of the section layer.

- *region*

  A [Region](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the composite ply applies.

- *material*

  A String specifying the name of the material for the ply.

- *plyName*

  A String specifying the ply identifier for this section layer. The default value is an empty string.

- *orientationType*

  A SymbolicConstant specifying the method used to define the relative orientation. If *orientationType*=SPECIFY_ORIENT the *orientationValue* argument is required. If *orientationType*=CSYS the *orientation* argument is required. Possible values are CSYS, SPECIFY_ORIENT, ANGLE_0, ANGLE_45, ANGLE_90, and ANGLE_NEG45. The default value is ANGLE_0.

- *thicknessType*

  A SymbolicConstant specifying the method used to define the thickness. If *thicknessType*=SPECIFY_THICKNESS, the *thickness* argument is required. Possible values are SPECIFY_THICKNESS, FIELD_THICKNESS, and ANALYTICAL_FIELD_THICKNESS. The default value is SPECIFY_THICKNESS.

### Optional arguments

- *orientationValue*

  A Float specifying the relative orientation of the section layer. The default value is 0.0.

- *thicknessField*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) or [DiscreteField](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all) object used to define the thickness of the shell elements and composite ply. The *thicknessField* argument applies when *thicknessType*=ANALYTICAL_FIELD or *thicknessType*=DISCRETE_FIELD for shell elements and *thicknessType*=FIELD_THICKNESS or *thicknessType*=ANALYTICAL_FIELD_THICKNESS for composite ply. The default value is an empty string.

- *numIntPts*

  An Int specifying the number of integration points to be used through the section layer. This argument is valid only if *preIntegrate*=OFF. The default value is 3.

- *axis*

  A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied. For shells this axis is also the shell normal. The *axis* argument applies only if a valid reference is provided for the *orientation*. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.

- *angle*

  A Float specifying the angle of the additional rotation. The *angle* argument applies only if a valid reference is provided for the *orientation*. The default value is 0.0.

- *additionalRotationType*

  A SymbolicConstant specifying the method used to describe the additional rotation when a valid orientation is specified. Use *orientationType*=ANGLE_0 and *additionalRotationType*=ROTATION_FIELD to specify a discrete field of rotations for this CompositePly. Possible values are ROTATION_NONE, ROTATION_ANGLE, and ROTATION_FIELD. The default value is ROTATION_NONE.

- *orientation*

  The SymbolicConstant None or a [DatumCsys](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying a coordinate system reference for the relative orientation of this layer. The default value is None.

- *additionalRotationField*

  A String specifying the name of the field specifying the additional rotation. The default value is an empty string.

### Return value

A CompositePly object.

### Exceptions

AbaqusException.



## Members

The CompositePly object has members with the same names and descriptions as the arguments to the [CompositePly](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositeplypyc.htm?ContextScope=all#simaker-compositeplycompositeplypyc) method.