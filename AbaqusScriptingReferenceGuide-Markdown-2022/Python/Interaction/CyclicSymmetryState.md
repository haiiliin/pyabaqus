# CyclicSymmetryState object

The CyclicSymmetryState object stores the propagating data for a [CyclicSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cyclicsymmetrypyc.htm?ContextScope=all) object. One instance of this object is created internally by the [CyclicSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cyclicsymmetrypyc.htm?ContextScope=all) object for each step. The instance is also deleted internally by the [CyclicSymmetry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cyclicsymmetrypyc.htm?ContextScope=all) object.

The CyclicSymmetryState object has no constructor or methods.

The CyclicSymmetryState object is derived from the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].steps[name].interactionStates[name]
```

## Members

The CyclicSymmetryState object has the following members:

- *extractedNodalDiameter*

  A SymbolicConstant specifying whether Abaqus should extract all possible nodal diameters or the nodal diameters between the user-specified values for *lowestNodalDiameter* and *highestNodalDiameter*. Possible values are ALL_NODAL_DIAMETER and SPECIFIED_NODAL_DIAMETER. The default value is ALL_NODAL_DIAMETER.

- *extractedNodalDiameterState*

  A SymbolicConstant specifying the propagation state of the *extractedNodalDiameter* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *lowestNodalDiameter*

  An Int specifying the lowest nodal diameter to be used in the eigenfrequency analysis. The default value is 0.

- *lowestNodalDiameterState*

  A SymbolicConstant specifying the propagation state of the *lowestNodalDiameter* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *highestNodalDiameter*

  An Int specifying the highest nodal diameter to be used in the eigenfrequency analysis. This argument value should be less than or equal to the half of the total number of sectors. The default value is 0.

- *highestNodalDiameterState*

  A SymbolicConstant specifying the propagation state of the *highestNodalDiameter* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *excitiationNodalDiameter*

  An Int specifying the nodal diameter for which the modal-based steady-state dynamic analysis will be performed. This value should be greater than or equal to the lowest nodal diameter (specified in the *lowestNodalDiameter* parameter), and less than or equal to the highest nodal diameter (specified in the *highestNodalDiameter* parameter). The default value is 0.

- *excitiationNodalDiameterState*

  A SymbolicConstant specifying the propagation state of the *excitiationNodalDiameter* member. Possible values are UNSET, SET, UNCHANGED, and FREED.

- *status*

  A SymbolicConstant specifying the propagation state of the [InteractionState](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionstatepyc.htm?ContextScope=all) object. Possible values are:

  - NOT_YET_ACTIVE
  - CREATED
  - PROPAGATED
  - MODIFIED
  - DEACTIVATED
  - NO_LONGER_ACTIVE
  - TYPE_NOT_APPLICABLE
  - INSTANCE_NOT_APPLICABLE
  - BUILT_INTO_BASE_STATE



## Corresponding analysis keywords

- [CLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cload.htm?ContextScope=all#simakey-r-cload), CYCLIC MODE
- [DLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dload.htm?ContextScope=all#simakey-r-dload), CYCLIC MODE
- [DSLOAD](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dsload.htm?ContextScope=all#simakey-r-dsload), CYCLIC MODE
- [SELECT CYCLIC SYMMETRY MODES](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-selectcyclicsymmetrymodes.htm?ContextScope=all#simakey-r-selectcyclicsymmetrymodes)