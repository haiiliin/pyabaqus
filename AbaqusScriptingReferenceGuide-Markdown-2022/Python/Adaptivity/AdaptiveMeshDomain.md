# AdaptiveMeshDomain object

The AdaptiveMeshDomain object defines the region and controls that govern an Arbitrary Lagrangian Eularian (ALE) style adaptive smoothing mesh domain.

## Access

```
import step
mdb.models[name].steps[name].adaptiveMeshDomains[name]
```

## AdaptiveMeshDomain(...)



This method creates an AdaptiveMeshDomain object.



### Path

```
mdb.models[name].steps[name].AdaptiveMeshDomain
```

### Required arguments

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the adaptive mesh domain is applied.

### Optional arguments

- *controls*

  A String specifying the name of an [AdaptiveMeshControl](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshcontrolpyc.htm?ContextScope=all) object.

- *frequency*

  An Int specifying the frequency in increments at which adaptive meshing will be performed. The default value is 10.

- *initialMeshSweeps*

  An Int specifying the number of mesh sweeps to be performed at the beginning of the first step in which this adaptive mesh definition is active. The default value is 5.

- *meshSweeps*

  An Int specifying the number of mesh sweeps to be performed in each adaptive mesh increment. The default value is 1.

### Return value

An AdaptiveMeshDomain object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the AdaptiveMeshDomain object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AdaptiveMeshDomain ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshdomainpyc.htm?ContextScope=all#simaker-adaptivemeshdomainadaptivemeshdomainpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The AdaptiveMeshDomain object has members with the same names and descriptions as the arguments to the [AdaptiveMeshDomain ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivemeshdomainpyc.htm?ContextScope=all#simaker-adaptivemeshdomainadaptivemeshdomainpyc)method.