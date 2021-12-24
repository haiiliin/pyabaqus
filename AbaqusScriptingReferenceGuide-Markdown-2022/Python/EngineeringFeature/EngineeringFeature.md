# EngineeringFeature object

The EngineeringFeature object is a container for various specific engineering feature repositories. The EngineeringFeature object has no explicit constructor or methods.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures
import assembly
mdb.models[name].rootAssembly.engineeringFeatures
```

## assignSeam(...)



This method creates a seam crack along an edge or a face.



### Required arguments

- *regions*

  A sequence of [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects specifying the domain of the seam crack. The [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects must be faces or edges.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## deleteSeam(...)



This method deletes a seam crack.



### Required arguments

- *regions*

  A sequence of [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects specifying the domain of the seam crack. The [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) objects must be faces or edges.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The EngineeringFeature object can have the following members:

- *inertias*

  A repository of [Inertia](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiapyc.htm?ContextScope=all) objects.

- *cracks*

  A repository of [Crack](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-crackpyc.htm?ContextScope=all) objects.

- *fasteners*

  A repository of [Fastener](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fastenerpyc.htm?ContextScope=all) objects.

- *springDashpots*

  A repository of [SpringDashpot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-springdashpotpyc.htm?ContextScope=all) objects.