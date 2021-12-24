# RegionPairs object

The RegionPairs object stores the domain pair definition for [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) and [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) objects. The RegionPairs object has no constructor or members.

## Access

```
import interaction
mdb.models[name].interactions[name].excludedPairs
mdb.models[name].interactions[name].includedPairs
```

## setValuesInStep(...)



This method allows addition and removal of domain pairs in a given step.



### Required arguments

- *stepName*

  A String specifying the name of the step in which the region pair assignments are to be modified.

### Optional arguments

- *useAllstar*

  A Boolean specifying whether the contacting surface pair consists of all exterior faces and -- in an Abaqus/Explicit analysis -- analytical rigid surfaces, shell edges, and beam segments in the model.

- *addPairs*

  A sequence of pairs of region objects or SymbolicConstants that specify the surface pairs to add to the included pairs of the [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) or [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) object in the given step. Possible values of the SymbolicConstants are GLOBAL and SELF. When used with a [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) object, the second parameter of each pair can also be a string that references an Eulerian material surface.

- *removePairs*

  A sequence of pairs of region objects or SymbolicConstants that specify the surface pairs to remove from the included pairs of the [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) or [ContactStd](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactstdpyc.htm?ContextScope=all) object in the given step. Possible values of the SymbolicConstants are GLOBAL and SELF. When used with a [ContactExp](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactexppyc.htm?ContextScope=all) object, the second parameter of each pair can also be a string that references an Eulerian material surface.

### Return value

None.

### Exceptions

None.



## Members

The RegionPairs object has no members.



## Corresponding analysis keywords

- [CONTACT INCLUSIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactinclusions.htm?ContextScope=all#simakey-r-contactinclusions)
- [CONTACT EXCLUSIONS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-contactexclusions.htm?ContextScope=all#simakey-r-contactexclusions)