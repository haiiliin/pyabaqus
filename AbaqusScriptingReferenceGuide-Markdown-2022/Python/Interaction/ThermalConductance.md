# ThermalConductance object

The ThermalConductance object specifies thermal conductance for a contact interaction property.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].thermalConductance
```

## ThermalConductance(...)



This method creates a ThermalConductance object.



### Path

```
mdb.models[name].interactionProperties[name].ThermalConductance
```

### Required arguments

None.

### Optional arguments

- *definition*

  A SymbolicConstant specifying how the thermal conductance is defined. Possible values are TABULAR and USER_DEFINED. The default value is TABULAR.

- *clearanceDependency*

  A Boolean specifying whether to use clearance-dependent data. The default value is ON.

- *pressureDependency*

  A Boolean specifying whether to use pressure-dependent data. The default value is OFF.

- *temperatureDependencyC*

  A Boolean specifying whether to use temperature-dependent data with clearance dependency. The default value is OFF.

- *massFlowRateDependencyC*

  A Boolean specifying whether to use mass-flow-rate-dependent data with clearance dependency. The default value is OFF.

- *dependenciesC*

  An Int specifying the number of field variables to use with clearance dependency. The default value is 0.

- *clearanceDepTable*

  A sequence of sequences of Floats specifying clearance dependency data. The items in the table data are described below.

- *temperatureDependencyP*

  A Boolean specifying whether to use temperature-dependent data with pressure dependency. The default value is OFF.

- *massFlowRateDependencyP*

  A Boolean specifying whether to use mass-flow-rate-dependent data with pressure dependency. The default value is OFF.

- *dependenciesP*

  An Int specifying the number of field variables to use with pressure dependency. The default value is 0.

- *pressureDepTable*

  A sequence of sequences of Floats specifying pressure dependency data. The items in the table data are described below.

### Table data

The *clearanceDepTable* data specify the following:

- Conductivity.
- Clearance.
- Temperature, if the data depend on temperature.
- Mass flow rate, if the data depend on mass flow rate.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

The *pressureDepTable* data specify the following:

- Conductivity.
- Pressure.
- Temperature, if the data depend on temperature.
- Mass flow rate, if the data depend on mass flow rate.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ThermalConductance object.

### Exceptions

None.



## setValues(...)



This method modifies the ThermalConductance object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ThermalConductance ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-thermalconductancepyc.htm?ContextScope=all#simaker-thermalconductancethermalconductancepyc)method.

### Return value

None.

### Exceptions

None.



## Members

The ThermalConductance object has members with the same names and descriptions as the arguments to the [ThermalConductance ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-thermalconductancepyc.htm?ContextScope=all#simaker-thermalconductancethermalconductancepyc)method.



## Corresponding analysis keywords

- [GAP CONDUCTANCE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gapconductance.htm?ContextScope=all#simakey-r-gapconductance)