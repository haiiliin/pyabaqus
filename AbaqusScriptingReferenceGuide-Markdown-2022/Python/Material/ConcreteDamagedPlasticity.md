# ConcreteDamagedPlasticity object

The ConcreteDamagedPlasticity object specifies the concrete damaged plasticity model.

## Access

```
import material
mdb.models[name].materials[name].concreteDamagedPlasticity
import odbMaterial
session.odbs[name].materials[name].concreteDamagedPlasticity
```

## ConcreteDamagedPlasticity(...)



This method creates a ConcreteDamagedPlasticity object.



### Path

```
mdb.models[name].materials[name].ConcreteDamagedPlasticity
session.odbs[name].materials[name].ConcreteDamagedPlasticity
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

### Table data

The table data specify the following:

- Dilation angle, ψ (in degrees) in the p–q plane.
- Flow potential eccentricity, ϵ. The default value is 0.1.
- σb0/σt0σb⁢0/σt⁢0, the ratio of initial equibiaxial compressive yield stress to initial uniaxial compressive yield stress. The default value is 1.16.
- Kc, the ratio of the second stress invariant on the tensile meridian, to that on the compressive meridian, at initial yield for any given value of the pressure invariant p such that the maximum principal stress is negative. The default value is 2/3.
- Viscosity parameter, μ, used for the viscoplastic regularization of the concrete constitutive equations in an Abaqus/Standard analysis. This parameter is ignored in an Abaqus/Explicit analysis. The default value is 0.0.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ConcreteDamagedPlasticity object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ConcreteDamagedPlasticity object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConcreteDamagedPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretedamagedplasticitypyc.htm?ContextScope=all#simaker-concretedamagedplasticityconcretedamagedplasticitypyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The ConcreteDamagedPlasticity object has members with the same names and descriptions as the arguments to the [ConcreteDamagedPlasticity ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretedamagedplasticitypyc.htm?ContextScope=all#simaker-concretedamagedplasticityconcretedamagedplasticitypyc)method.

In addition, the ConcreteDamagedPlasticity object can have the following members:

- *concreteCompressionHardening*

  A [ConcreteCompressionHardening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretecompressionhardeningpyc.htm?ContextScope=all) object.

- *concreteTensionStiffening*

  A [ConcreteTensionStiffening](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretetensionstiffeningpyc.htm?ContextScope=all) object.

- *concreteCompressionDamage*

  A [ConcreteCompressionDamage](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretecompressiondamagepyc.htm?ContextScope=all) object.

- *concreteTensionDamage*

  A [ConcreteTensionDamage](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concretetensiondamagepyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [CONCRETE DAMAGED PLASTICITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-concretedamagedplasticity.htm?ContextScope=all#simakey-r-concretedamagedplasticity)