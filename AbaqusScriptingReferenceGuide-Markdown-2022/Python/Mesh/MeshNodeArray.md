# MeshNodeArray object

The MeshNodeArray is a sequence of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

## Access

```
import part
mdb.models[name].parts[name].allInternalSets[name].nodes
mdb.models[name].parts[name].allInternalSurfaces[name].nodes
mdb.models[name].parts[name].allSets[name].nodes
mdb.models[name].parts[name].allSurfaces[name].nodes
mdb.models[name].parts[name].nodes
mdb.models[name].parts[name].retainedNodes
mdb.models[name].parts[name].sets[name].nodes
mdb.models[name].parts[name].surfaces[name].nodes
import assembly
mdb.models[name].rootAssembly.allInstances[name].nodes
mdb.models[name].rootAssembly.allInstances[name].sets[name].nodes
mdb.models[name].rootAssembly.allInstances[name].surfaces[name].nodes
mdb.models[name].rootAssembly.allInternalSets[name].nodes
mdb.models[name].rootAssembly.allInternalSurfaces[name].nodes
mdb.models[name].rootAssembly.allSets[name].nodes
mdb.models[name].rootAssembly.allSurfaces[name].nodes
mdb.models[name].rootAssembly.instances[name].nodes
mdb.models[name].rootAssembly.instances[name].sets[name].nodes
mdb.models[name].rootAssembly.instances[name].surfaces[name].nodes
mdb.models[name].rootAssembly.modelInstances[i].nodes
mdb.models[name].rootAssembly.modelInstances[i].sets[name].nodes
mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].nodes
mdb.models[name].rootAssembly.nodes
mdb.models[name].rootAssembly.sets[name].nodes
mdb.models[name].rootAssembly.surfaces[name].nodes
```

## MeshNodeArray(...)



This method creates a MeshNodeArray object.



### Path

mesh.MeshNodeArray

### Required arguments

- *nodes*

  A list of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Optional arguments

None.

### Return value

A MeshNodeArray object.

### Exceptions

None.



## getFromLabel(...)



This method returns the object in the MeshNodeArray with the given label.



### Required arguments

- *label*

  An Int specifying the label of the object.

### Optional arguments

None.

### Return value

A [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object.

### Exceptions

None.



## getSequenceFromMask(...)



This method returns the objects in the MeshNodeArray identified using the specified *mask*. This command is generated when the [JournalOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-journaloptionspyc.htm?ContextScope=all) are set to COMPRESSEDINDEX. When a large number of objects are involved, this method is highly efficient.



### Required arguments

- *mask*

  A String specifying the object or objects.

### Optional arguments

None.

### Return value

A MeshNodeArray object.

### Exceptions

None.



## getMask()



This method returns a string specifying the object or objects.



### Arguments

None.

### Return value

A String specifying the object or objects.

### Exceptions

None.



## getByBoundingBox(...)



This method returns an array of nodes that lie within the specified bounding box.



### Required arguments

None.

### Optional arguments

- *xMin*

  A float specifying the minimum X boundary of the bounding box.

- *yMin*

  A float specifying the minimum Y boundary of the bounding box.

- *zMin*

  A float specifying the minimum Z boundary of the bounding box.

- *xMax*

  A float specifying the maximum X boundary of the bounding box.

- *yMax*

  A float specifying the maximum Y boundary of the bounding box.

- *zMax*

  A float specifying the maximum Z boundary of the bounding box.

### Return value

A MeshNodeArray object, which is a sequence of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getByBoundingCylinder(...)



This method returns an array of node objects that lie within the specified bounding cylinder.



### Required arguments

- *center1*

  A tuple of the X-, Y-, and Z-coordinates of the center of the first end of the cylinder.

- *center2*

  A tuple of the X-, Y-, and Z-coordinates of the center of the second end of the cylinder.

- *radius*

  A float specifying the radius of the cylinder.

### Optional arguments

None.

### Return value

A MeshNodeArray object, which is a sequence of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getByBoundingSphere(...)



This method returns an array of node objects that lie within the specified bounding sphere.



### Required arguments

- *center*

  A tuple of the X-, Y-, and Z-coordinates of the center of the sphere.

- *radius*

  A float specifying the radius of the sphere.

### Optional arguments

None.

### Return value

A MeshNodeArray object, which is a sequence of [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getBoundingBox()



This method returns a dictionary of two tuples representing minimum and maximum boundary values of the bounding box of the minimum size containing the node sequence.



### Arguments

None.

### Return value

A Dictionary object with the following items:

*low*: a tuple of three floats representing the minimum x, y and z boundary values of the bounding box.

*high*: a tuple of three floats representing the maximum x, y and z boundary values of the bounding box.



## getClosest()



This method returns the node or nodes closest to the given point or set of points.



### Required arguments

- *coordinates*

  A point defined by x, y, and z values or a list of such points.

### Optional arguments

- *numToFind*

  The number of nodes to find for each given point. For example, if *numToFind* is 2, then the 2 closest points, if available and within *searchTolerance*, will be returned in order of proximity for each input point. The default is 1.

- *searchTolerance*

  A float specifying a search radius for each point. By default, no search radius is defined, and all nodes in the sequence will be searched.

### Return value

A MeshNode, or a list of MeshNode objects, or a list of lists of MeshNode objects, depending on the number of points given and the number of nodes requested.

### Exceptions

None.



## sequenceFromLabels(...)



This method returns the objects in the MeshNodeArray identified using the specified labels.



### Required arguments

- *labels*

  A sequence of Ints specifying the labels.

### Optional arguments

None.

### Return value

A MeshNodeArray object.

### Exceptions

- An exception occurs if the resulting sequence is empty.

  Error: The mask results in an empty sequence



## Members

The MeshNodeArray object has no members.