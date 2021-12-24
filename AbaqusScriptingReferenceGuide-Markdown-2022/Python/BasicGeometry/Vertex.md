# Vertex object

Vertices are point regions of geometry.

## Access

```
import part
mdb.models[name].parts[name].allInternalSets[name].vertices[i]
mdb.models[name].parts[name].allSets[name].vertices[i]
mdb.models[name].parts[name].sets[name].vertices[i]
mdb.models[name].parts[name].vertices[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].sets[name].vertices[i]
mdb.models[name].rootAssembly.allInstances[name].vertices[i]
mdb.models[name].rootAssembly.allInternalSets[name].vertices[i]
mdb.models[name].rootAssembly.allSets[name].vertices[i]
mdb.models[name].rootAssembly.instances[name].sets[name].vertices[i]
mdb.models[name].rootAssembly.instances[name].vertices[i]
mdb.models[name].rootAssembly.modelInstances[i].sets[name].vertices[i]
mdb.models[name].rootAssembly.modelInstances[i].vertices[i]
mdb.models[name].rootAssembly.sets[name].vertices[i]
mdb.models[name].rootAssembly.vertices[i]
```

## getEdges()



This method returns a sequence consisting of the edge ids of the edges which share this vertex.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getNodes()



This method returns an array of node objects that are associated with the vertex.



### Arguments

None.

### Return value

A [MeshNodeArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object which is a sequence of [MeshNode](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getElements()



This method returns an array of element objects that are associated with the vertex.



### Arguments

None.

### Return value

A [MeshElementArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object which is a sequence of [MeshElement](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The Vertex object has the following members:

- *index*

  An Int specifying the index of the Vertex in the VertexArray.

- *isReferenceRep*

  A Boolean specifying whether the vertex belongs to the reference representation of the Part or Instance.

- *pointOn*

  A tuple of Floats specifying the *X* -, *Y* -, and *Z* -coordinates of the vertex.

- *featureName*

  A tuple of Floats specifying the name of the feature that created this vertex.

- *instanceName*

  A tuple of Floats specifying the name of the part instance for this vertex (if applicable).