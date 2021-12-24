# ConstrainedSketchVertexArray object

The ConstrainedSketchVertexArray is a sequence of [ConstrainedSketchVertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) objects.

## Access

```
import sketch
mdb.models[name].sketches[name].vertices[i]
```

## findAt(...)



This method returns the [ConstrainedSketchVertex](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) located at the given coordinates.



### Required arguments

- *coordinates*

  A sequence of Floats specifying the *X*- and *Y*-coordinates of the object to find.

### Optional arguments

- *printWarning*

  A Boolean specifying whether a message is to be printed to the CLI if no entity is found at the specified location. The default value is True.

### Return value

A [ConstrainedSketchVertex](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?ContextScope=all) object.

### Exceptions

None.



## Members

The ConstrainedSketchVertexArray object has no members.