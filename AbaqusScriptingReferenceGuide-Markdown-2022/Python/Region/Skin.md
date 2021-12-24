# Skin object

The Skin object stores information on skin reinforcements created on entities.

## Access

```
import part
mdb.models[name].parts[name].skins[name]
import assembly
mdb.models[name].rootAssembly.allInstances[name].skins[name]
mdb.models[name].rootAssembly.instances[name].skins[name]
mdb.models[name].rootAssembly.skins[name]
```

## Skin(...)



This method creates a skin from a sequence of objects in a model database. At least one of the optional arguments needs to be specified.



### Path

mdb.models[*name*].parts[*name*].Skin

### Required arguments

- *name*

  A String specifying the repository key. The default value is an empty string.

### Optional arguments

- *faces*

  A sequence of Face objects specifying the faces on which skins should be created. Applicable to three and two dimensional parts.

- *edges*

  A sequence of Edge objects specifying the edges on which skins should be created. Applicable to axisymmetric parts.

- *elementFaces*

  A sequence of MeshFace objects specifying the mesh faces on which skins should be created. Applicable to three and two dimensional parts.

- *elementEdges*

  A sequence of MeshEdge objects specifying the mesh edges on which skins should be created. Applicable to axisymmetric parts.

### Return value

A Skin object.

### Exceptions

InvalidNameError.



## EditSkin(...)



This method modifies underlying entities of the selected skin. At least one of the optional arguments needs to be specified.



### Path

mdb.models[*name*].parts[*name*].EditSkin

### Required arguments

- *name*

  A String specifying the repository key. The default value is an empty string.

### Optional arguments

- *faces*

  A sequence of Face objects specifying the faces on which skins should be created. Applicable to three and two dimensional parts.

- *edges*

  A sequence of Edge objects specifying the edges on which skins should be created. Applicable to axisymmetric parts.

- *elementFaces*

  A sequence of MeshFace objects specifying the mesh faces on which skins should be created. Applicable to three and two dimensional parts.

- *elementEdges*

  A sequence of MeshEdge objects specifying the mesh edges on which skins should be created. Applicable to axisymmetric parts.

### Return value

A Skin object.

### Exceptions

InvalidNameError.



## Members

The Skin object has the following members:

- *elements*

  A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object.

- *edges*

  An [EdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object.

- *faces*

  A [FaceArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.