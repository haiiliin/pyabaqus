# HeatCapacitance object

The HeatCapacitance object defines point heat capacitance on a part or an assembly region.

The HeatCapacitance object is derived from the [Inertia](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiapyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.inertias[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]
```

## HeatCapacitance(...)



This method creates a HeatCapacitance object.



### Path

```
mdb.models[name].parts[name].engineeringFeatures.HeatCapacitance
mdb.models[name].rootAssembly.engineeringFeatures.HeatCapacitance
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the heat capacitance is applied.

- *table*

  A sequence of sequences of Floats specifying heat capacitance properties. The items in the table data are described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

The table data specify the following:

- Heat capacitance magnitude, ρcVρ⁢c⁢V (density × specific heat × volume).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A HeatCapacitance object.

### Exceptions

None.



## setValues(...)



This method modifies the HeatCapacitance object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [HeatCapacitance ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-heatcapacitancepyc.htm?ContextScope=all#simaker-heatcapacitanceheatcapacitancepyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The HeatCapacitance object has members with the same names and descriptions as the arguments to the [HeatCapacitance ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-heatcapacitancepyc.htm?ContextScope=all#simaker-heatcapacitanceheatcapacitancepyc)method.

In addition, the HeatCapacitance object has the following member:

- *suppressed*

  A Boolean specifying whether the inertia is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [HEATCAP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-heatcap.htm?ContextScope=all#simakey-r-heatcap)