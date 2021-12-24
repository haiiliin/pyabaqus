# MeshEdgeArray object

The MeshEdgeArray is a sequence of [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) objects.

## Access

```
import part
mdb.models[name].parts[name].elementEdges
import assembly
mdb.models[name].rootAssembly.allInstances[name].elementEdges
mdb.models[name].rootAssembly.instances[name].elementEdges
```

## MeshEdgeArray(...)



This method creates a MeshEdgeArray object.



### Path

mesh.MeshEdgeArray

### Required arguments

- *elemEdges*

  A list of [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) objects.

### Optional arguments

None.

### Return value

A MeshEdgeArray object.

### Exceptions

None.



## getSequenceFromMask(...)



This method returns the objects in the MeshEdgeArray identified using the specified *mask*. When large number of objects are involved, this method is highly efficient.



### Required arguments

- *mask*

  A String specifying the object or objects.

### Optional arguments

None.

### Return value

A MeshEdgeArray object.

### Exceptions

- An exception occurs if the resulting sequence is empty.

  Error: The mask results in an empty sequence



## getMask()



This method returns a string specifying the object or objects.



### Arguments

None.

### Return value

A String specifying the object or objects.

### Exceptions

None.



## Members

The MeshEdgeArray object has no members.