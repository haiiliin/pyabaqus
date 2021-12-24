# ConcreteTensionStiffening object

The ConcreteTensionStiffening object specifies hardening for the concrete damaged plasticity model.

## Access

```
import material
mdb.models[name].materials[name].concreteDamagedPlasticity\
.concreteTensionStiffening
import odbMaterial
session.odbs[name].materials[name].concreteDamagedPlasticity\
.concreteTensionStiffening
```

## ConcreteTensionStiffening(...)



This method creates a ConcreteTensionStiffening object.



### Path

```
mdb.models[name].materials[name].concreteDamagedPlasticity\
.ConcreteTensionStiffening
session.odbs[name].materials[name].concreteDamagedPlasticity\
.ConcreteTensionStiffening
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *rate*

  A Boolean specifying whether the data depend on rate. The default value is OFF.

- *type*

  A SymbolicConstant specifying the type of postcracking behavior data. Possible values are:

  - STRAIN, specifying postfailure stress as a function of cracking strain.
  - DISPLACEMENT, specifying postfailure stress as a function of cracking displacement.
  - GFI, specifying failure stress as a function of the fracture energy.

  The default value is STRAIN.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=STRAIN, the table data specify the following:

- Remaining direct stress after cracking, σt.
- Direct cracking strain, ϵckt.
- Direct cracking strain rate, ˙ϵckt.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT, the table data specify the following:

- Remaining direct stress after cracking, σt.
- Direct cracking displacement, uckt.
- Direct cracking displacement rate, ˙uckt
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=GFI, the table data specify the following:

- Failure stress, σt0σt⁢0.
- Fracture energy, Gf.
- Direct cracking displacement rate, ˙uckt.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ConcreteTensionStiffening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ConcreteTensionStiffening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConcreteTensionStiffening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretetensionstiffeningpyc.htm?ContextScope=all#simaker-concretetensionstiffeningconcretetensionstiffeningpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ConcreteTensionStiffening object has members with the same names and descriptions as the arguments to the [ConcreteTensionStiffening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretetensionstiffeningpyc.htm?ContextScope=all#simaker-concretetensionstiffeningconcretetensionstiffeningpyc)method.



## Corresponding analysis keywords

- [CONCRETE TENSION STIFFENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-concretetensionstiffening.htm?ContextScope=all#simakey-r-concretetensionstiffening)