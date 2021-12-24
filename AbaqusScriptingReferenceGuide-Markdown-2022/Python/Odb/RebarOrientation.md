# RebarOrientation object

The RebarOrientation object represents the orientation of the rebar reference.

## Access

```
import odbAccess
session.odbs[name].parts[name].rebarOrientations[i]
session.odbs[name].rootAssembly.instances[name].rebarOrientations[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.rebarOrientations[i]
```

## Members

The RebarOrientation object can have the following members:

- *axis*

  A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3.

- *angle*

  A Float specifying the angle of the additional rotation.

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying a region for which the rebar orientation is defined.

- *csys*

  An [OdbDatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatumcsyspyc.htm?ContextScope=all) object specifying a datum coordinates system.