# DatumCsys object

The DatumCsys object has no direct constructor; it is created when a [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) object is created. For example, the DatumCsysByOffset method creates a Feature object that creates a DatumCsys object.

The DatumCsys object is derived from the [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].datums[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].datums[i]
mdb.models[name].rootAssembly.connectorOrientations[i].localCsys1
mdb.models[name].rootAssembly.connectorOrientations[i].localCsys2
mdb.models[name].rootAssembly.datums[i]
mdb.models[name].rootAssembly.instances[name].datums[i]
import odbAccess
session.odbs[name].rootAssembly.connectorOrientations[i].localCsys1
session.odbs[name].rootAssembly.connectorOrientations[i].localCsys2
```

## Members

The DatumCsys object has the following members:

- *coordSysType*

  A SymbolicConstant specifying the type of the coordinate system. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL.

- *origin*

  A [DatumPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpointpyc.htm?ContextScope=all) object specifying the origin of the coordinate system.

- *axis1*

  A [DatumAxis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the 1-direction of the coordinate system.

- *axis2*

  A [DatumAxis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the 2-direction of the coordinate system.

- *axis3*

  A [DatumAxis](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumaxispyc.htm?ContextScope=all) object specifying the 3-direction of the coordinate system.