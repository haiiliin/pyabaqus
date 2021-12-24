# SubmodelSB object

The SubmodelSB object stores the data for a submodel surface based load.

The SubmodelSB object is derived from the [Load](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?ContextScope=all) object.

## Access

```
import load
mdb.models[name].loads[name]
```

## SubmodelSB(...)



This method creates a SubmodelSB object.



### Path

```
mdb.models[name].SubmodelSB
```

### Required arguments

- *name*

  A String specifying the load repository key.

- *createStepName*

  A String specifying the name of the step in which the load is created.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.

- *globalStep*

  A String specifying the step in the global model from which Abaqus reads the values of the variables that will drive the submodel analysis. The String indicates the position of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates the first step.

### Optional arguments

- *globalDrivingRegion*

  A String specifying the element set in the global model that will be searched for elements whose responses will be used to drive the submodel. An empty string indicates that the entire global model will be searched. The default value is an empty string.

- *absoluteExteriorTolerance*

  None or a Float specifying the absolute value by which a driven node of the submodel can lie outside the region of the elements of the global model. The default value is None.

- *exteriorTolerance*

  None or a Float specifying the fraction of the average element size in the global model by which a driven node of the submodel can lie outside the region of the elements of the global model. The default value is 0.05.

- *globalIncrement*

  An Int specifying the increment number in the global model step from which the solution will be used to specify the values of the driven variables. If *globalIncrement*=0, the solution from the last increment will be used. The *globalIncrement* argument is applicable only for linear perturbation steps. The default value is 0.

### Return value

A SubmodelSB object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing SubmodelSB object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [SubmodelSB ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelsbpyc.htm?ContextScope=all#simaker-submodelsbsubmodelsbpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing SubmodelSB object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the load is modified.

### Optional arguments

- *fixed*

  A Boolean specifying whether the load should remain fixed at the current values at the start of the step. The default value is ON.

- *globalStep*

  A String specifying the step in the global model from which Abaqus reads the values of the variables that will drive the submodel analysis. The String indicates the position of the step in the sequence of analysis steps. For example, *globalStep*='1' indicates the first step. The *globalStep* argument is applicable only if *fixed*=OFF.

- *globalIncrement*

  An Int specifying the increment number in the global model step at which the solution will be used to specify the values of the driven variables. If *globalIncrement*=0, the solution from the last increment will be used. The *globalIncrement* argument is applicable only for linear perturbation steps and if *fixed*=OFF. The default value is 0.

### Return value

None.

### Exceptions

None.



## Members

The SubmodelSB object can have the following members:

- *name*

  A String specifying the load repository key.

- *absoluteExteriorTolerance*

  None or a Float specifying the absolute value by which a driven node of the submodel can lie outside the region of the elements of the global model. The default value is None.

- *exteriorTolerance*

  None or a Float specifying the fraction of the average element size in the global model by which a driven node of the submodel can lie outside the region of the elements of the global model. The default value is 0.05.

- *globalDrivingRegion*

  A String specifying the element set in the global model that will be searched for elements whose responses will be used to drive the submodel. An empty string indicates that the entire global model will be searched. The default value is an empty string.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region to which the load is applied.