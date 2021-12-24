# MassScaling object

A MassScaling object defines the region and controls that govern mass scaling.

## Access

```
import step
mdb.models[name].steps[name].massScaling[i]
```

## Members

The MassScaling object can have the following members:

- *objective*

  A SymbolicConstant specifying the objective of the mass scaling definition. Possible values are SEMI_AUTOMATIC, AUTOMATIC, and REINITIALIZE. The default value is SEMI_AUTOMATIC.

- *occurs*

  A SymbolicConstant specifying whether mass scaling should be performed at the beginning of the step or throughout the step. Possible values are AT_BEGINNING and THROUGHOUT_STEP.

- *type*

  A SymbolicConstant specifying the type of scaling. Possible values are UNIFORM, BELOW_MIN, SET_EQUAL_DT, and ROLLING. The default value is BELOW_MIN.

- *factor*

  A Float specifying a scaling factor.

- *dt*

  A Float specifying a target time increment.

- *frequency*

  An Int specifying the frequency at which mass scaling calculations are performed.

- *numberInterval*

  An Int specifying the number of intervals at which mass scaling calculations are performed.

- *feedRate*

  A Float specifying the estimated average velocity of the workpiece in the rolling direction at steady-state conditions.

- *extrudedLength*

  A Float specifying the average element length in the extruded direction.

- *crossSection*

  An Int specifying the number of nodes in the cross-section of the workpiece.

- *direction*

  A SymbolicConstant specifying the rolling direction. Possible values are GLOBAL_X, GLOBAL_Y, GLOBAL_Z, and GLOBAL_NONE. The default value is GLOBAL_X.

- *region*

  The SymbolicConstant MODEL or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying where the mass scaling is applied. The default value is MODEL.