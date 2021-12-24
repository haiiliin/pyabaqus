# LeafFromConstraintNames object

The LeafFromConstraintNames object can be used whenever a Leaf object is expected as an argument.

A [Leaf object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all#simaker-c-leafpyc) is used used to specify the items in a display group. Leaf objects are constructed as temporary objects that are used as arguments to DisplayGroup ([DisplayGroup object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all#simaker-c-displaygrouppyc)) commands.

The LeafFromConstraintNames object is derived from the Leaf object.

## Access

```
import displayGroupOdbToolset
```

## LeafFromConstraintNames(...)



This method creates a Leaf object from a sequence of constraint objects. Leaf objects specify the items in a display group.



### Path

```
LeafFromConstraintNames
```

### Required arguments

- *name*

  A sequence of tuples of name objects.

- *type*

  A SymbolicConstant specifying the Leaf type. Possible values are TIE, SHELL_TO_SOLID_COUPLING, DISTRIBUTING_COUPLING, KINEMATIC_COUPLING, RIGID_BODY, and MPC.

### Optional arguments

None.

### Return value

A LeafFromConstraintNames object.

### Exceptions

None.



## Members

The LeafFromConstraintNames object has members with the same names and descriptions as the arguments to the [LeafFromConstraintNames](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leaffromconstraintnamespyc.htm?ContextScope=all#simaker-leaffromconstraintnamesleaffromconstraintnamespyc) method.

In addition, the LeafFromConstraintNames object has the following member:

- *leafType*

  A SymbolicConstant specifying the leaf type. Possible values are TIE, SHELL_TO_SOLID_COUPLING, DISTRIBUTING_COUPLING, KINEMATIC_COUPLING, RIGID_BODY, and MPC.