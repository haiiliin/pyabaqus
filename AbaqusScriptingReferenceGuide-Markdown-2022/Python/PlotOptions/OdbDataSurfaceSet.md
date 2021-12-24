# OdbDataSurfaceSet object

The OdbDataSurfaceSet object stores surface set data.

## Access

```
import visualization
session.odbData[name].surfaceSets[i]
```

## Members

The OdbDataSurfaceSet object has the following members:

- *name*

  A String specifying the set name. This attribute is read-only.

- *elements*

  A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute is read-only.

- *facets*

  A String-to-tuple-of-Ints Dictionary specifying the facets corresponding to the *elements*. This attribute is read-only.