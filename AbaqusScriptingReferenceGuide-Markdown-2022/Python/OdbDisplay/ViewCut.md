# ViewCut object

The ViewCut object is used to store values and attributes associate with ViewCut type objects. ViewCut objects can be created using the methods described below. The methods accessed via the [OdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdisplaypyc.htm?ContextScope=all) object cause the ViewCut object to be added to the session.viewports[name].odbDisplay.viewCuts repository.

## Access

```
import visualization
session.viewports[name].layers[name].odbDisplay.viewCuts[name]
session.viewports[name].odbDisplay.viewCuts[name]
```

## ViewCut(...)



This method creates a ViewCut object.



### Path

```
session.viewports[name].layers[name].odbDisplay.ViewCut
session.viewports[name].odbDisplay.ViewCut
```

### Required arguments

- *name*

  A String specifying the repository key.

- *shape*

  A SymbolicConstant specifying the shape of the ViewCut object. Possible values are PLANE, CYLINDER, SPHERE, and ISOSURFACE.

- *origin*

  A sequence of three Floats specifying the X-, Y-, and Z-coordinates of the origin of the plane, cylinder or sphere cut. This origin is not required if the cut shape is ISOSURFACE or if the cut is defined by the *csysName* argument.

- *normal*

  A sequence of Floats specifying the X-, Y-, and Z-coordinates of the normal axis to the plane defining the cut, when the plane is defined using the *origin* argument or a SymbolicConstant defining this normal axis, when the cut is defined by the *csysName* argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is not required if the cut *shape* is CYLINDER, SPHERE or ISOSURFACE.

- *axis2*

  A sequence of three Floats specifying the X-, Y-, and Z-coordinates of the second axis of the plane defining the cut, when the plane is defined using the *origin* argument or a SymbolicConstant defining this second axis, when the cut is defined by the *csysName* argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is used to rotate the plane cut. It is not required if the cut *shape* is CYLINDER, SPHERE or ISOSURFACE.

