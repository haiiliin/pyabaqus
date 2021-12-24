# PorousFailureCriteria object

The PorousFailureCriteria object specifies the material failure criteria for a porous metal.

## Access

```
import material
mdb.models[name].materials[name].porousMetalPlasticity\
.porousFailureCriteria
import odbMaterial
session.odbs[name].materials[name].porousMetalPlasticity\
.porousFailureCriteria
```

## PorousFailureCriteria(...)



This method creates a PorousFailureCriteria object.



### Path

```
mdb.models[name].materials[name].porousMetalPlasticity\
.PorousFailureCriteria
session.odbs[name].materials[name].porousMetalPlasticity\
.PorousFailureCriteria
```

### Required arguments

None.

### Optional arguments

- *fraction*

  A Float specifying the void volume fraction at total failure, fF>0. The default value is 1.0.

- *criticalFraction*

  A Float specifying the critical void volume fraction, fc≥0. The default value is 1.0.

### Return value

A PorousFailureCriteria object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the PorousFailureCriteria object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PorousFailureCriteria ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousfailurecriteriapyc.htm?ContextScope=all#simaker-porousfailurecriteriaporousfailurecriteriapyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The PorousFailureCriteria object has members with the same names and descriptions as the arguments to the [PorousFailureCriteria ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porousfailurecriteriapyc.htm?ContextScope=all#simaker-porousfailurecriteriaporousfailurecriteriapyc)method.



## Corresponding analysis keywords

- [POROUS FAILURE CRITERIA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-porousfailurecriteria.htm?ContextScope=all#simakey-r-porousfailurecriteria)