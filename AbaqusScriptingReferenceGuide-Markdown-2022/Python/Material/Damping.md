# Damping object

The Damping object specifies material damping.

## Access

```
import material
mdb.models[name].materials[name].damping
import odbMaterial
session.odbs[name].materials[name].damping
```

## Damping(...)



This method creates a Damping object.



### Path

```
mdb.models[name].materials[name].Damping
session.odbs[name].materials[name].Damping
```

### Required arguments

None.

### Optional arguments

- *alpha*

  A Float specifying the αRαR factor to create mass proportional damping in direct-integration and explicit dynamics. The default value is 0.0.

- *beta*

  A Float specifying the βRβR factor to create stiffness proportional damping in direct-integration and explicit dynamics. The default value is 0.0.

- *composite*

  A Float specifying the fraction of critical damping to be used with this material in calculating composite damping factors for the modes (for use in modal dynamics). The default value is 0.0.This argument applies only to Abaqus/Standard analyses.

- *structural*

  A Float specifying the structural factor to create material damping in direct-integration and explicit dynamics. The default value is 0.0.

### Return value

A Damping object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Damping object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Damping ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dampingpyc.htm?ContextScope=all#simaker-dampingdampingpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Damping object has members with the same names and descriptions as the arguments to the [Damping ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dampingpyc.htm?ContextScope=all#simaker-dampingdampingpyc)method.



## Corresponding analysis keywords

- [DAMPING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damping.htm?ContextScope=all#simakey-r-damping)