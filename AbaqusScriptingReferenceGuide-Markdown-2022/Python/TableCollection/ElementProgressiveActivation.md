# ElementProgressiveActivation object

The ElementProgressiveActivation object is used to specify elements that can be activated during an analysis.

## Access

```
mdb.models[name].rootAssembly.elementProgressiveActivations[name]
```

## ElementProgressiveActivation(...)

This method creates an ElementProgressiveActivation object and places it in the elementProgressiveActivation repository.

### Path

```
mdb.models[name].rootAssembly.ElementProgressiveActivation
```

### Required arguments

- *name*

  A String specifying the key of the repository.

### Optional arguments

- *elset*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all#simaker-c-regionpyc) object specifying the region containing the elements that will be activated during the analysis.

- *deformation*

  A Boolean value specifying whether the elements that have not yet been activated will follow the deformations of the active elements. Set *deformation*=ON when the deformation of the active elements is excessive. The default value is OFF.

- *freeSurfaceType*

  A SymbolicConstant specifying the exposed areas of the element facets that are active for convection or radiation boundary conditions to be applied. Possible values are NONE and FACET. If *freeSurfaceType*=FACET, user subroutine [UEPACTIVATIONFACET](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-uepactivationfacet.htm?ContextScope=all#simasub-c-uepactivationfacet) will be called at the start of the increment for each element. If *freeSurfaceType*=NONE, all the exposed areas of the element facets are considered. The default value is NONE.

### Return value

An ElementProgressiveActivation object.

### Exceptions

AbaqusException: If the region does not contain only elements.



## setValues

The method modifies the ElementProgressiveActivation object.



## Members

The ElementProgressiveActivation object has members with the same names and descriptions as the arguments to the [ElementProgressiveActivation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elemProgActivationpyc.htm?ContextScope=all#simaker-c-elemProgActivationpyc) method.



## Corresponding analysis keywords

- [*ELEMENT PROGRESSIVE ACTIVATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-elementprogressiveactivation.htm?ContextScope=all#simakey-r-elementprogressiveactivation)