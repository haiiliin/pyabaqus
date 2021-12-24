# IntegratedOutputSection object

The IntegratedOutputSection object specifies parameters used for integrated output.

## Access

```
import step
mdb.models[name].integratedOutputSections[name]
```

## IntegratedOutputSection(...)



This method creates an IntegratedOutputSection object.



### Path

```
mdb.models[name].IntegratedOutputSection
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surface over which the output is based.

- *refPoint*

  None or a [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the anchor point about which the integrated moment over the output region is computed or the SymbolicConstant None representing the global origin. The default value is None.

- *refPointAtCenter*

  A Boolean specifying that the *refPoint* be adjusted so that it coincides with the center of the output region in the initial configuration. This argument is valid only when you include the *refPoint* argument. The default value is OFF.

- *refPointMotion*

  A SymbolicConstant specifying how to relate the motion of *refPoint* to the average motion of the output region. A value of INDEPENDENT will allow the *refPoint* to move independent of the output region. A value of AVERAGE_TRANSLATION will set the displacement of the *refPoint* equal to the average translation of the output region. A value of AVERAGE will set the displacement and rotation of the *refPoint* equal to the average translation of the output region. The default value is INDEPENDENT.This argument is valid only when you include the *refPoint* argument.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system used to express vector output. If *localCsys*=None, the degrees of freedom are defined in the global coordinate system. The default value is None.

- *projectOrientation*

  A Boolean specifying that the coordinate system be projected onto the *surface* such that the 1–axis is normal to the *surface*. Projection onto a planar *surface* is such that the 1-axis is normal to the surface, and a projection onto a nonplanar *surface* is such that a least-squares fit surface will be used. The default value is OFF.

### Return value

An IntegratedOutputSection object.

### Exceptions

None.



## setValues(...)



This method modifies the IntegratedOutputSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [IntegratedOutputSection ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-integratedoutputsectionpyc.htm?ContextScope=all#simaker-integratedoutputsectionintegratedoutputsectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The IntegratedOutputSection object has members with the same names and descriptions as the arguments to the [IntegratedOutputSection ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-integratedoutputsectionpyc.htm?ContextScope=all#simaker-integratedoutputsectionintegratedoutputsectionpyc)method.