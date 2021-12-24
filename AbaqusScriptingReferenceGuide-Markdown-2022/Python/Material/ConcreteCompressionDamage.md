# ConcreteCompressionDamage object

The ConcreteCompressionDamage object specifies hardening for the concrete damaged plasticity model.

## Access

```
import material
mdb.models[name].materials[name].concreteDamagedPlasticity.concreteCompressionDamage
import odbMaterial
session.odbs[name].materials[name].concreteDamagedPlasticity.concreteCompressionDamage
```

## ConcreteCompressionDamage(...)



This method creates a ConcreteCompressionDamage object.



### Path

```
mdb.models[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionDamage
session.odbs[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionDamage
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *tensionRecovery*

  A Float specifying the value of the stiffness recovery factor, wtwt, that determines the amount of tension stiffness that is recovered as loading changes from compression to tension. The default value is 0.0.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- Compressive damage variable, dc.
- Inelastic (crushing) strain, ϵci⁢n.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ConcreteCompressionDamage object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ConcreteCompressionDamage object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConcreteCompressionDamage ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretecompressiondamagepyc.htm?ContextScope=all#simaker-concretecompressiondamageconcretecompressiondamagepyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ConcreteCompressionDamage object has members with the same names and descriptions as the arguments to the [ConcreteCompressionDamage ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretecompressiondamagepyc.htm?ContextScope=all#simaker-concretecompressiondamageconcretecompressiondamagepyc)method.



## Corresponding analysis keywords

- [CONCRETE COMPRESSION DAMAGE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-concretecompressiondamage.htm?ContextScope=all#simakey-r-concretecompressiondamage)