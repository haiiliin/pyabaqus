# ExpInitialization object

The ExpInitialization object is used in conjunction with [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) in Abaqus/Explicit analyses to specify contact initialization data.

The ExpInitialization object is derived from the [ContactInitialization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactinitializationpyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].contactInitializations[name]
```

## ExpInitialization(...)



This method creates an ExpInitialization object.



### Path

```
mdb.models[name].ExpInitialization
```

### Required arguments

- *name*

  A String specifying the contact initialization repository key.

### Optional arguments

- *overclosureType*

  A SymbolicConstant specifying the type of overclosure to be defined. Possible values are ADJUST, INTERFERENCE, and CLEARANCE. The default value is ADJUST.

- *interferenceDistance*

  None or a Float specifying the interference distance. This argument is valid only when *overclosureType*=INTERFERENCE. The default value is None.

- *clearanceDistance*

  None or a Float specifying the initial clearance distance. This argument is valid only when *overclosureType*=CLEARANCE and must be specified in that case. The default value is None.

- *openingTolerance*

  None or a Float specifying the distance tolerance within which initial openings will undergo strain-free adjustments. This argument is not valid when *overclosureType*=INTERFERENCE unless a value has been specified for *interferenceDistance*. The default value is None.

- *overclosureTolerance*

  None or a Float specifying the distance tolerance within which initial overclosures will undergo strain-free adjustments. The default value is None.

- *adjustNodalCoords*

  A Boolean specifying whether to resolve clearances/overclosures by adjusting the nodal coordinates without creating strain in the model. *adjustNodalCoords*=True can be used only for clearances/overclosures defined in the first step of an analysis. The default value is True.

- *secondaryNodesetName*

  A String specifying the name of the node set containing the secondary nodes to be included in the initial clearance specification. This argument is not valid when *overclosureType*=INTERFERENCE and if *openingTolerance* or *overclosureTolerance* is specified. The default value is None.

- *stepFraction*

  A Float specifying the fraction of the step time (between 0.0 and 1.0) in which the interference fit has to be solved. The default value is 1.0. This argument is valid only when *overclosureType*=INTERFERENCE.

### Return value

An ExpInitialization object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the ExpInitialization object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ExpInitialization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expinitializationpyc.htm?ContextScope=all#simaker-expInitializationexpInitializationpyc) method, except for the *name* argument.

### Return value

None.

### Exceptions

RangeError.



## Members

The ExpInitialization object has members with the same names and descriptions as the arguments to the [ExpInitialization](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expinitializationpyc.htm?ContextScope=all#simaker-expInitializationexpInitializationpyc) method.



## Corresponding analysis keywords

- [CONTACT INITIALIZATION DATA](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactinitializationdata.htm?ContextScope=all#simakey-r-contactinitializationdata)