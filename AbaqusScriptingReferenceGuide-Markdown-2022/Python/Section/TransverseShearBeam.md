# TransverseShearBeam object

The TransverseShearBeam object defines the transverse shear stiffness properties of a beam section.

## Access

```
import section
mdb.models[name].sections[name].beamTransverseShear
import odbSection
session.odbs[name].sections[name].beamTransverseShear
```

## TransverseShearBeam(...)



This method creates a TransverseShearBeam object.



### Path

```
mdb.models[name].sections[name].TransverseShearBeam
session.odbs[name].sections[name].TransverseShearBeam
```

### Required arguments

- *scfDefinition*

  A SymbolicConstant specifying how slenderness compensation factor of the section is given. Possible values are ANALYSIS_DEFAULT, COMPUTED, and VALUE.

### Optional arguments

- *k23*

  None or a Float specifying the k23 shear stiffness of the section. The default value is None.

- *k13*

  None or a Float specifying the k13 shear stiffness of the section. The default value is None.

- *slendernessCompensation*

  The SymbolicConstant COMPUTED or a Float specifying the slenderness compensation factor of the section. The default value is 0.25.

### Return value

A TransverseShearBeam object.

### Exceptions

None.



## setValues(...)



This method modifies the TransverseShearBeam object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [TransverseShearBeam ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-transverseshearbeampyc.htm?ContextScope=all#simaker-transverseshearbeamtransverseshearbeampyc)method.

### Return value

None.

### Exceptions

None.



## Members

The TransverseShearBeam object has members with the same names and descriptions as the arguments to the [TransverseShearBeam ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-transverseshearbeampyc.htm?ContextScope=all#simaker-transverseshearbeamtransverseshearbeampyc)method.



## Corresponding analysis keywords

- [TRANSVERSE SHEAR STIFFNESS](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-transverseshearstiffness.htm?ContextScope=all#simakey-r-transverseshearstiffness)