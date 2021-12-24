# XFEMCrackGrowth object

The XFEMCrackGrowth object defines the enrichment activation state for an [XFEMCrack](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackpyc.htm?ContextScope=all).

The XFEMCrackGrowth object is derived from the [Interaction](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactions[name]
```

## XFEMCrackGrowth(...)



This method creates an XFEMCrackGrowth object.



### Path

```
mdb.models[name].XFEMCrackGrowth
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A String specifying the name of the step in which the XFEMCrackGrowth object is created.

- *crackName*

  A String specifying the [XFEMCrack](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackpyc.htm?ContextScope=all) object associated with this interaction.

### Optional arguments

- *allowGrowth*

  A Boolean specifying whether the crack is allowed to grow (propagate) during this analysis step. The default value is ON.

### Return value

A XFEMCrackGrowth object.

### Exceptions

None.



## setValues(...)



This method modifies the data for an existing XFEMCrackGrowth object in the step where it is created.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [XFEMCrackGrowth ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackgrowthpyc.htm?ContextScope=all#simaker-xfemcrackgrowthxfemcrackgrowthpyc)method, except for the *name* and *createStepName* arguments.

### Return value

None.

### Exceptions

None.



## setValuesInStep(...)



This method modifies the propagating data for an existing XFEMCrackGrowth object in the specified step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the interaction is modified.

### Optional arguments

- *allowGrowth*

  A Boolean specifying whether the crack is allowed to grow (propagate) during this analysis step. The default value is ON.

### Return value

None.

### Exceptions

None.



## Members

The XFEMCrackGrowth object has members with the same names and descriptions as the arguments to the [XFEMCrackGrowth ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackgrowthpyc.htm?ContextScope=all#simaker-xfemcrackgrowthxfemcrackgrowthpyc)method.



## Corresponding analysis keywords

- [ENRICHMENT ACTIVATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-enrichmentactivation.htm?ContextScope=all#simakey-r-enrichmentactivation)