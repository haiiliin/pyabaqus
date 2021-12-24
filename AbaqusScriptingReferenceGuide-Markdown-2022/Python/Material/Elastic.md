# Elastic object

The Elastic object specifies elastic material properties.

## Access

```
import material
mdb.models[name].materials[name].elastic
import odbMaterial
session.odbs[name].materials[name].elastic
```

## Elastic(...)



This method creates an Elastic object.



### Path

```
mdb.models[name].materials[name].Elastic
session.odbs[name].materials[name].Elastic
```

### Required arguments

- *table*

  A sequence of sequences of Floats specifying the items described below.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of elasticity data provided. Possible values are:

  - ISOTROPIC
  - ORTHOTROPIC
  - ANISOTROPIC
  - ENGINEERING_CONSTANTS
  - LAMINA
  - TRACTION
  - COUPLED_TRACTION
  - SHORT_FIBER
  - SHEAR
  - BILAMINA

  The default value is ISOTROPIC.

- *noCompression*

  A Boolean specifying whether compressive stress is allowed. The default value is OFF.

- *noTension*

  A Boolean specifying whether tensile stress is allowed. The default value is OFF.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *moduli*

  A SymbolicConstant specifying the time-dependence of the elastic material constants. Possible values are INSTANTANEOUS and LONG_TERM. The default value is LONG_TERM.

### Table data

If *type*=ISOTROPIC, the table data specify the following:

- The Young's modulus, E.
- The Poisson's ratio, ν.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=SHEAR, the table data specify the following:

- The shear modulus,G.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ENGINEERING_CONSTANTS, the table data specify the following:

- E1.
- E2.
- E3.
- ν12.
- ν13.
- ν23.
- G12.
- G13.
- G23.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=LAMINA, the table data specify the following:

- E1.
- E2.
- ν12.
- G12.
- G13. This shear modulus is needed to define transverse shear behavior in shells.
- G23. This shear modulus is needed to define transverse shear behavior in shells.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ORTHOTROPIC, the table data specify the following:

- D1111.
- D1122.
- D2222.
- D1133.
- D2233.
- D3333.
- D1212.
- D1313.
- D2323.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=ANISOTROPIC, the table data specify the following:

- D1111.
- D1122.
- D2222.
- D1133.
- D2233.
- D3333.
- D1112.
- D2212.
- D3312.
- D1212.
- D1113.
- D2213.
- D3313.
- D1213.
- D1313.
- D1123.
- D2223.
- D3323.
- D1223.
- D1323.
- D2323.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=TRACTION, the table data specify the following:

- EE for warping elements; En⁢n for cohesive elements.
- G1 for warping elements; Es⁢s for cohesive elements.
- G2 for warping elements; Et⁢t for cohesive elements.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=BILAMINA, the table data specify the following:

- E1+.
- E2+.
- ν12+.
- G12.
- E1−.
- E2−.
- ν112−.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *type*=SHORT_FIBER, there is no table data.

### Return value

An Elastic object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the Elastic object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [Elastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticpyc.htm?ContextScope=all#simaker-elasticelasticpyc) method.

### Return value

None.

### Exceptions

RangeError.



## Members

The Elastic object has members with the same names and descriptions as the arguments to the [Elastic](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elasticpyc.htm?ContextScope=all#simaker-elasticelasticpyc) method.

In addition, the Elastic object can have the following members:

- *failStress*

  A [FailStress](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failstresspyc.htm?ContextScope=all) object.

- *failStrain*

  A [FailStrain](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-failstrainpyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [ELASTIC](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-elastic.htm?ContextScope=all#simakey-r-elastic)