# Ornl object

The Ornl object specifies the constitutive model developed by Oak Ridge National Laboratory.

## Access

```
import material
mdb.models[name].materials[name].creep.ornl
mdb.models[name].materials[name].plastic.ornl
import odbMaterial
session.odbs[name].materials[name].creep.ornl
session.odbs[name].materials[name].plastic.ornl
```

## Ornl(...)



This method creates an Ornl object.



### Path

```
mdb.models[name].materials[name].creep.Ornl
mdb.models[name].materials[name].plastic.Ornl
session.odbs[name].materials[name].creep.Ornl
session.odbs[name].materials[name].plastic.Ornl
```

### Required arguments

None.

### Optional arguments

- *a*

  A Float specifying the saturation rates for kinematic shift caused by creep strain, as defined by Equation (15) of Section 4.3.3–3 of the Nuclear Standard. The default value corresponds to that section of the Standard. Set *a*=0.0 to use the 1986 revision of the Standard. The default value is 0.3.

- *h*

  None or a Float specifying the rate of kinematic shift with respect to creep strain [Equation (7) of Section 4.3.2–1 of the Nuclear Standard]. If *h*=None, the value of *h* is determined according to Section 4.3.3–3 of the 1981 revision of the Standard. Set *h*=0.0 to use the 1986 revision of the Standard. The default value is None.

- *reset*

  A Boolean specifying whether to invoke the optional αα reset procedure described in Section 4.3.5 of the Nuclear Standard. The default value is OFF.

### Return value

An Ornl object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Ornl object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Ornl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ornlpyc.htm?ContextScope=all#simaker-ornlornlpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Ornl object has members with the same names and descriptions as the arguments to the [Ornl ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ornlpyc.htm?ContextScope=all#simaker-ornlornlpyc)method.



## Corresponding analysis keywords

- [ORNL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-ornl.htm?ContextScope=all#simakey-r-ornl)