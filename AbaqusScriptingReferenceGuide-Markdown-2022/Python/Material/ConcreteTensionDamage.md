# ConcreteTensionDamage object

The ConcreteTensionDamage object specifies hardening for the concrete damaged plasticity model.

## Access

```
import material
mdb.models[name].materials[name].concreteDamagedPlasticity\
.concreteTensionDamage
import odbMaterial
session.odbs[name].materials[name].concreteDamagedPlasticity\
.concreteTensionDamage
```

## ConcreteTensionDamage(...)



This method creates a ConcreteTensionDamage object.



### Path

```
mdb.models[name].materials[name].concreteDamagedPlasticity\
.ConcreteTensionDamage
session.odbs[name].materials[name].concreteDamagedPlasticity\
.ConcreteTensionDamage
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *compressionRecovery*

  A Float specifying the value of the stiffness recovery factor, wcwc, that determines the amount of compression stiffness that is recovered as loading changes from tension to compression. The default value is 1.0.

- *type*

  A SymbolicConstant specifying the type of tensile damage data. Set *type*=STRAIN to specify the tensile damage variable as a function of cracking strain. Set *type*=DISPLACEMENT to specify the tensile damage variable as a function of cracking displacement. Possible values are STRAIN and DISPLACEMENT. The default value is STRAIN.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

If *type*=STRAIN, the table data specify the following:

- Tensile damage variable, dt.
- Direct cracking strain, ϵtc⁢k.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=DISPLACEMENT, the table data specify the following:

- Tensile damage variable, dt.
- Direct cracking displacement, utc⁢k.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ConcreteTensionDamage object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ConcreteTensionDamage object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConcreteTensionDamage ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretetensiondamagepyc.htm?ContextScope=all#simaker-concretetensiondamageconcretetensiondamagepyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ConcreteTensionDamage object has members with the same names and descriptions as the arguments to the [ConcreteTensionDamage ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretetensiondamagepyc.htm?ContextScope=all#simaker-concretetensiondamageconcretetensiondamagepyc)method.



## Corresponding analysis keywords

- [CONCRETE TENSION DAMAGE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-concretetensiondamage.htm?ContextScope=all#simakey-r-concretetensiondamage)