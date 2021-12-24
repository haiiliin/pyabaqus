# Sorption object

The Sorption object defines absorption and exsorption behaviors of a partially saturated porous medium in the analysis of coupled wetting liquid flow and porous medium stress.

## Access

```
import material
mdb.models[name].materials[name].sorption
import odbMaterial
session.odbs[name].materials[name].sorption
```

## Sorption(...)



This method creates a Sorption object.



### Path

```
mdb.models[name].materials[name].Sorption
session.odbs[name].materials[name].Sorption
```

### Required arguments

- *absorptionTable*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *lawAbsorption*

  A SymbolicConstant specifying absorption behavior. Possible values are LOG and TABULAR. The default value is TABULAR.

- *exsorption*

  A Boolean specifying whether the exsorption data is specified. The default value is OFF.

- *lawExsorption*

  A SymbolicConstant specifying exsorption behavior. Possible values are LOG and TABULAR. The default value is TABULAR.

- *scanning*

  A Float specifying the slope of the scanning line, (duw/ds)|s. This slope must be positive and larger than the slope of the absorption or exsorption behaviors. The default value is 0.0.

- *exsorptionTable*

  A sequence of sequences of Floats specifying the items described below. The default value is an empty sequence.

### Table data

If *lawAbsorption*=TABULAR or *lawExsorption*=TABULAR, the *absorptionTable* and *exsorptionTable* data respectively specify the following:

- Pore pressure, uw.
- Saturation, s.

If *lawAbsorption*=LOG or *lawExsorption*=LOG, the *absorptionTable* and *exsorptionTable* data respectively specify the following:

- A.
- B.
- s0.
- s1.

### Return value

A Sorption object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Sorption object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Sorption ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sorptionpyc.htm?ContextScope=all#simaker-sorptionsorptionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Sorption object has members with the same names and descriptions as the arguments to the [Sorption ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sorptionpyc.htm?ContextScope=all#simaker-sorptionsorptionpyc)method.



## Corresponding analysis keywords

- [SORPTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-sorption.htm?ContextScope=all#simakey-r-sorption)