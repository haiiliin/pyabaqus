# MeshElementArray object

The MeshElementArray is a sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

## Access

```
import part
mdb.models[name].parts[name].allInternalSets[name].elements
mdb.models[name].parts[name].allInternalSurfaces[name].elements
mdb.models[name].parts[name].allSets[name].elements
mdb.models[name].parts[name].allSurfaces[name].elements
mdb.models[name].parts[name].elements
mdb.models[name].parts[name].sets[name].elements
mdb.models[name].parts[name].surfaces[name].elements
import assembly
mdb.models[name].rootAssembly.allInstances[name].elements
mdb.models[name].rootAssembly.allInstances[name].sets[name].elements
mdb.models[name].rootAssembly.allInstances[name].surfaces[name].elements
mdb.models[name].rootAssembly.allInternalSets[name].elements
mdb.models[name].rootAssembly.allInternalSurfaces[name].elements
mdb.models[name].rootAssembly.allSets[name].elements
mdb.models[name].rootAssembly.allSurfaces[name].elements
mdb.models[name].rootAssembly.elements
mdb.models[name].rootAssembly.instances[name].elements
mdb.models[name].rootAssembly.instances[name].sets[name].elements
mdb.models[name].rootAssembly.instances[name].surfaces[name].elements
mdb.models[name].rootAssembly.modelInstances[i].elements
mdb.models[name].rootAssembly.modelInstances[i].sets[name].elements
mdb.models[name].rootAssembly.modelInstances[i].surfaces[name]\
.elements
mdb.models[name].rootAssembly.sets[name].elements
mdb.models[name].rootAssembly.surfaces[name].elements
```

## MeshElementArray(...)



This method creates a MeshElementArray object.



### Path

mesh.MeshElementArray

### Required arguments

- *elements*

  A list of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Optional arguments

None.

### Return value

A MeshElementArray object.

### Exceptions

None.



## getFromLabel(...)



This method returns the object in the MeshElementArray with the given label.



### Required arguments

- *label*

  An Int specifying the label of the object.

### Optional arguments

None.

### Return value

A [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object.

### Exceptions

None.



## getSequenceFromMask(...)



This method returns the objects in the MeshElementArray identified using the specified *mask*. This command is generated when the [JournalOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-journaloptionspyc.htm?ContextScope=all) are set to COMPRESSEDINDEX. When a large number of objects are involved, this method is highly efficient.



### Required arguments

- *mask*

  A String specifying the object or objects.

### Optional arguments

None.

### Return value

A MeshElementArray object.

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



## getExteriorEdges()



This method returns the exterior element edges for 2D/shell elements in the MeshElementArray. These are edges referenced by exactly one element in the sequence. Nothing is returned if the sequence contains no topologically 2D/shell elements.



### Arguments

None.

### Return value

A MeshEdgeArray object specifying the element edges on the exterior.

### Exceptions

None.



## getExteriorFaces()



This method returns the exterior element faces for solid elements in the MeshElementArray. These are faces referenced by exactly one element in the sequence. Nothing is returned if the sequence contains no topologically solid elements.



### Arguments

None.

### Return value

A MeshFaceArray object specifying the element faces on the exterior.

### Exceptions

None.



## getByBoundingBox(...)



This method returns an array of element objects that lie within the specified bounding box.



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

A MeshElementArray object, which is a sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getByBoundingCylinder(...)



This method returns an array of element objects that lie within the specified bounding cylinder.



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

A MeshElementArray object, which is a sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getByBoundingSphere(...)



This method returns an array of element objects that lie within the specified bounding sphere.



### Required arguments

- *center*

  A tuple of the X-, Y-, and Z-coordinates of the center of the sphere.

- *radius*

  A float specifying the radius of the sphere.

### Optional arguments

None.

### Return value

A MeshElementArray object, which is a sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.



## getBoundingBox()



This method returns a dictionary of two tuples representing minimum and maximum boundary values of the bounding box of the minimum size containing the element sequence.



### Arguments

None.

### Return value

A Dictionary object with the following items:

*low*: a tuple of three floats representing the minimum x, y, and z boundary values of the bounding box.

*high*: a tuple of three floats representing the maximum x, y, and z boundary values of the bounding box.

### Exceptions

None.



## sequenceFromLabels(...)



This method returns the objects in the MeshElementArray identified using the specified labels.



### Required arguments

- *labels*

  A sequence of Ints specifying the labels.

### Optional arguments

None.

### Return value

A MeshElementArray object.

### Exceptions

- An exception occurs if the resulting sequence is empty.

  Error: The mask results in an empty sequence



## Members

The MeshElementArray object has no members.