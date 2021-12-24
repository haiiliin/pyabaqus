# ConstrainedSketchVertex object

The ConstrainedSketchVertex object stores the vertex position.

## Access

```
import sketch
mdb.models[name].sketches[name].vertices[i]
mdb.models[name].sketches[name].vertices[i][i]
```

## Spot(...)



This method creates a spot (construction point) located at the specified coordinates.



### Path

```
mdb.models[name].sketches[name].Spot
```

### Required arguments

- *point*

  A pair of Floats specifying the coordinates of the construction point.

### Optional arguments

None.

### Return value

A ConstrainedSketchVertex object (None if the spot cannot be created).

### Exceptions

None.



## Members

The ConstrainedSketchVertex object has the following member:

- *coords*

  A tuple of Floats specifying the*X*-, *Y*-, and *Z*-coordinates of the sketch vertex.