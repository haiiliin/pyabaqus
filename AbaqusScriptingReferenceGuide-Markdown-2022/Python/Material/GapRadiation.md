# GapRadiation object

The GapRadiation object specifies radiative heat transfer between closely adjacent surfaces.

## Access

```
import material
mdb.models[name].materials[name].gapRadiation
import odbMaterial
session.odbs[name].materials[name].gapRadiation
```

## GapRadiation(...)



This method creates a GapRadiation object.



### Path

```
mdb.models[name].materials[name].Gapradiation
session.odbs[name].materials[name].Gapradiation
```

### Required arguments

- *mainSurfaceEmissivity*

  A Float specifying the Emissivity of main surface.ϵA

- *secondarySurfaceEmissivity*

  A Float specifying the Emissivity of the secondary surfaceϵB.

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Table data

- Effective view factor.
- Gap clearance.
- Repeat this data line as often as necessary to define the dependence of the view factor on gap clearance.

### Return value

A Gapradiation object.

### Exceptions

None.



## setValues(...)



This method modifies the GapRadiation object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GapRadiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapradiationpyc.htm?ContextScope=all#simaker-gapradiationgapradiationpyc) method.

### Return value

None.

### Exceptions

None.



## Members

The Gap Radiation object has members with the same names and descriptions as the arguments to the [GapRadiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapradiationpyc.htm?ContextScope=all#simaker-gapradiationgapradiationpyc) method.



## Corresponding analysis keywords

- [GAP RADIATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gapradiation.htm?ContextScope=all#simakey-r-gapradiation)