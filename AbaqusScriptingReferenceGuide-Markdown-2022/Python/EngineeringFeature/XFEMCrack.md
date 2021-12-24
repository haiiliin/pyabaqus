# XFEMCrack object

The XFEMCrack object defines the parameters needed to model crack initiation or crack growth using XFEM technology. Currently only assembly regions are supported.

The XFEMCrack object is derived from the [Crack](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-crackpyc.htm?ContextScope=all) object.

## Access

```
import part
mdb.models[name].parts[name].engineeringFeatures.cracks[name]
import assembly
mdb.models[name].rootAssembly.engineeringFeatures.cracks[name]
```

## XFEMCrack(...)



This method creates a XFEMCrack object. Although the constructor is available both for parts and for the assembly, XFEMCrack objects are currently supported only under the assembly.



### Path

```
mdb.models[name].parts[name].engineeringFeatures.XFEMCrack
mdb.models[name].rootAssembly.engineeringFeatures.XFEMCrack
```

### Required arguments

- *name*

  A String specifying the repository key.

- *crackDomain*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the region that contains the crack or is likely to contain the crack.

### Optional arguments

- *allowCrackGrowth*

  A Boolean specifying whether the crack is allowed to propagate (grow). The default value is ON.

- *crackLocation*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object specifying the initial crack location. This parameter is required when *allowCrackGrowth*=OFF.

- *singularityCalcRadius*

  None or a Float specifying the radius from the crack tips within which the elements are used for crack singularity calculations. This argument applies only when *allowCrackGrowth*=OFF. The default value is None.

- *interactionProperty*

  A String specifying the name of the [ContactProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpropertypyc.htm?ContextScope=all) object that defines the contact properties for the crack surfaces. The default value is an empty string.

- *elemId*

  A sequence of Ints specifying the labels of the elements that are intersected by the initial crack location. This argument is used only by the input file reader.

- *nodeId*

  A sequence of Ints specifying the position of a node in the corresponding element connectivity. This argument is used only by the input file reader.

- *hasCrackFront*

  A sequence of Ints specifying the values indicating the inclusion/exclusion of the *crackFrontDist* values. A zero value indicates that *crackFrontDist* is not specified for the ith pair *elemId* and *nodeId*. This argument is used only by the input file reader.

- *crackPlaneDist*

  A sequence of Floats specifying the values of the first signed distance function. This argument is used by the input file reader.

- *crackFrontDist*

  A sequence of Floats specifying the values of the second signed distance function. This argument is used only by the input file reader.

- *autoDetectValue*

  An integer specifying the number of element layers around the crack location, to which the crack domain is shrunk.

### Return value

A XFEMCrack object.

### Exceptions

None.



## setValues(...)



This method modifies the XFEMCrack object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [XFEMCrack ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackpyc.htm?ContextScope=all#simaker-xfemcrackxfemcrackpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The XFEMCrack object has members with the same names and descriptions as the arguments to the [XFEMCrack ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xfemcrackpyc.htm?ContextScope=all#simaker-xfemcrackxfemcrackpyc)method.

In addition, the XFEMCrack object has the following member:

- *suppressed*

  A Boolean specifying whether the crack is suppressed or not. The default value is OFF.



## Corresponding analysis keywords

- [ENRICHMENT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-enrichment.htm?ContextScope=all#simakey-r-enrichment)

- [INITIAL CONDITIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-initialconditions.htm?ContextScope=all#simakey-r-initialconditions), TYPE=ENRICHMENT