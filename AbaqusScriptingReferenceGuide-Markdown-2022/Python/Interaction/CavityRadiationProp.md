# CavityRadiationProp object

The CavityRadiationProp object is an interaction property that defines emissivity as a function of temperature and field variables.

The CavityRadiationProp object is derived from the [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactionProperties[name]
```

## CavityRadiationProp(...)



This method creates a CavityRadiationProp object.



### Path

```
mdb.models[name].CavityRadiationProp
```

### Required arguments

- *name*

  A String specifying the interaction property repository key.

### Optional arguments

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *property*

  A sequence of sequences of Floats specifying the following:The emissivity, ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if the data depend on field variables.Value of the second field variable.Etc.

### Return value

A CavityRadiationProp object.

### Exceptions

None.



## setValues(...)



This method modifies the CavityRadiationProp object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CavityRadiationProp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cavityradiationproppyc.htm?ContextScope=all#simaker-cavityradiationpropcavityradiationproppyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The CavityRadiationProp object has members with the same names and descriptions as the arguments to the [CavityRadiationProp ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cavityradiationproppyc.htm?ContextScope=all#simaker-cavityradiationpropcavityradiationproppyc)method.



## Corresponding analysis keywords

- [EMISSIVITY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-emissivity.htm?ContextScope=all#simakey-r-emissivity)