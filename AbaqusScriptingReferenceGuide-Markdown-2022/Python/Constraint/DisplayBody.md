# DisplayBody object

The DisplayBody object defines a constraint such that the specified instance is used for display only and does not take part in the analysis. However it will still be visible during postprocessing and its position at any frame will be defined by the translation and rotation of the specified control points.

The DisplayBody object is derived from the [Constraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].constraints[name]
```

## DisplayBody(...)



This method creates a DisplayBody object.



### Path

```
mdb.models[name].DisplayBody
```

### Required arguments

- *name*

  A String specifying the constraint repository key.

- *instance*

  A [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object specifying the part instance that is to be used for display only.

- *controlPoints*

  A [ModelDotArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modeldotpyc.htm?ContextScope=all) object specifying the motion of the [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all). The control points may be Vertex, ReferencePoint, or MeshNode objects. Their motion will control the motion of the PartInstance. If this argument is set to an empty sequence, the PartInstance will remain fixed in space during the analysis. The sequence can have either one object or three objects.

### Optional arguments

None.

### Return value

A DisplayBody object.

### Exceptions

None.



## setValues(...)



This method modifies the DisplayBody object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DisplayBody ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaybodypyc.htm?ContextScope=all#simaker-displaybodydisplaybodypyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The DisplayBody object has members with the same names and descriptions as the arguments to the [DisplayBody ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaybodypyc.htm?ContextScope=all#simaker-displaybodydisplaybodypyc)method.

In addition, the DisplayBody object has the following member:

- *suppressed*

  A Boolean specifying whether the constraint is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [DISPLAY BODY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-displaybody.htm?ContextScope=all#simakey-r-displaybody)