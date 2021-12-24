# MeshStats object

The MeshStats object is a query object for holding mesh statistics and is returned by the getMeshStats command. The object does not have any methods.

## Access

```
import mesh
```

## Members

The MeshStats object has the following members:

- *numPointElems*

  An Int specifying the number of point elements.

- *numLineElems*

  An Int specifying the number of line elements.

- *numQuadElems*

  An Int specifying the number of quadrilateral elements.

- *numTriElems*

  An Int specifying the number of triangular elements.

- *numHexElems*

  An Int specifying the number of hexahedral elements.

- *numWedgeElems*

  An Int specifying the number of wedge elements.

- *numTetElems*

  An Int specifying the number of tetrahedral elements.

- *numPyramidElems*

  An Int specifying the number of pyramid elements.

- *numNodes*

  An Int specifying the number of nodes.

- *numMeshedRegions*

  An Int specifying the number of regions that contain a mesh.