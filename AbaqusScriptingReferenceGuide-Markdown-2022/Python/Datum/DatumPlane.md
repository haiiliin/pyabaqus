# DatumPlane object

The DatumPlane object has no direct constructor; it is created when a [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) object is created. For example, the DatumPlaneByPrincipalPlane method creates a Feature object that creates a DatumPlane object.

The DatumPlane object is derived from the [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].datums[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].datums[i]
mdb.models[name].rootAssembly.datums[i]
mdb.models[name].rootAssembly.instances[name].datums[i]
```

## Members

The DatumPlane object has the following members:

- *pointOn*

  A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point located on the datum.

- *normal*

  A tuple of Floats specifying a sequence of three Floats specifying the normal.