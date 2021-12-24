# OdbDataElementSet object

The OdbDataElementSet object stores element set data.

## Access

```
import visualization
session.odbData[name].elementSets[i]
```

## Members

The OdbDataElementSet object has the following members:

- *name*

  A String specifying the set name. This attribute is read-only.

- *elements*

  A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute is read-only.