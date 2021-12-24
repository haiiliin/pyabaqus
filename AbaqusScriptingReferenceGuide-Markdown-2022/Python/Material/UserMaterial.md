# UserMaterial object

The UserMaterial object defines material constants for use in subroutines [UMAT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-umat.htm?ContextScope=all#simasub-c-umat), [UMATHT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-umatht.htm?ContextScope=all#simasub-c-umatht), or [VUMAT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-vumat.htm?ContextScope=all#simasub-c-vumat).

## Access

```
import material
mdb.models[name].materials[name].userMaterial
import odbMaterial
session.odbs[name].materials[name].userMaterial
```

## UserMaterial(...)



This method creates a UserMaterial object.



### Path

```
mdb.models[name].materials[name].UserMaterial
session.odbs[name].materials[name].UserMaterial
```

### Required arguments

None.

### Optional arguments

- *type*

  A SymbolicConstant specifying the type of material behavior defined by the command. Possible values are MECHANICAL, THERMAL, and THERMOMECHANICAL. The default value is MECHANICAL.

- *unsymm*

  A Boolean specifying if the material stiffness matrix, ∂Δσ/∂Δε, is not symmetric or, when a thermal constitutive model is used, if ∂f/∂(∂θ/∂x) is not symmetric. The default value is OFF. This argument is valid only for an Abaqus/Standard analysis.

- *mechanicalConstants*

  A sequence of Floats specifying the mechanical constants of the material. This argument is valid only when *type*=MECHANICAL or THERMOMECHANICAL. The default value is an empty sequence.

- *thermalConstants*

  A sequence of Floats specifying the thermal constants of the material. This argument is valid only when *type*=THERMAL or THERMOMECHANICAL. The default value is an empty sequence.

- *effmod*

  A Boolean specifying if effective bulk modulus and shear modulus are returned by user subroutine [VUMAT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-vumat.htm?ContextScope=all#simasub-c-vumat). The default value is OFF. This argument is valid only in an Abaqus/Explicit analysis.

- *hybridFormulation*

  A SymbolicConstant to specify the formulation of the hybrid element with user subroutine [UMAT](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAESUBRefMap/simasub-c-umat.htm?ContextScope=all#simasub-c-umat). Possible values are TOTAL, INCREMENTAL, and INCOMPRESSIBLE. The default value is INCREMENTAL. This argument is valid only in an Abaqus/Standard analysis.

### Return value

A UserMaterial object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the UserMaterial object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [UserMaterial](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-usermaterialpyc.htm?ContextScope=all#simaker-usermaterialusermaterialpyc) method.

### Return value

None.

### Exceptions

RangeError.



## Members

The UserMaterial object has members with the same names and descriptions as the arguments to the [UserMaterial](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-usermaterialpyc.htm?ContextScope=all#simaker-usermaterialusermaterialpyc) method.



## Corresponding analysis keywords

- [USER MATERIAL](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-usermaterial.htm?ContextScope=all#simakey-r-usermaterial)