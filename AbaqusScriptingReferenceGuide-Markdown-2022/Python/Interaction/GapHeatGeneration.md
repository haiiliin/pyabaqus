# GapHeatGeneration object

The GapHeatGeneration object specifies heat generation for a contact interaction property.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].heatGeneration
```

## HeatGeneration(...)



This method creates a GapHeatGeneration object.



### Path

```
mdb.models[name].interactionProperties[name].HeatGeneration
```

### Required arguments

None.

### Optional arguments

- *conversionFraction*

  A Float specifying the fraction of dissipated energy caused by friction or electric currents that is converted to heat. The default value is 1.0.

- *secondaryFraction*

  A Float specifying the fraction of converted heat distributed to the secondary surface. The default value is 0.5.

### Return value

A GapHeatGeneration object.

### Exceptions

None.



## setValues(...)



This method modifies the GapHeatGeneration object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GapHeatGeneration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapheatgenerationpyc.htm?ContextScope=all#simaker-gapheatgenerationheatgenerationpyc) method.

### Return value

None.

### Exceptions

None.



## Members

The GapHeatGeneration object has the following members:

- *conversionFraction*

  A Float specifying the fraction of dissipated energy caused by friction or electric currents that is converted to heat. The default value is 1.0.

- *secondaryFraction*

  A Float specifying the fraction of converted heat distributed to the secondary surface. The default value is 0.5.



## Corresponding analysis keywords

- [GAP HEAT GENERATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gapheatgeneration.htm?ContextScope=all#simakey-r-gapheatgeneration)