# SpringDashpotToGround object

The SpringDashpotToGround object defines springs and/or dashpots between points and ground on a part or an assembly region.

The SpringDashpotToGround object is derived from the [SpringDashpot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-springdashpotpyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.springDashpots[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.springDashpots[name]
```

## SpringDashpotToGround(...)



This method creates a SpringDashpotToGround object.



### Path

```
mdb.models[name].parts[name].engineeringFeatures.SpringDashpotToGround
mdb.models[name].rootAssembly.engineeringFeatures\
.SpringDashpotToGround
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the springs and/or dashpots are applied.

- *dof*

  An Int specifying the degree of freedom associated with the spring and dashpot behaviors.

### Optional arguments

- *orientation*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local directions for the spring and/or dashpot. If *orientation*=None, the spring and/or dashpot data are defined in the global coordinate system. The default value is None.

- *springBehavior*

  A Boolean specifying whether to apply spring behavior to the selected points. The default value is OFF.At least one of the arguments *springBehavior*=ON or *dashpotBehavior*=ON must be specified.

- *dashpotBehavior*

  A Boolean specifying whether to apply dashpot behavior to the selected points. The default value is OFF.At least one of the arguments *springBehavior*=ON or *dashpotBehavior*=ON must be specified.

- *springStiffness*

  A Float specifying the force per relative displacement for the spring. The default value is 0.0.

- *dashpotCoefficient*

  A Float specifying the force per relative velocity for the dashpot. The default value is 0.0.

### Return value

A SpringDashpotToGround object.

### Exceptions

None.



## setValues(...)



This method modifies the SpringDashpotToGround object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SpringDashpotToGround ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-springdashpottogroundpyc.htm?ContextScope=all#simaker-springdashpottogroundspringdashpottogroundpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The SpringDashpotToGround object has members with the same names and descriptions as the arguments to the [SpringDashpotToGround ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-springdashpottogroundpyc.htm?ContextScope=all#simaker-springdashpottogroundspringdashpottogroundpyc)method.

In addition, the SpringDashpotToGround object has the following member:

- *suppressed*

  A Boolean specifying whether the spring/dashpot is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [ELEMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-element.htm?ContextScope=all#simakey-r-element), TYPE=SPRING1
- [ELEMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-element.htm?ContextScope=all#simakey-r-element), TYPE=DASHPOT1
- [SPRING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-spring.htm?ContextScope=all#simakey-r-spring)
- [DASHPOT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-dashpot.htm?ContextScope=all#simakey-r-dashpot)