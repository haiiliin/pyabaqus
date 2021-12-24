# ConstrainedSketchGeometryArray object

The ConstrainedSketchGeometryArray is a sequence of [ConstrainedSketchGeometry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) objects.

## Access

```
import sketch
mdb.models[name].sketches[name].geometry[i]
```

## findAt(...)



This method returns the [ConstrainedSketchGeometry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object located at the given coordinates.



### Required arguments

- *coordinates*

  A sequence of Floats specifying the *X*- and *Y*-coordinates of the object to find.

### Optional arguments

- *printWarning*

  A Boolean specifying whether a message is to be printed to the CLI if no entity is found at the specified location. The default value is True.

### Return value

A [ConstrainedSketchGeometry](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?ContextScope=all) object.

### Exceptions

None.



## Members

The ConstrainedSketchGeometryArray object has no members.