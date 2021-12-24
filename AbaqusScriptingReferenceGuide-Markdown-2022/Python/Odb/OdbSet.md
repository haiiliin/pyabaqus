# OdbSet object

The set objects are used to identify regions of a model.

## Access

```
import odbAccess
session.odbs[name].parts[name].elementSets[name]
session.odbs[name].parts[name].nodeSets[name]
session.odbs[name].parts[name].surfaces[name]
session.odbs[name].rootAssembly.elementSets[name]
session.odbs[name].rootAssembly.instances[name].elementSets[name]
session.odbs[name].rootAssembly.instances[name].nodeSets[name]
session.odbs[name].rootAssembly.instances[name].surfaces[name]
session.odbs[name].rootAssembly.nodeSets[name]
session.odbs[name].rootAssembly.surfaces[name]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.elementSets[name]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.nodeSets[name]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.surfaces[name]
```

## NodeSet(...)



This method creates a node set from an array of [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) objects (for part instance-level sets) or from a sequence of arrays of [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) objects (for assembly-level sets).



### Path

session.odbs[*name*].parts[*name*].NodeSet

session.odbs[*name*].rootAssembly.instances[*name*].NodeSet

session.odbs[*name*].rootAssembly.NodeSet

### Required arguments

- *name*

  A String specifying the name of the set and the repository key.

- *nodes*

  A sequence of [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) objects. For example, for a part:`nodes=part1.nodes[1:5]`For an assembly:`nodes=(instance1.nodes[6:7], instance2.nodes[1:5])`

### Optional arguments

None.

### Return value

An OdbSet object.

### Exceptions

InvalidNameError.



## NodeSetFromNodeLabels(...)



This method creates a node set from a sequence of node labels.



### Path

session.odbs[*name*].parts[*name*].NodeSetFromNodeLabels

session.odbs[*name*].rootAssembly.instances[*name*].NodeSetFromNodeLabels

session.odbs[*name*].rootAssembly.NodeSetFromNodeLabels

### Required arguments

- *name*

  A String specifying the name of the set and the repository key.

- *nodeLabels*

  A sequence of node labels. A node label is a sequence of Int node identifiers. For example, for a part:`nodeLabels=(2,3,5,7)`For an assembly:`nodeLabels=(('Instance-1', (2,3,5,7)), ('Instance-2', (1,2,3)))`

### Optional arguments

None.

### Return value

An OdbSet object.

### Exceptions

InvalidNameError.



## ElementSet(...)



This method creates an element set from an array of [OdbMeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) objects (for part instance-level sets) or from a sequence of arrays of [OdbMeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) objects (for assembly-level sets).



### Path

session.odbs[*name*].parts[*name*].ElementSet

session.odbs[*name*].rootAssembly.instances[*name*].ElementSet

### Required arguments

- *name*

  A String specifying the name of the set and the repository key.

- *elements*

  A sequence of [OdbMeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) objects. For example, for a part:`elements=instance1.elements[1:5]`For an assembly:`elements=(instance1.elements[1:5], instance2.elements[1:5])`

### Optional arguments

None.

### Return value

An OdbSet object.

### Exceptions

InvalidNameError.



## ElementSetFromElementLabels(...)



This method creates an element set from a sequence of element labels.



### Path

session.odbs[*name*].parts[*name*].ElementSetFromElementLabels

session.odbs[*name*].rootAssembly.instances[*name*].ElementSetFromElementLabels

session.odbs[*name*].rootAssembly.ElementSetFromElementLabels

### Required arguments

- *name*

  A String specifying the name of the set and the repository key.

- *elementLabels*

  A sequence of element labels. An element label is a sequence of Int element identifiers. For example, for a part:`elementLabels=(2,3,5,7)`For an assembly:`elementLabels=(('Instance-1', (2,3,5,7)), ('Instance-2', (1,2,3)))`

### Optional arguments

None.

