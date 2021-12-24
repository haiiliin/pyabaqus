# TransverseShearShell object

The TransverseShearShell object defines the transverse shear stiffness properties of a shell section.

## Access

```
import section
mdb.models[name].sections[name].transverseShear
import odbSection
session.odbs[name].sections[name].transverseShear
```

## TransverseShearShell(...)



This method creates a TransverseShearShell object.



### Path

```
mdb.models[name].sections[name].TransverseShearShell
session.odbs[name].sections[name].TransverseShearShell
```

### Required arguments

- *k11*

  A Float specifying the shear stiffness of the section in the first direction.

- *k22*

  A Float specifying the shear stiffness of the section in the second direction.

- *k12*

  A Float specifying the coupling term in the shear stiffness of the section.

### Optional arguments

None.

### Return value

A TransverseShearShell object.

### Exceptions

None.



## setValues(...)



This method modifies the TransverseShearShell object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TransverseShearShell ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-transverseshearshellpyc.htm?ContextScope=all#simaker-transverseshearshelltransverseshearshellpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The TransverseShearShell object has members with the same names and descriptions as the arguments to the [TransverseShearShell ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-transverseshearshellpyc.htm?ContextScope=all#simaker-transverseshearshelltransverseshearshellpyc)method.



## Corresponding analysis keywords

- [TRANSVERSE SHEAR STIFFNESS](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-transverseshearstiffness.htm?ContextScope=all#simakey-r-transverseshearstiffness)