# ConcreteCompressionHardening object

The ConcreteCompressionHardening object specifies hardening for the concrete damaged plasticity model.

## Access

```
import material
mdb.models[name].materials[name].concreteDamagedPlasticity.concreteCompressionHardening
import odbMaterial
session.odbs[name].materials[name].concreteDamagedPlasticity.concreteCompressionHardening
```

## ConcreteCompressionHardening(...)



This method creates a ConcreteCompressionHardening object.



### Path

```
mdb.models[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionHardening
session.odbs[name].materials[name].concreteDamagedPlasticity.ConcreteCompressionHardening
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *rate*

  A Boolean specifying whether the data depend on rate. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

- Yield stress in compression, σcσc.
- Inelastic (crushing) strain, ϵinc
- Inelastic (crushing) strain rate, ϵinc
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ConcreteCompressionHardening object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ConcreteCompressionHardening object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConcreteCompressionHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretecompressionhardeningpyc.htm?ContextScope=all#simaker-concretecompressionhardeningconcretecompressionhardpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ConcreteCompressionHardening object has members with the same names and descriptions as the arguments to the [ConcreteCompressionHardening ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretecompressionhardeningpyc.htm?ContextScope=all#simaker-concretecompressionhardeningconcretecompressionhardpyc)method.



## Corresponding analysis keywords

- [CONCRETE COMPRESSION HARDENING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-concretecompressionhardening.htm?ContextScope=all#simakey-r-concretecompressionhardening)