### Return value

An OdbSet object.

### Exceptions

InvalidNameError.



## MeshSurface(...)



This method creates a surface from the element and side identifiers for the assembly.



### Path

session.odbs[*name*].parts[*name*].MeshSurface

session.odbs[*name*].rootAssembly.instances[*name*].MeshSurface

session.odbs[*name*].rootAssembly.MeshSurface

### Required arguments

- *name*

  A String specifying the name of the set and the repository key.

- *meshSurfaces*

  A sequence of sequences. Each sequence consists of an element sequence and a side identifier. The possible side identifiers depend on the type of element, as described in the following table:

  | Sequence of elements             | Side identifiers                         |
  | -------------------------------- | ---------------------------------------- |
  | Solid elements                   | FACE1, FACE2, FACE3, FACE4, FACE5, FACE6 |
  | Three-dimensional shell elements | SIDE1, SIDE2                             |
  | Two-dimensional elements         | FACE1, FACE2, FACE3, FACE4               |
  | Wire elements                    | END, END2                                |

  For example:

  ```
  side1Elements=instance1.elements[217:218]
  side2Elements=instance2.elements[100:105]
  assembly.MeshSurface(name='Surf-1',
  meshSurfaces=((side1Elems,SIDE1),
  (side2Elems,SIDE2)))
  ```

### Optional arguments

None.

### Return value

An OdbSet object.

### Exceptions

InvalidNameError.



## MeshSurfaceFromElsets(...)



This method creates a mesh surface from a sequence of element sets.



### Path

session.odbs[*name*].parts[*name*].MeshSurfaceFromElsets

session.odbs[*name*].rootAssembly.instances[*name*].MeshSurfaceFromElsets

session.odbs[*name*].rootAssembly.MeshSurfaceFromElsets

### Required arguments

- *name*

  A String specifying the name of the set and the repository key.

- *elementSetSeq*

  A sequence of element sets. For example,`elementSetSeq=((elset1,SIDE1),(elset2,SIDE2))`where `elset1=session.odbs[name].rootAssembly.elementSets['Clutch'] `and `SIDE1` and `SIDE2` indicate the side of the element set.

### Optional arguments

None.

### Return value

An OdbSet object.

### Exceptions

InvalidNameError.



## MeshSurfaceFromLabels(...)



This method creates a mesh surface from a sequence of surface labels.



### Path

session.odbs[*name*].parts[*name*].MeshSurfaceFromLabels

session.odbs[*name*].rootAssembly.instances[*name*].MeshSurfaceFromLabels

session.odbs[*name*].rootAssembly.MeshSurfaceFromLabels

### Required arguments

- *name*

  A String specifying the name of the set and the repository key.

- *surfaceLabels*

  A sequence of surface labels. For example,`surfaceLabels=(('Instance-1', ((10, FACE1), (11, FACE2))),  ('Instance-2', ((10, FACE3), (12, FACE4))))`where `10` is an element number and `FACE1` indicates the side of the element.

### Optional arguments

None.

### Return value

An OdbSet object.

### Exceptions

InvalidNameError.



## Members

The OdbSet object can have the following members:

- *name*

  A String specifying the name of the set and the repository key.

- *instanceNames*

  A tuple of Strings specifying the namespaces for the nodes, elements, and faces; None if the set is on a Part or an [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) object.

- *nodes*

  An [OdbMeshNodeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) object specifying the nodes of an OdbSet. If a set spans more than one part instance, this member is a sequence of sequences for each part instance.

- *elements*

  An [OdbMeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) object specifying the elements of an OdbSet. If a set spans more than one part instance, this member is a sequence of sequences for each part instance.

- *faces*

  A tuple of SymbolicConstants specifying the element face. If a set spans more than one part instance, this member is a sequence of sequences for each part instance.

- *instances*

  A repository of an [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) object.

- *isInternal*

  A Boolean specifying whether the set is internal.