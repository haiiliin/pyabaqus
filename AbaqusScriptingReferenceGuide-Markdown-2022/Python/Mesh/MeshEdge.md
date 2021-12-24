# MeshEdge object

The MeshEdge object refers to an element edge. It has no constructor or members. A MeshEdge object can be accessed via a [MeshEdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) or a repository on a part or part instance.

## Access

```
import part
mdb.models[name].parts[name].elemEdges[i]
mdb.models[name].parts[name].elementEdges[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].elemEdges[i]
mdb.models[name].rootAssembly.allInstances[name].elementEdges[i]
mdb.models[name].rootAssembly.instances[name].elemEdges[i]
mdb.models[name].rootAssembly.instances[name].elementEdges[i]
```

## getElements()



This method returns a tuple of elements that share the element edge.



### Arguments

None.

### Return value

A tuple of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getElementsViaTopology()



This method returns an array of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects that are obtained by recursively finding adjacent elements via topology.



### Optional arguments

- *domain*

  A MeshElementArray object specifying the domain to include in the search. By default, all elements in the mesh are included.

### Return value

A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object, which is a sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getNodesViaTopology()



This method returns an array of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects that lie along element edges topologically in line with the element edge.



### Optional arguments

- *domain*

  A MeshElementArray object specifying the domain to include in the search. By default, all elements in the mesh are included.

### Return value

A [MeshNodeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object, which is a sequence of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getElemFaces()



This method returns a tuple of unique [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects that share the element edge.



### Arguments

None.

### Return value

A tuple of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getNodes()



This method returns a tuple of nodes on the element edge.



### Arguments

None.

### Return value

A tuple of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## Members

The MeshEdge object has no members.