# DatumPoint object

The DatumPoint object has no direct constructor; it is created when a [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) object is created. For example, the DatumPointByCoordinate method creates a Feature object that creates a DatumPoint object.

The DatumPoint object is derived from the [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object.

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

The DatumPoint object has the following member:

- *pointOn*

  A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point located on the datum.