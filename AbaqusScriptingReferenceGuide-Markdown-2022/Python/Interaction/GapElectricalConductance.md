# GapElectricalConductance object

The GapElectricalConductance object specifies electrical conductance for a contact interaction property.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].electricalConductance
```

## GapElectricalConductance(...)



This method creates a GapElectricalConductance object.



### Path

```
mdb.models[name].interactionProperties[name].GapElectricalConductance
```

### Required arguments

None.

### Optional arguments

- *definition*

  A SymbolicConstant specifying how the electrical conductance is defined. Possible values are TABULAR and USER_DEFINED. The default value is TABULAR.

- *clearanceDependency*

  A Boolean specifying whether to use clearance-dependent data. The default value is ON.

- *pressureDependency*

  A Boolean specifying whether to use pressure-dependent data. The default value is OFF.

- *temperatureDependencyC*

  A Boolean specifying whether to use temperature-dependent data with clearance dependency. The default value is OFF.

- *dependenciesC*

  An Int specifying the number of field variables to use with clearance dependency. The default value is 0.

- *clearanceDepTable*

  A sequence of sequences of Floats specifying clearance dependency data. The items in the table data are described below.

- *temperatureDependencyP*

  A Boolean specifying whether to use temperature-dependent data with pressure dependency. The default value is OFF.

- *dependenciesP*

  An Int specifying the number of field variables to use with pressure dependency. The default value is 0.

- *pressureDepTable*

  A sequence of sequences of Floats specifying pressure dependency data. The items in the table data are described below.

### Table data

The *clearanceDepTable* data specify the following:

- Conductivity.
- Clearance.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

The *pressureDepTable* data specify the following:

- Conductivity.
- Pressure.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A GapElectricalConductance object.

### Exceptions

None.



## setValues(...)



This method modifies the GapElectricalConductance object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GapElectricalConductance ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapelectricalconductancepyc.htm?ContextScope=all#simaker-gapelectricalconductancegapelectricalconductancepyc)method.

### Return value

None.

### Exceptions

None.



## Members

The GapElectricalConductance object has members with the same names and descriptions as the arguments to the [GapElectricalConductance ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapelectricalconductancepyc.htm?ContextScope=all#simaker-gapelectricalconductancegapelectricalconductancepyc)method.



## Corresponding analysis keywords

- [GAP ELECTRICAL CONDUCTANCE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gapelectricalconductance.htm?ContextScope=all#simakey-r-gapelectricalconductance)