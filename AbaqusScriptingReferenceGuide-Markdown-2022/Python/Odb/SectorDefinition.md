# SectorDefinition object

The SectorDefinition object describes the number of symmetry sectors and axis of symmetry for a cyclic symmetry model.

## Access

```
import odbAccess
session.odbs[name].sectorDefinition
```

## Members

The SectorDefinition object has the following members:

- *numSectors*

  An Int specifying the number of sectors in the cyclic symmetry model.

- *symmetryAxis*

  A tuple of tuples of Floats specifying the coordinates of two points on the axis of symmetry.