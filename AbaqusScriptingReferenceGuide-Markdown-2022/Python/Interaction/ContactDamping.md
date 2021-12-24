# ContactDamping object

The ContactDamping object specifies damping for a contact interaction property.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].damping
```

## Damping(...)



This method creates a ContactDamping object.



### Path

```
mdb.models[name].interactionProperties[name].Damping
```

### Required arguments

None.

### Optional arguments

- *definition*

  A SymbolicConstant specifying the method used to define the damping. Possible values are DAMPING_COEFFICIENT and CRITICAL_DAMPING_FRACTION. The default value is DAMPING_COEFFICIENT.

- *tangentFraction*

  The SymbolicConstant DEFAULT or a Float specifying the tangential damping coefficient divided by the normal damping coefficient. The default value is DEFAULT.

- *clearanceDependence*

  A SymbolicConstant specifying the variation of the damping coefficient or fraction with respect to clearance. Possible values are STEP, LINEAR, and BILINEAR. The default value is STEP.If *definition*=CRITICAL_DAMPING_FRACTION, the only possible value is STEP.

- *table*

  A sequence of pairs of Floats specifying the damping properties. The items in the table data are described below.

### Table data

If *definition*=DAMPING_COEFFICIENT and *clearanceDependence*=STEP, the table data specify the following:

- Damping coefficient.

If *definition*=DAMPING_COEFFICIENT and *clearanceDependence*=LINEAR or BILINEAR, the table data specify the following:

- Damping coefficient.
- Clearance.

Two pairs must be given for *clearanceDependence*=LINEAR and three pairs for *clearanceDependence*=BILINEAR. The first pair must have *clearance*=0.0, and the last pair must have *coefficient*=0.0.

If *definition*=CRITICAL_DAMPING_FRACTION, the table data specify the following:

- Critical damping fraction.

### Return value

A ContactDamping object.

### Exceptions

None.



## setValues(...)



This method modifies the ContactDamping object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ContactDamping ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactdampingpyc.htm?ContextScope=all#simaker-contactdampingdampingpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The ContactDamping object has the following members:

- *definition*

  A SymbolicConstant specifying the method used to define the damping. Possible values are DAMPING_COEFFICIENT and CRITICAL_DAMPING_FRACTION. The default value is DAMPING_COEFFICIENT.

- *tangentFraction*

  The SymbolicConstant DEFAULT or a Float specifying the tangential damping coefficient divided by the normal damping coefficient. The default value is DEFAULT.

- *clearanceDependence*

  A SymbolicConstant specifying the variation of the damping coefficient or fraction with respect to clearance. Possible values are STEP, LINEAR, and BILINEAR. The default value is STEP.If *definition*=CRITICAL_DAMPING_FRACTION, the only possible value is STEP.

- *table*

  A tuple of pairs of Floats specifying the damping properties. The items in the table data are described below.



## Corresponding analysis keywords

- [CONTACT DAMPING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactdamping.htm?ContextScope=all#simakey-r-contactdamping)