# NonstructuralMass object

The NonstructuralMass object defines the mass contribution from nonstructural features into the model.

The NonstructuralMass object is derived from the [Inertia](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiapyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.inertias[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.inertias[name]
```

## NonstructuralMass(...)



This method creates a NonstructuralMass object.



### Path

```
mdb.models[name].parts[name].engineeringFeatures.NonstructuralMass
mdb.models[name].rootAssembly.engineeringFeatures.NonstructuralMass
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the mass is applied.

- *units*

  A SymbolicConstant specifying the units used to specify the nonstructural mass. Possible values are TOTAL_MASS, MASS_PER_VOLUME, MASS_PER_AREA, and MASS_PER_LENGTH.

- *magnitude*

  A Float specifying the mass magnitude.

### Optional arguments

- *distribution*

  A SymbolicConstant specifying the distribution of the nonstructural mass. Possible values are MASS_PROPORTIONAL and VOLUME_PROPORTIONAL. The default value is MASS_PROPORTIONAL.The *distribution* argument applies only when *units*=TOTAL_MASS.

### Return value

A NonstructuralMass object.

### Exceptions

None.



## setValues(...)



This method modifies the NonstructuralMass object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [NonstructuralMass ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nonstructuralmasspyc.htm?ContextScope=all#simaker-nonstructuralmassnonstructuralmasspyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The NonstructuralMass object has members with the same names and descriptions as the arguments to the [NonstructuralMass ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nonstructuralmasspyc.htm?ContextScope=all#simaker-nonstructuralmassnonstructuralmasspyc)method.

In addition, the NonstructuralMass object has the following member:

- *suppressed*

  A Boolean specifying whether the inertia is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [NONSTRUCTURAL MASS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-nonstructuralmass.htm?ContextScope=all#simakey-r-nonstructuralmass)