# Model object

The following commands operate on Model objects. For more information about the Model object, see [Model object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?ContextScope=all).

## Access

```
import assembly
```

## Instance(...)



This method copies a [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object from the specified model and creates a new [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object.



### Path

mdb.models[*name*].Instance

### Required arguments

- *name*

  A String specifying the repository key.

- *objectToCopy*

  A [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object to be copied.

### Optional arguments

None.

### Return value

A Model object.

### Exceptions

None.



## convertAllSketches(...)



This method converts all sketches from Abaqus 6.5 or earlier to the equivalent [ConstrainedSketch](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) objects.



### Required arguments

None.

### Optional arguments

- *regenerate*

  A Boolean specifying if all the features in assembly as well as in all the parts in the model should be regenerated after the conversion. The default value is True.

- *convertReversedSketches*

  A Boolean specifying whether sketches in analytic rigid parts should be converted even if they cause the orientation of surfaces defined on them to be flipped. The default value is True.

### Return value

A list of strings describing any warnings or errors encountered during the conversion process.

### Exceptions

None.



## linkInstances(...)



This method links the selected [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects to the corresponding [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects from the specified models. If all instances of a Part are selected for linking, the Part will be linked as well. If not, a new linked child Part object will be created and added to the repository.



### Required arguments

- *instancesMap*

  A tuple of tuples containing the instance name to be linked and the corresponding [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object to which it will be linked.

### Optional arguments

None.

### Return value

A list of strings describing any warnings or errors encountered during the conversion process.

### Exceptions

None.