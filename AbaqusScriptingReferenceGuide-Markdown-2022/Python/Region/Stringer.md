# Stringer object

The Stringer object stores information on stringer reinforcements created on entities.

## Access

```
import part
mdb.models[name].parts[name].stringers[name]
import assembly
mdb.models[name].rootAssembly.allInstances[name].stringers[name]
mdb.models[name].rootAssembly.instances[name].stringers[name]
mdb.models[name].rootAssembly.stringers[name]
```

## Stringer(...)



This method creates a stringer from a sequence of objects in a model database. At least one of the optional arguments needs to be specified.



### Path

mdb.models[*name*].parts[*name*].Stringer

### Required arguments

- *name*

  A String specifying the repository key. The default value is an empty string.

### Optional arguments

- *edges*

  A sequence of Edge objects specifying the edges on which stringers should be created. Applicable to three and two dimensional parts.

- *elementEdges*

  A sequence of MeshEdge objects specifying the mesh edges on which stringers should be created. Applicable to three and two dimensional parts.

### Return value

A Stringer object.

### Exceptions

InvalidNameError.



## EditStringer(...)



This method modifies underlying entities of the selected stringer. At least one of the optional arguments needs to be specified.



### Path

mdb.models[*name*].parts[*name*].EditStringer

### Required arguments

- *name*

  A String specifying the repository key. The default value is an empty string.

### Optional arguments

- *edges*

  A sequence of Edge objects specifying the edges on which stringers should be created. Applicable to three and two dimensional parts.

- *elementEdges*

  A sequence of MeshEdge objects specifying the mesh edges on which stringers should be created. Applicable to three and two dimensional parts.

### Return value

A Stringer object.

### Exceptions

InvalidNameError.



## Members

The Stringer object has the following members:

- *elements*

  A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object.

- *edges*

  An [EdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object.