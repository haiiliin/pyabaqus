# Cell object

Cells are volumetric regions of geometry.

## Access

```
import part
mdb.models[name].parts[name].allInternalSets[name].cells[i]
mdb.models[name].parts[name].allSets[name].cells[i]
mdb.models[name].parts[name].cells[i]
mdb.models[name].parts[name].sets[name].cells[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].cells[i]
mdb.models[name].rootAssembly.allInstances[name].sets[name].cells[i]
mdb.models[name].rootAssembly.allInternalSets[name].cells[i]
mdb.models[name].rootAssembly.allSets[name].cells[i]
mdb.models[name].rootAssembly.instances[name].cells[i]
mdb.models[name].rootAssembly.instances[name].sets[name].cells[i]
mdb.models[name].rootAssembly.modelInstances[i].sets[name].cells[i]
mdb.models[name].rootAssembly.sets[name].cells[i]
```

## getSize(...)



This method returns a Float indicating the volume of the cell.



### Required arguments

None.

### Optional arguments

- *printResults*

  A Boolean that determines whether a verbose output is to be printed. The default is True.

### Return value

A Float.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getFaces()



This method returns a sequence consisting of the face IDs of the faces which bound the cell.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getEdges()



This method returns a sequence consisting of the edge IDs of the edges on the cell.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getVertices()



This method returns a sequence consisting of the vertex IDs of the vertices on the cell.



### Arguments

None.

### Return value

A tuple of integers.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getAdjacentCells()



This method returns an array of cell objects that share at least one face of the cell.



### Arguments

None.

### Return value

A [CellArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) object which is a sequence of Cell objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getNodes()



This method returns an array of node objects that are associated with the cell.



### Arguments

None.

### Return value

A [MeshNodeArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object which is a sequence of [MeshNode](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getElements()



This method returns an array of element objects that are associated with the cell.



### Arguments

None.

### Return value

A [MeshElementArray](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object which is a sequence of [MeshElement](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## getCADAttributes(...)



This method returns an array of CAD attribute strings associated with the cell when the part was created from CAD data.



### Arguments

None.

### Return value

An array of String.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The Cell object has the following members:

- *index*

  An Int specifying the index of the cell in the CellArray.

- *isReferenceRep*

  A Boolean specifying whether the cell belongs to the reference representation of the Part or Instance.

- *pointOn*

  A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point located on the cell.

- *featureName*

  A tuple of Floats specifying the name of the feature that created this cell.

- *instanceName*

  A tuple of Floats specifying the name of the part instance for this cell (if applicable).