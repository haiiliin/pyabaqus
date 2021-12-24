# DiscreteFastener object

The DiscreteFastener object defines a discrete fastener.

The DiscreteFastener object is derived from the [Fastener](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fastenerpyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.fasteners[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.fasteners[name]
```

## DiscreteFastener(...)



This method creates a DiscreteFastener object. Although the constructor is available both for parts and for the assembly, DiscreteFastener objects are currently supported only under the assembly.



### Path

```
mdb.models[name].parts[name].engineeringFeatures.DiscreteFastener
mdb.models[name].rootAssembly.engineeringFeatures.DiscreteFastener
```

### Required arguments

- *name*

  A String specifying the repository key.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the fastener is applied.

- *influenceRadius*

  The SymbolicConstant WHOLE_SURFACE or a Float specifying the coupling influence radius.

### Optional arguments

- *ur1*

  A Boolean specifying whether to constrain rotational displacement component about the 1-direction. The default value is ON.

- *ur2*

  A Boolean specifying whether to constrain rotational displacement component about the 2-direction. The default value is ON.

- *ur3*

  A Boolean specifying whether to constrain rotational displacement component about the 3-direction. The default value is ON.

- *coupling*

  A SymbolicConstant specifying the coupling method used to couple the displacement and rotation of each attachment point to the average motion of the surface nodes within the radius of influence from the fastening point. Possible values are CONTINUUM and STRUCTURAL. The default value is CONTINUUM.

- *weightingMethod*

  A SymbolicConstant specifying the weighting scheme to be used to weight the contribution of the displacements of the surface nodes within the radius of influence to the motion of the fastening point. UNIFORM, LINEAR, QUADRATIC, and CUBIC indicate uniform, linear decreasing, quadratic polynomial decreasing, and cubic polynomial monotonic decreasing weight distributions. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC. The default value is UNIFORM.

- *localCsys*

  None or a [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the local coordinate system of fastener couplings. If *localCsys*=None, couplings are defined in the global coordinate system. When this member is queried, it returns an Int. The default value is None.

### Return value

A DiscreteFastener object.

### Exceptions

None.



## setValues(...)



This method modifies the DiscreteFastener object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DiscreteFastener ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefastenerpyc.htm?ContextScope=all#simaker-discretefastenerdiscretefastenerpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The DiscreteFastener object has members with the same names and descriptions as the arguments to the [DiscreteFastener ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefastenerpyc.htm?ContextScope=all#simaker-discretefastenerdiscretefastenerpyc)method.

In addition, the DiscreteFastener object has the following member:

- *suppressed*

  A Boolean specifying whether the fastener is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [COUPLING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-coupling.htm?ContextScope=all#simakey-r-coupling), [DISTRIBUTING](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-distributing.htm?ContextScope=all#simakey-r-distributing)