# IgnoredEdge object

An IgnoredEdge object is a one-dimensional region of geometry that has been abstracted away by a virtual topology feature.

## Access

```
import part
mdb.models[name].parts[name].ignoredEdges[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].ignoredEdges[i]
mdb.models[name].rootAssembly.instances[name].ignoredEdges[i]
```

## getSize(...)



This method returns a Float indicating the length of the edge.



### Required arguments

None.

### Optional arguments

- *printResults*

  A Bool specifying whether verbose output is printed. The default is True.

### Return value

A Float.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getRadius()



This method returns the radius of a circular IgnoredEdge object.



### Arguments

None.

### Return value

A Float specifying the radius.

### Exceptions

The given IgnoredEdge object is not circular.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getCurvature(...)



This method returns curvature information at a location on the IgnoredEdge object.



### Required arguments

- *parameter*

  A Float specifying the normalized parameter location on the IgnoredEdge where the curvature is to be computed. This argument is mutually exclusive with the argument *point*.

- *point*

  A tuple of *X*-, *Y*-, and *Z*-coordinates of a point at which the curvature is to be computed. If *point* does not lie on the IgnoredEdge an attempt is made to project it onto the IgnoredEdge and use the projected point.

### Optional arguments

None.

### Return value

A dictionary with keys 'evaluationPoint', 'curvature', 'radius', 'tangent'. Where 'evaluationPoint' specifies the location at which the curvature was computed. 'curvature' specifies the curvature vector at that location. 'radius' is the Radius of curvature and 'tangent' specifies the tangent to the IgnoredEdge at that location.

### Exceptions

The given IgnoredEdge is straight.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The IgnoredEdge object has the following members:

- *index*

  An Int specifying the index of the IgnoredEdge in the [IgnoredEdgeArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all).

- *pointOn*

  A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point located on the edge.