# Inertia object

The Inertia object is the abstract base type for [HeatCapacitance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-heatcapacitancepyc.htm?ContextScope=all), [NonstructuralMass](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nonstructuralmasspyc.htm?ContextScope=all), and [PointMassInertia](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pointmassinertiapyc.htm?ContextScope=all).

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.inertias[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]
```

## resume()



This method resumes the inertia that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the inertia.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Inertia object has the following members:

- *name*

  A String specifying the repository key.

- *suppressed*

  A Boolean specifying whether the inertia is suppressed or not. The default value is OFF.