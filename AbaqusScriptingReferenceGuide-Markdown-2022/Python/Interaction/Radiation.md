# Radiation object

The Radiation object specifies radiation for a contact interaction property.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].radiation
```

## Radiation(...)



This method creates a Radiation object.



### Path

```
mdb.models[name].interactionProperties[name].Radiation
```

### Required arguments

- *mainEmissivity*

  A Float specifying the emissivity of the main surface.

- *secondaryEmissivity*

  A Float specifying the emissivity of the secondary surface.

- *table*

  A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap clearance, dd.

### Optional arguments

None.

### Return value

A Radiation object.

### Exceptions

None.



## setValues(...)



This method modifies the Radiation object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Radiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationpyc.htm?ContextScope=all#simaker-radiationradiationpyc) method.

### Return value

None.

### Exceptions

None.



## Members

The Radiation object has members with the same names and descriptions as the arguments to the [Radiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationpyc.htm?ContextScope=all#simaker-radiationradiationpyc) method.



## Corresponding analysis keywords

- [GAP RADIATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gapradiation.htm?ContextScope=all#simakey-r-gapradiation)