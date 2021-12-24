# VertexArray object

The VertexArray is a sequence of [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects. If the part is modified, then VertexArray must be updated for that part.

## Access

```
import part
mdb.models[name].parts[name].allInternalSets[name].vertices
mdb.models[name].parts[name].allSets[name].vertices
mdb.models[name].parts[name].sets[name].vertices
mdb.models[name].parts[name].vertices
import assembly
mdb.models[name].rootAssembly.allInstances[name].sets[name].vertices
mdb.models[name].rootAssembly.allInstances[name].vertices
mdb.models[name].rootAssembly.allInternalSets[name].vertices
mdb.models[name].rootAssembly.allSets[name].vertices
mdb.models[name].rootAssembly.instances[name].sets[name].vertices
mdb.models[name].rootAssembly.instances[name].vertices
mdb.models[name].rootAssembly.modelInstances[i].sets[name].vertices
mdb.models[name].rootAssembly.modelInstances[i].vertices
mdb.models[name].rootAssembly.sets[name].vertices
mdb.models[name].rootAssembly.vertices
```

## VertexArray(...)



This method creates a VertexArray object.



### Path

part.VertexArray

### Required arguments

- *vertices*

  A list of [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects.

### Optional arguments

None.

### Return value

A VertexArray object.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## findAt(...)



This method returns the object or objects in the VertexArray located at the given coordinates.

findAt initially uses the ACIS tolerance of 1E-6. As a result, findAt returns any [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary point. If nothing is found, findAt uses the tolerance for imprecise geometry (applicable only for imprecise geometric entities).

findAt will always try to find objects among all the vertices in the part or assembly instance and will not restrict itself to a subset even if the VertexArray represents such subset.



### Required arguments

- *coordinates*

  A sequence of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the object to find.findAt returns either a Vertex object or a sequence of Vertex objects based on the type of input.If *coordinates* is a sequence of Floats, findAt returns the Vertex object at that point.If you omit the *coordinates* keyword argument, findAt accepts as arguments a sequence of sequence of floats in the following format:`verts = v.findAt(((20.19686, -169.513997, 27.798593), ),                 ((19.657627, -167.295749, 27.056402), ),                 ((18.274129, -157.144741, 25.15218), ))`

### Optional arguments

- *printWarning*

  A Boolean specifying whether a message is to be printed to the CLI if no entity is found at the specified location. The default value is True.

### Return value

A Vertex object or a sequence of Vertex objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getSequenceFromMask(...)



This method returns the object or objects in the VertexArray identified using the specified *mask*. This command is generated when the [JournalOptions](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-journaloptionspyc.htm?ContextScope=all) are set to COMPRESSEDINDEX. When a large number of objects are involved, this method is highly efficient.



### Required arguments

- *mask*

  A String specifying the object or objects.

### Optional arguments

None.

### Return value

A [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object or a sequence of [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getMask()



This method returns a string specifying the object or objects.



### Arguments

None.

### Return value

A String specifying the object or objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getByBoundingBox(...)



This method returns an array of vertex objects that lie within the specified bounding box.



### Required arguments

None.

### Optional arguments

- *xMin*

  A float specifying the minimum *X*-boundary of the bounding box.

- *yMin*

  A float specifying the minimum *Y*-boundary of the bounding box.

- *zMin*

  A float specifying the minimum *Z*-boundary of the bounding box.

- *xMax*

  A float specifying the maximum *X*-boundary of the bounding box.

- *yMax*

  A float specifying the maximum *Y*-boundary of the bounding box.

- *zMax*

  A float specifying the maximum *Z*-boundary of the bounding box.

### Return value

A VertexArray object, which is a sequence of [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getByBoundingCylinder(...)



This method returns an array of vertex objects that lie within the specified bounding cylinder.



### Required arguments

- *center1*

  A tuple of the *X*-, *Y*-, and *Z*-coordinates of the center of the first end of the cylinder.

- *center2*

  A tuple of the *X*-, *Y*-, and *Z*-coordinates of the center of the second end of the cylinder.

- *radius*

  A float specifying the radius of the cylinder.

### Optional arguments

None.

### Return value

A VertexArray object, which is a sequence of [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getByBoundingSphere(...)



This method returns an array of vertex objects that lie within the specified bounding sphere.



### Required arguments

- *center*

  A tuple of the *X*-, *Y*-, and *Z*-coordinates of the center of the sphere.

- *radius*

  A float specifying the radius of the sphere.

### Optional arguments

None.

### Return value

A VertexArray object, which is a sequence of [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getBoundingBox()



This method returns a dictionary of two tuples representing minimum and maximum boundary values of the bounding box of the minimum size containing the vertex sequence.



### Arguments

None.

### Return value

A Dictionary object with the following items:

*low*: a tuple of three floats representing the minimum *X*-, *Y*-, and *Z*-boundary values of the bounding box.

*high*: a tuple of three floats representing the maximum *X*-, *Y*-, and *Z*-boundary values of the bounding box.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getClosest(...)



This method returns a object or objects in the VertexArray closest to the given set of points, where the given points need not lie on [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) objects in the VertexArray.



### Required arguments

- *coordinates*

  A sequence of a sequence of floats, where each sequence of floats describes the *X*-, *Y*-, and *Z*-coordinates of a point.`r=v.getClosest(coordinates=((20.0,20.0,10.0),(-1.0, -15.0, 15),))``r.keys()``[0, 1]``r[0]``(mdb.models['Model-1'].parts['Part-1'].vertices[0],        (15.7090625762939, 29.1666641235352, 20.0))`

### Optional arguments

- *searchTolerance*

  A double specifying the distance within which the closest object must lie. The default value is half of the parent part/instance size.

### Return value

This method returns a dictionary object. The key to the dictionary object is the position of the input point in the tuple specified in the *coordinates* starting at index 0. If a closest vertex could be found then the value is a sequence consisting of two objects. The first object in the sequence is a [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) that is close to the input point referred to by the key. The second object in the sequence is a sequence of floats that specifies the *X*-, *Y*-, and *Z*-location of the [Vertex](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all). See program listing above.

### Exceptions

- An exception occurs if the resulting sequence is empty.

  Error: The mask results in an empty sequence

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The VertexArray object has no members.