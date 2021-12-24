# ActivateElements object

The ActivateElements object is used turn on progressive element activation within a step definition.

## Access

```
mdb.models[name].steps[name].activateElements[key]
```

## ActivateElements(...)

This method creates an ActivateElements object.

### Path

```
mdb.models[name].ActivateElements
```

### Required arguments

- *tableCollection*

  A String specifying the name of the tableCollection object.

- *activation*

  A string specifying the name of progressive element activation.

### Optional arguments

- *eigenTimeConst*

  A Double specifying the time constant used to ramp up the eigenstrains at element activation.

- *expansionTimeConstant*

  A Double specifying the time constant used to ramp up the thermal strains at element activation.

### Return value

An ActivateElements object.

### Exceptions

RangeError.



## setValues(...)

This method modifies the ActivateElements object.

### Optional arguments

The optional arguments to setValues are the same as the optional arguments to the [ActivateElements](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-activateelementspyc.htm?ContextScope=all#simaker-c-activateelementspyc) method.

### Exceptions

RangeError.



## Members

The ActivateElements object has members with the same names and descriptions as the arguments to the [ActivateElements](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-activateelementspyc.htm?ContextScope=all#simaker-c-activateelementspyc) method.



## Corresponding analysis keywords

- [ActivateElements](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-activateelements.htm?ContextScope=all#simakey-r-activateelements)
- [ElementProgressiveActivation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-elementprogressiveactivation.htm?ContextScope=all#simakey-r-elementprogressiveactivation)