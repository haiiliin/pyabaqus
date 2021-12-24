# CyclicSymmetry object

The CyclicSymmetry object defines a cyclic symmetry analysis.

The CyclicSymmetry object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## CyclicSymmetry(...)



This method creates a CyclicSymmetry object.



### Path

```
mdb.models[name].CyclicSymmetry
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the cyclic symmetry interaction should be created.

- *main*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the main surface.

- *secondary*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the secondary surface.

- *repetitiveSectors*

  An Int specifying the total number of sectors in the cyclic symmetric model.

- *axisPoint1*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the first point of the axis of symmetry. The region should contain exactly one mesh node, vertex, interesting point, reference point, or datum point. In a two-dimensional model *axisPoint1* is the only point used to define the axis of symmetry.

- *axisPoint2*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the second point of the axis of symmetry. The region should contain exactly one mesh node, vertex, interesting point, reference point, or datum point. This point is ignored in a two-dimensional model.

### Optional arguments

- *extractedNodalDiameter*

  A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters or the nodal diameters between the user-specified values for *lowestNodalDiameter* and *highestNodalDiameter*. Possible values are ALL_NODAL_DIAMETER and SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.

- *lowestNodalDiameter*

  An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis. The default value is 0.

- *highestNodalDiameter*

  An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis. This argument value should be less than or equal to the half of the total number of sectors (as specified in the *repetitiveSectors* parameter). The default value is 0.

- *excitationNodalDiameter*

  An Int specifying the nodal diameter for which the modal-based steady-state dynamic analysis will be performed. This value should be greater than or equal to the lowest nodal diameter (specified in the *lowestNodalDiameter* parameter), and less than or equal to the highest nodal diameter (specified in the *highestNodalDiameter* parameter). The default value is 0.

- *adjustTie*

  A Boolean specifying whether or not to adjust the secondary surface of the cyclic symmetry to tie it to the main surface. The default value is ON.

- *positionTolerance*

  A Float specifying the position tolerance. The*positionTolerance* argument applies only when *positionToleranceMethod*=SPECIFY_TOLERANCE. The default value is 0.0.

- *positionToleranceMethod*

  A SymbolicConstant specifying the method used to determine the position tolerance. Possible values are COMPUTED_TOLERANCE and SPECIFY_TOLERANCE. The default value is COMPUTED_TOLERANCE.

### Return value

A CyclicSymmetry object.

### Exceptions

None.



## swapSurfaces()



This method switches the main and secondary surfaces of a cyclic symmetry interaction. This command is valid only during the step in which the interaction is created.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing CyclicSymmetry object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CyclicSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cyclicsymmetrypyc.htm?ContextScope=all#simaker-cyclicsymmetrycyclicsymmetrypyc) method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data of an existing CyclicSymmetry object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *extractedNodalDiameter*

  A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters or the nodal diameters between the user-specified values for *lowestNodalDiameter* and *highestNodalDiameter*. Possible values are ALL_NODAL_DIAMETER and SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.

- *lowestNodalDiameter*

  An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis. The default value is 0.

- *highestNodalDiameter*

  An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis. This argument value should be less than or equal to the half of the total number of sectors (as specified in the *repetitiveSectors* parameter). The default value is 0.

- *excitationNodalDiameter*

  An Int specifying the nodal diameter for which the modal-based steady-state dynamic analysis will be performed. This value should be greater than or equal to the lowest nodal diameter (specified in the *lowestNodalDiameter* parameter), and less than or equal to the highest nodal diameter (specified in the *highestNodalDiameter* parameter). The default value is 0.

### Return value

None.

### Exceptions

None.



## Members

The CyclicSymmetry object has members with the same names and descriptions as the arguments to the [CyclicSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cyclicsymmetrypyc.htm?ContextScope=all#simaker-cyclicsymmetrysetvaluesinsteppyc) method except the optional arguments to the [setValuesInStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cyclicsymmetrypyc.htm?ContextScope=all#simaker-cyclicsymmetrycyclicsymmetrypyc) method.



## Corresponding analysis keywords

- [CLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cload.htm?ContextScope=all#simakey-r-cload), CYCLIC MODE
- [CYCLIC SYMMETRY MODEL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cyclicsymmetrymodel.htm?ContextScope=all#simakey-r-cyclicsymmetrymodel)
- [DLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dload.htm?ContextScope=all#simakey-r-dload), CYCLIC MODE
- [DSLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dsload.htm?ContextScope=all#simakey-r-dsload), CYCLIC MODE
- [SELECT CYCLIC SYMMETRY MODES](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-selectcyclicsymmetrymodes.htm?ContextScope=all#simakey-r-selectcyclicsymmetrymodes)
- [TIE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-tie.htm?ContextScope=all#simakey-r-tie), CYCLIC SYMMETRY