- *csysName*

  A String specifying the name of the [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object to be used to define the cut. This name is not required if the cut *shape* is ISOSURFACE or if the cut is defined by the *origin* argument.

- *cylinderAxis*

  A sequence of Floats specifying the X-, Y-, and Z-coordinates of the cylinder axis defining the cut, when the cut is defined using the *origin* argument or a SymbolicConstant defining this cylinder axis, when the cut is defined by the *csysName* argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is not required if the cut *shape* is PLANE, SPHERE, or ISOSURFACE.

### Optional arguments

- *followDeformation*

  A Boolean specifying whether the cut will follow the deformation or be static. The default value is OFF.

- *overrideAveraging*

  A Boolean specifying averaging for element based fields associated with isosurface cuts will be set to compute-average with a threshold of 100% when true. The current field options will be used when false. The default value is ON.

- *referenceFrame*

  A SymbolicConstant specifying which reference frame will be used when the cut follows the deformation. Possible values are FIRST_FRAME, LAST_FRAME, and CURRENT_FRAME. The default value is FIRST_FRAME.

### Return value

A ViewCut object.

### Exceptions

None.



## setValues(...)



This method modifies the ViewCut object.



### Required arguments

None.

### Optional arguments

At least one of the following must be provided:

- *angle*

  A Float specifying the rotation angle of the cut defined with a *shape* set to PLANE.

- *motion*

  A SymbolicConstant specifying the type of motion for the cut defined with a *shape* set to PLANE. Possible values are TRANSLATE and ROTATE. The default value is TRANSLATE.

- *position*

  A Float specifying the position of the cut defined with a *shape* set to PLANE.

- *radius*

  A Float specifying the radius of the cut defined with a *shape* set to CYLINDER or SPHERE.

- *rotationAxis*

  A SymbolicConstant specifying the rotation axis for the cut defined with a *shape* set to PLANE. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_2.

- *value*

  A Float specifying the value of the cut defined with a *shape* set to ISOSURFACE.

- *showModelAboveCut*

  A Boolean specifying whether to display the model above the cut. The default value is OFF.

- *showModelOnCut*

  A Boolean specifying whether to display the model on the cut. The default value is ON.

- *showModelBelowCut*

  A Boolean specifying whether to display the model below the cut. The default value is ON.

- *showFreeBodyCut*

  A Boolean specifying whether to display the free body cut. The default value is OFF.

- *csysName*

  A String specifying the name of the [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object to be used to define the cut. This name is not required if the cut *shape* is ISOSURFACE or if the cut is defined by the *origin* argument.

- *origin*

  A sequence of three Floats specifying the X-, Y-, and Z-coordinates of the origin of the plane, cylinder or sphere cut. This origin is not required if the cut shape is ISOSURFACE or if the cut is defined by the *csysName* argument.

- *normal*

  A sequence of Floats specifying the X-, Y-, and Z-coordinates of the normal axis to the plane defining the cut, when the plane is defined using the *origin* argument or a SymbolicConstant defining this normal axis, when the cut is defined by the *csysName* argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is not required if the cut *shape* is CYLINDER, SPHERE or ISOSURFACE.

- *axis2*

  A sequence of three Floats specifying the X-, Y-, and Z-coordinates of the second axis of the plane defining the cut, when the plane is defined using the *origin* argument or a SymbolicConstant defining this second axis, when the cut is defined by the *csysName* argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is used to rotate the plane cut. It is not required if the cut *shape* is CYLINDER, SPHERE or ISOSURFACE.

- *cylinderAxis*

  A sequence of Floats specifying the X-, Y-, and Z-coordinates of the cylinder axis defining the cut, when the cut is defined using the *origin* argument or a SymbolicConstant defining this cylinder axis, when the cut is defined by the *csysName* argument. Possible values are AXIS_1, AXIS_2, AXIS_3. This axis is not required if the cut *shape* is PLANE, SPHERE, or ISOSURFACE.

- *followDeformation*

  A Boolean specifying whether the cut will follow the deformation or be static. The default value is OFF.

- *overrideAveraging*

  A Boolean specifying averaging for element based fields associated with isosurface cuts will be set to compute-average with a threshold of 100% when true. The current field options will be used when false. The default value is ON.

- *referenceFrame*

  A SymbolicConstant specifying which reference frame will be used when the cut follows the deformation. Possible values are FIRST_FRAME, LAST_FRAME, and CURRENT_FRAME. The default value is FIRST_FRAME.

### Return value

None.

### Exceptions

None.



## updateVariable()



This method updates the field associated with an isosurface cut to be consistent with the current primary variable.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The ViewCut object has members with the same names and descriptions as the arguments to the [ViewCut ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewcutpyc.htm?ContextScope=all#simaker-viewcutviewcutpyc)method.

In addition, the ViewCut object has the following members:

- *angle*

  A Float specifying the rotation angle of the cut defined with a *shape* set to PLANE.

- *motion*

  A SymbolicConstant specifying the type of motion for the cut defined with a *shape* set to PLANE. Possible values are TRANSLATE and ROTATE. The default value is TRANSLATE.

- *position*

  A Float specifying the position of the cut defined with a *shape* set to PLANE.

- *radius*

  A Float specifying the radius of the cut defined with a *shape* set to CYLINDER or SPHERE.

- *rotationAxis*

  A SymbolicConstant specifying the rotation axis for the cut defined with a *shape* set to PLANE. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_2.

- *value*

  A Float specifying the value of the cut defined with a *shape* set to ISOSURFACE.

- *showModelAboveCut*

  A Boolean specifying whether to display the model above the cut. The default value is OFF.

- *showModelOnCut*

  A Boolean specifying whether to display the model on the cut. The default value is ON.

- *showModelBelowCut*

  A Boolean specifying whether to display the model below the cut. The default value is ON.

- *showFreeBodyCut*

  A Boolean specifying whether to display the free body cut. The default value is OFF.

- *active*

  A Boolean specifying whether the cut is displayed.

- *cutRange*

  A pair of Floats specifying the acceptable range for positioning the cut.

- *crossSectionalArea*

  A Float returning the cross-sectional area of the cut when *showFreeBodyCut* is set to ON.