# GeometricRestrictionDisplayOptions object

The GeometricRestrictionDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when

```
session.viewports[name].assemblyDisplay.geometricRestrictions=ON
```

The GeometricRestrictionDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.

## Access

```
session.viewports[name].assemblyDisplay.geometricRestrictionOptions
session.viewports[name].layers[name].assemblyDisplay\
.geometricRestrictionOptions
```

## setValues(...)



This method modifies the GeometricRestrictionDisplayOptions object.



### Required arguments

None.

### Optional arguments

- *drillControl*

  A Boolean specifying whether drill control geometric restriction symbols are shown. The default value is ON.

- *fixedRegion*

  A Boolean specifying whether fixed region geometric restriction symbols are shown. The default value is ON.

- *frozenArea*

  A Boolean specifying whether frozen area geometric restriction symbols are shown. The default value is ON.

- *growth*

  A Boolean specifying whether growth geometric restriction symbols are shown. The default value is ON.

- *penetrationCheck*

  A Boolean specifying whether penetration check geometric restriction symbols are shown. The default value is ON.

- *shapeDemoldControl*

  A Boolean specifying whether demold control (shape) geometric restriction symbols are shown. The default value is ON.

- *designDirection*

  A Boolean specifying whether design direction geometric restriction symbols are shown. The default value is ON.

- *shapeMemberSize*

  A Boolean specifying whether member size (shape) geometric restriction symbols are shown. The default value is ON.

- *shapePlanarSymmetry*

  A Boolean specifying whether planar symmetry (shape) geometric restriction symbols are shown. The default value is ON.

- *shapePointSymmetry*

  A Boolean specifying whether point symmetry (shape) geometric restriction symbols are shown. The default value is ON.

- *shapeRotationalSymmetry*

  A Boolean specifying whether rotational symmetry (shape) geometric restriction symbols are shown. The default value is ON.

- *stampControl*

  A Boolean specifying whether stamp control geometric restriction symbols are shown. The default value is ON.

- *slideRegionControl*

  A Boolean specifying whether slide region control geometric restriction symbols are shown. The default value is ON.

- *topologyCyclicSymmetry*

  A Boolean specifying whether cyclic symmetry geometric restriction symbols are shown. The default value is ON.

- *topologyDemoldControl*

  A Boolean specifying whether demold control (topology) geometric restriction symbols are shown. The default value is ON.

- *topologyMemberSize*

  A Boolean specifying whether member size (topology) geometric restriction symbols are shown. The default value is ON.

- *topologyPlanarSymmetry*

  A Boolean specifying whether planar symmetry (topology) geometric restriction symbols are shown. The default value is ON.

- *topologyPointSymmetry*

  A Boolean specifying whether point symmetry (topology) geometric restriction symbols are shown. The default value is ON.

- *topologyRotationalSymmetry*

  A Boolean specifying whether rotational symmetry (topology) geometric restriction symbols are shown. The default value is ON.

- *turnControl*

  A Boolean specifying whether turn control geometric restriction symbols are shown. The default value is ON.

### Return value

None.

### Exceptions

RangeError.



## Members

The GeometricRestrictionDisplayOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictiondisplayoptionspyc.htm?ContextScope=all#simaker-geometricrestrictiondisplayoptionssetvaluespyc)method.