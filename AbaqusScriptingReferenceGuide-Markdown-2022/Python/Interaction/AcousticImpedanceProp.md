# AcousticImpedanceProp object

The AcousticImpedanceProp object is an interaction property that defines the properties referred to by an [AcousticImpedance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedancepyc.htm?ContextScope=all) object.

The AcousticImpedanceProp object is derived from the [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactionProperties[name]
```

## AcousticImpedanceProp(...)



This method creates an AcousticImpedanceProp object.



### Path

```
mdb.models[name].AcousticImpedanceProp
```

### Required arguments

- *name*

  A String specifying the interaction property repository key.

- *tableType*

  A SymbolicConstant specifying the type of tabular data to be defined. Possible values are IMPEDANCE and ADMITTANCE.

- *table*

  A sequence of sequences of Floats specifying acoustic impedance properties.If *tableType*=IMPEDANCE, each sequence of the table data specifies:The real part of the complex impedance.The imaginary part of the complex impedance.Frequency, if the data depend on frequency.If *tableType*=ADMITTANCE, each sequence of the table data specifies:The real part of the complex admittance.The imaginary part of the complex admittance.Frequency, if the data depend on frequency.

### Optional arguments

- *frequencyDependency*

  A Boolean specifying whether the *table* data depend on frequency. The default value is OFF.

### Return value

An AcousticImpedanceProp object.

### Exceptions

None.



## setValues(...)



This method modifies the AcousticImpedanceProp object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [AcousticImpedanceProp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedanceproppyc.htm?ContextScope=all#simaker-acousticimpedancepropacousticimpedanceproppyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The AcousticImpedanceProp object has members with the same names and descriptions as the arguments to the [AcousticImpedanceProp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticimpedanceproppyc.htm?ContextScope=all#simaker-acousticimpedancepropacousticimpedanceproppyc)method.



## Corresponding analysis keywords

- [IMPEDANCE PROPERTY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-impedanceproperty.htm?ContextScope=all#simakey-r-impedanceproperty)