# CohesiveBehavior object

The CohesiveBAccess

```
import interaction
mdb.models[name].interactionProperties[name].cohesiveBehavior
```

## CohesiveBehavior(...)



This method creates a CohesiveBehavior object.



### Path

```
mdb.models[name].interactionProperties[name].CohesiveBehavior
```

### Required arguments

None.

### Optional arguments

- *repeatedContacts*

  A Boolean specifying whether to enforce cohesive behavior for recurrent contacts at nodes on the secondary surface subsequent to ultimate failure. The default value is OFF.

- *eligibility*

  A SymbolicConstant specifying the eligible secondary nodes. Possible values are ALL_NODES, INITIAL_NODES, and SPECIFIED. The default value is ALL_NODES.

- *defaultPenalties*

  A Boolean specifying whether to use the default contact penalties. The default value is ON.

- *coupling*

  A SymbolicConstant specifying whether the traction-separation coefficients are coupled or uncoupled. This argument is valid only for *defaultPenalties*=OFF. Possible values are UNCOUPLED and COUPLED. The default value is UNCOUPLED.

- *temperatureDependency*

  A Boolean specifying whether the coefficient data depend on temperature. This argument is valid only for *defaultPenalties*=OFF. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variables. This argument is valid only for *defaultPenalties*=OFF. The default value is 0.

- *table*

  A sequence of sequences of Floats specifying the traction-separation coefficients. The items in the table data are described below. This argument is valid only for *defaultPenalties*=OFF.

### Table data

If *coupling*=UNCOUPLED, the table data specify the following:

- Stiffness coefficient in the normal direction, KnnKn⁢n.
- Stiffness coefficient in the first shear direction, KssKs⁢s.
- Stiffness coefficient in the second shear direction, KttKt⁢t.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *coupling*=COUPLED, the table data specify the following:

- Stiffness coefficient in the normal direction, KnnKn⁢n.
- Stiffness coefficient in the first shear direction, KssKs⁢s.
- Stiffness coefficient in the second shear direction, KttKt⁢t.
- Coupled stiffness coefficient, KnsKn⁢s.
- Coupled stiffness coefficient, KntKn⁢t.
- Coupled stiffness coefficient, KstKs⁢t.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A CohesiveBehavior object.

### Exceptions

None.



## setValues(...)



This method modifies the CohesiveBehavior object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CohesiveBehavior](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cohesivebehaviorpyc.htm?ContextScope=all#simaker-cohesivebehaviorcohesivebehaviorpyc) method.

### Return value

None.

### Exceptions

None.



## Members

The CohesiveBehavior object has members with the same names and descriptions as the arguments to the [CohesiveBehavior](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cohesivebehaviorpyc.htm?ContextScope=all#simaker-cohesivebehaviorcohesivebehaviorpyc) method.



## Corresponding analysis keywords

- [COHESIVE BEHAVIOR](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-cohesivebehavior.htm?ContextScope=all#simakey-r-cohesivebehavior), Cohesive behavior object specifies cohesive behavior for a contact interaction property.
