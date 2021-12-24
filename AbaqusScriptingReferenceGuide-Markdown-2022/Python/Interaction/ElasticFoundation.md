# ElasticFoundation object

The ElasticFoundation object defines a mechanical foundation.

The ElasticFoundation object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## ElasticFoundation(...)



This method creates an ElasticFoundation object.



### Path

```
mdb.models[name].ElasticFoundation
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the ElasticFoundation object is created. *createStepName* must be set to 'Initial'.

- *surface*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the surface to which the foundation applies.

- *stiffness*

  A Float specifying the foundation stiffness per area (or per length for beams).

### Optional arguments

None.

### Return value

An ElasticFoundation object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing ElasticFoundation object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ElasticFoundation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticfoundationpyc.htm?ContextScope=all#simaker-elasticfoundationelasticfoundationpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data of an existing ElasticFoundation object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *stiffness*

  A Float specifying the foundation stiffness per area (or per length for beams).

### Return value

None.

### Exceptions

None.



## Members

The ElasticFoundation object has members with the same names and descriptions as the arguments to the [ElasticFoundation ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticfoundationpyc.htm?ContextScope=all#simaker-elasticfoundationelasticfoundationpyc)method except the optional arguments to the [setValuesInStep ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticfoundationpyc.htm?ContextScope=all#simaker-elasticfoundationsetvaluesinsteppyc)method.



## Corresponding analysis keywords

- [FOUNDATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-foundation.htm?ContextScope=all#simakey-r-foundation)