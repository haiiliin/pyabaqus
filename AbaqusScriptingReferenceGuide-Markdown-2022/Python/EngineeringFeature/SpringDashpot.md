# SpringDashpot object

The SpringDashpot object is the abstract base type for the [SpringDashpotToGround](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-springdashpottogroundpyc.htm?ContextScope=all) and [TwoPointSpringDashpot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-twopointspringdashpotpyc.htm?ContextScope=all) objects.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.springDashpots[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.springDashpots[name]
```

## resume()



This method resumes the spring/dashpot that was previously suppressed.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## suppress()



This method suppresses the spring/dashpot.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The SpringDashpot object has the following members:

- *name*

  A String specifying the repository key.

- *suppressed*

  A Boolean specifying whether the spring/dashpot is suppressed or not. The default value is OFF.