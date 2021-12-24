# IgnoredVertex object

An IgnoredVertex object is a point region of the geometry that was abstracted away by a virtual topology feature.

## Access

```
import part
mdb.models[name].parts[name].ignoredVertices[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].ignoredVertices[i]
mdb.models[name].rootAssembly.instances[name].ignoredVertices[i]
```

## Members

The IgnoredVertex object has the following members:

- *index*

  An Int specifying the index of the IgnoredVertex in the IgnoredVertexArray.

- *pointOn*

  A tuple of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the vertex.