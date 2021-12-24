# Crack object

The Crack object is the abstract base type for [ContourIntegral](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contourintegralpyc.htm?ContextScope=all) and future crack objects.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.cracks[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.cracks[name]
```

## resume()



This method resumes the crack that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the crack.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Crack object has the following members:

- *name*

  A String specifying the repository key.

- *suppressed*

  A Boolean specifying whether the crack is suppressed or not. The default value is OFF.