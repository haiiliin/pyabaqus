# BCDisplayOptions object

The BCDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when

```
session.viewports[name].assemblyDisplay.bcs=ON
```

The BCDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.

## Access

```
session.viewports[name].assemblyDisplay.bcOptions
session.viewports[name].layers[name].assemblyDisplay.bcOptions
```

## setValues(...)



This method modifies the BCDisplayOptions object.



### Required arguments

None.

### Optional arguments

- *displacement*

  A Boolean specifying whether displacement symbols are shown. The default value is ON.

- *velocity*

  A Boolean specifying whether velocity symbols are shown. The default value is ON.

- *acceleration*

  A Boolean specifying whether acceleration symbols are shown. The default value is ON.

- *symmetry*

  A Boolean specifying whether symmetry symbols are shown. The default value is ON.

- *antiSymmetry*

  A Boolean specifying whether anti- symmetry symbols are shown. The default value is ON.

- *temperature*

  A Boolean specifying whether temperature symbols are shown. The default value is ON.

- *porePressure*

  A Boolean specifying whether pore pressure symbols are shown. The default value is ON.

- *fluidCavityPressure*

  A Boolean specifying whether fluid cavity pressure symbols are shown. The default value is ON.

- *acousticPressure*

  A Boolean specifying whether acoustic pressure symbols are shown. The default value is ON.

- *electricPotential*

  A Boolean specifying whether electric potential symbols are shown. The default value is ON.

- *concentration*

  A Boolean specifying whether concentration mass diffusion symbols are shown. The default value is ON.

- *encastre*

  A Boolean specifying whether encastre symbols are shown. The default value is ON.

- *pinned*

  A Boolean specifying whether pinned symbols are shown. The default value is ON.

### Return value

None.

### Exceptions

None.



## Members

The BCDisplayOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bcdisplayoptionspyc.htm?ContextScope=all#simaker-bcdisplayoptionssetvaluespyc)method.