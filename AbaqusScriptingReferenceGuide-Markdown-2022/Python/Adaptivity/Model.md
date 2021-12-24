# Model object

The following commands operate on Model objects. For more information about the Model object, see [Model object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?ContextScope=all).

## Access

```
import mesh
```

## adaptiveRemesh(...)



This method remeshes the model using the active remesh rules in the model and the error indicator results from a previous analysis.



### Required arguments

- *odb*

  An [Odb](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?ContextScope=all) object containing error output field results.

### Optional arguments

None.

### Return value

An [AdaptivityIteration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivityiterationpyc.htm?ContextScope=all) Object.

### Exceptions

None.