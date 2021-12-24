# FractureCriterion object

The FractureCriterion object specifies fractureCriterion options for a contact interaction property.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].fractureCriterion
```

## FractureCriterion(...)



This method creates a FractureCriterion object.



### Path

```
mdb.models[name].interactionProperties[name].FractureCriterion
```

### Required arguments

- *initTable*

  A sequence of sequences of Floats specifying the value defining the fracture criterion. The items in the table data are described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of data used to define the fracture criterion. Possible values are VCCT and ENHANCED VCCT. The default value is VCCT.

- *mixedModeBehavior*

  A SymbolicConstant specifying the mixed mode behavior type used to define fracture criterion. Possible values are BK, POWER, and REEDER. The default value is BK.

- *temperatureDependency*

  A Boolean specifying whether the fracture criterion data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of fracture criterion data field variables. The default value is 0.

- *tolerance*

  A Float specifying the tolerance for VCCT\Enhanced VCCT type. The default value is 0.2.

- *specifyUnstableCrackProp*

  A SymbolicConstant specifying whether to include unstable crack growth tolerance in fracture criterion. Possible values are ON and OFF. The default value is OFF.

- *unstableTolerance*

  The SymbolicConstant DEFAULT or a Float specifying the tolerance for unstable crack propagation. This parameter specified only if *specifyUnstableCrackProp*=ON. The default value is DEFAULT.

### Table data

Table data for *initTable*:

If *type*=VCCT for *mixedModeBehavior*=BK or REEDER, the table data specify the following:

- Mode I critical energy release rate, GICGI⁢C.
- Mode II critical energy release rate, GIICGI⁢I⁢C.
- Mode III critical energy release rate, GIIICGI⁢I⁢I⁢C.
- Exponent, ηη.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=VCCT for *mixedModeBehavior*=POWER, the table data specify the following:

- Mode I critical energy release rate, GICGI⁢C.
- Mode II critical energy release rate, GIICGI⁢I⁢C.
- Mode III critical energy release rate, GIIICGI⁢I⁢I⁢C.
- Exponent, ama⁢m.
- Exponent, ana⁢n.
- Exponent, aoa⁢o.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENHANCED VCCT for *mixedModeBehavior*=BK or REEDER, the table data specify the following:

- Mode I critical energy release rate for onset crack, GICGI⁢C.
- Mode II critical energy release rate for onset crack, GIICGI⁢I⁢C.
- Mode III critical energy release rate for onset crack, GIIICGI⁢I⁢I⁢C.
- Mode I critical energy release rate for crack propagation, GICGI⁢C.
- Mode II critical energy release rate for crack propagation, GIICGI⁢I⁢C.
- Mode III critical energy release rate for crack propagation, GIIICGI⁢I⁢I⁢C.
- Exponent, ηη.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENHANCED VCCT for *mixedModeBehavior*=POWER, the table data specify the following:

- Mode I critical energy release rate for onset crack, GICGI⁢C.
- Mode II critical energy release rate for onset crack, GIICGI⁢I⁢C.
- Mode III critical energy release rate for onset crack, GIIICGI⁢I⁢I⁢C.
- Mode I critical energy release rate for crack propagation, GICGI⁢C.
- Mode II critical energy release rate for crack propagation, GIICGI⁢I⁢C.
- Mode III critical energy release rate for crack propagation, GIIICGI⁢I⁢I⁢C.
- Exponent, ama⁢m.
- Exponent, ana⁢n.
- Exponent, aoa⁢o.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A FractureCriterion object.

### Exceptions

None.



## setValues(...)



This method modifies the FractureCriterion object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FractureCriterion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fracturecriterionpyc.htm?ContextScope=all#simaker-fracturecriterionfracturecriterionpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The FractureCriterion object has members with the same names and descriptions as the arguments to the [FractureCriterion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fracturecriterionpyc.htm?ContextScope=all#simaker-fracturecriterionfracturecriterionpyc)method.



## Corresponding analysis keywords

- [FRACTURE CRITERION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-fracturecriterion.htm?ContextScope=all#simakey-r-fracturecriterion)