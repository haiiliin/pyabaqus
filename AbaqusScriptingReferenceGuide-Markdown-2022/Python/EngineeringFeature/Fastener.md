# Fastener object

The Fastener object is the abstract base type for [PointFastener](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pointfastenerpyc.htm?ContextScope=all), [DiscreteFastener](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefastenerpyc.htm?ContextScope=all), and [AssembledFastener](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assembledfastenerpyc.htm?ContextScope=all).

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.fasteners[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.fasteners[name]
```

## resume()



This method resumes the fastener that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the fastener.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Fastener object has the following members:

- *name*

  A String specifying the repository key.

- *suppressed*

  A Boolean specifying whether the fastener is suppressed or not. The default value is OFF.