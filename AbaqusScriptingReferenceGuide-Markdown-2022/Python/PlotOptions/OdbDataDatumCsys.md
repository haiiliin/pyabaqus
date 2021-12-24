# OdbDataDatumCsys object

The OdbDataDatumCsys object stores coordinate system data.

## Access

```
import visualization
session.odbData[name].datumCsyses[i]
```

## Members

The OdbDataDatumCsys object can have the following members:

- *name*

  A String specifying the coordinate system name. This String is read-only.

- *type*

  A SymbolicConstant specifying the coordinate system type. This String is read-only. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL.

- *xAxis*

  A tuple of three Floats specifying a sequence of three floats specifying the x-Axis vector. The default value is (1, 0, 0).

- *yAxis*

  A tuple of three Floats specifying a sequence of three floats specifying the y-Axis vector. The default value is (0, 1, 0).

- *zAxis*

  A tuple of three Floats specifying a sequence of three floats specifying the z-Axis vector. The default value is (0, 0, 1).

- *origin*

  A tuple of three Floats specifying a sequence of three floats specifying the origin. The default value is (0, 0, 0).