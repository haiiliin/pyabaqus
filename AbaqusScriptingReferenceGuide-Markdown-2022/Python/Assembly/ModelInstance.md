# ModelInstance object

A ModelInstance object is an instance of a Model.

## Access

```
import assembly
mdb.models[name].rootAssembly.modelInstances[i]
```

## Instance(...)



This method creates a ModelInstance object and puts it into the instances repository.



### Path

```
mdb.models[name].rootAssembly.Instance
```

### Required arguments

- *name*

  The repository key. The name must be a valid Abaqus object name.

- *model*

  A [Model](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?ContextScope=all) object to be instanced. If the model does not exist, no ModelInstance object is created.

### Optional arguments

- *autoOffset*

  A Boolean specifying whether to apply an auto offset to the new instance that will offset it from existing instances. The default value is OFF.

### Return value

A ModelInstance object.

### Exceptions

None.



## ConvertConstraints()



This method converts the position constraints of an instance to absolute positions. The method deletes the constraint features on the instance but preserves the position in space.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## getPosition()



This method prints the sum of the translations and rotations applied to the ModelInstance object.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## replace(...)



This method replaces one instance with an instance of another model.



### Required arguments

- *instanceOf*

  A [Model](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?ContextScope=all) object to be instanced. If the model does not exist, no ModelInstance object is created.

### Optional arguments

- *applyConstraints*

  A Boolean specifying whether to apply existing constraints on the new instance or to position the new instance in the same place as the original instance. The default value is True. A value of False indicates that constraints applies to the instance are deleted will be deleted from the feature list.

### Return value

None.

### Exceptions

None.



## translate(...)



This method translates an instance by the specified amount.



### Required arguments

- *vector*

  A sequence of three Floats specifying a translation vector.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The ModelInstance object can have the following members:

- *sets*

  A repository of [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) objects specifying the sets created on the assembly. For more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *surfaces*

  A repository of [Surface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacepyc.htm?ContextScope=all) objects specifying the surfaces created on the assembly. For more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *vertices*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object.

- *edges*

  An [EdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object.

- *elements*

  A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object.

- *nodes*

  A [MeshNodeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object.

- *datums*

  A repository of [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) objects.

- *referencePoints*

  A repository of [ReferencePoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-referencepointpyc.htm?ContextScope=all) objects.