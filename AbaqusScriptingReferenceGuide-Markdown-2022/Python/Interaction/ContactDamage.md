# ContactDamage object

The ContactDamage object specifies damage options for a contact interaction property.

## Access

```
import interaction
mdb.models[name].interactionProperties[name].damage
```

## Damage(...)



This method creates a ContactDamage object.



### Path

```
mdb.models[name].interactionProperties[name].Damage
```

### Required arguments

- *initTable*

  A sequence of sequences of Floats specifying the values defining the damage initiation. The items in the table data are described below.

### Optional arguments

- *criterion*

  A SymbolicConstant specifying the type of data used to define the initiation of damage. Possible values are MAX_STRESS, MAX_SEPARATION, QUAD_TRACTION, and QUAD_SEPARATION. The default value is MAX_STRESS.

- *initTempDep*

  A Boolean specifying whether the initiation data depend on temperature. The default value is OFF.

- *initDependencies*

  An Int specifying the number of initiation data field variables. The default value is 0.

- *useEvolution*

  A Boolean specifying whether evolution data will be defined. The default value is OFF.

- *evolutionType*

  A SymbolicConstant specifying the type of data used to define the evolution of damage. This argument is valid only when *useEvolution*=ON. Possible values are DISPLACEMENT and ENERGY. The default value is DISPLACEMENT.

- *softening*

  A SymbolicConstant specifying the type of data used to define the evolution softening response. This argument is valid only when *useEvolution*=ON. The TABULAR value can be used only when *evolutionType*=DISPLACEMENT. Possible values are LINEAR, EXPONENTIAL, and TABULAR. The default value is LINEAR.

- *useMixedMode*

  A Boolean specifying whether evolution data be defined using dependent behavior modes. This argument is valid only when *useEvolution*=ON. The default value is OFF.

- *mixedModeType*

  A SymbolicConstant specifying the mode mix fracture criterion. This argument is valid only when *useEvolution*=ON and when *useMixedMode*=ON. The POWER_LAW and BK values can be used only when *evolutionType*=ENERGY. Possible values are TABULAR, POWER_LAW, and BK. The default value is TABULAR.

- *modeMixRatio*

  A SymbolicConstant specifying the mode mix ratio type. This argument is valid only when *useEvolution*=ON and when *useMixedMode*=ON. The TRACTION value can be used only when *mixedModeType*=TABULAR. Possible values are ENERGY and TRACTION. The default value is ENERGY.

- *exponent*

  None or a Float specifying the exponent in the power-law or BK criterion that defines the variation of fracture energy with mode mix. This argument is valid only when *useEvolution*=ON and when *mixedModeType*=POWER_LAW or BK. The default value is None.

- *evolTempDep*

  A Boolean specifying whether the evolution data depend on temperature. This argument is valid only when *useEvolution*=ON. The default value is OFF.

- *evolDependencies*

  An Int specifying the number of evolution data field variables. This argument is valid only when *useEvolution*=ON. The default value is 0.

- *evolTable*

  A sequence of sequences of Floats specifying the values defining the damage evolution. The items in the table data are described below. This argument is valid only when *useEvolution*=ON.

- *useStabilization*

  A Boolean specifying whether stabilization data will be defined. This argument is valid only when *useEvolution*=ON. The default value is OFF.

- *viscosityCoef*

  None or a Float specifying the viscosity coefficient. This argument is valid only when *useStabilization*=ON. The default value is None.

### Table data

Table data for *initTable*:

If *criterion*=MAX_STRESS or QUAD_TRACTION, the table data specify the following:

- Maximum nominal stress in the normal-only mode.
- Maximum nominal stress in the first shear direction (for a mode that involves separation only in this direction).
- Maximum nominal stress in the second shear direction (for a mode that involves separation only in this direction).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *criterion*=MAX_SEPARATION or QUAD_SEPARATION, the table data specify the following:

- Separation at damage initiation in a normal-only mode.
- Separation at damage initiation in a shear-only mode that involves separation only along the first shear direction.
- Separation at damage initiation in a shear-only mode that involves separation only along the second shear direction.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

Table data for *evolTable*:

If *evolutionType*=DISPLACEMENT, *softening*=LINEAR, and *useMixedMode*=OFF, the table data specify the following:

- Effective total or plastic displacement at failure, measured from the time of damage initiation.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *evolutionType*=ENERGY, *softening*=LINEAR or EXPONENTIAL, and *useMixedMode*=OFF, the table data specify the following:

- Fracture energy.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *evolutionType*=DISPLACEMENT, *softening*=LINEAR, *useMixedMode*=ON, *mixedModeType*=TABULAR, and *modeMixRatio*=ENERGY or TRACTION, the table data specify the following:

- Total displacement at failure, measured from the time of damage initiation.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *evolutionType*=ENERGY, *softening*=LINEAR or EXPONENTIAL, *useMixedMode*=ON, *mixedModeType*=TABULAR, and *modeMixRatio*=ENERGY or TRACTION, the table data specify the following:

- Fracture energy.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *evolutionType*=DISPLACEMENT, *softening*=EXPONENTIAL, and *useMixedMode*=OFF, the table data specify the following:

- Effective total or plastic displacement at failure, measured from the time of damage initiation.
- Exponential law parameter.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *evolutionType*=DISPLACEMENT, *softening*=EXPONENTIAL, *useMixedMode*=ON, *mixedModeType*=TABULAR, and *modeMixRatio*=ENERGY or TRACTION, the table data specify the following:

- Total displacement at failure, measured from the time of damage initiation.
- Exponential law parameter.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *evolutionType*=DISPLACEMENT, *softening*=TABULAR, and *useMixedMode*=OFF, the table data specify the following:

- Damage variable.
- Effective total or plastic displacement at failure, measured from the time of damage initiation.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *evolutionType*=DISPLACEMENT, *softening*=TABULAR, *useMixedMode*=ON, *mixedModeType*=TABULAR, and *modeMixRatio*=ENERGY or TRACTION, the table data specify the following:

- Damage variable.
- Effective total displacement, measured from the time of damage initiation.
- Appropriate mode mix ratio.
- Appropriate mode mix ratio (if relevant, for three dimensional problems with anisotropic shear behavior).
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

If *evolutionType*=ENERGY, *softening*=LINEAR or EXPONENTIAL, *useMixedMode*=ON, *mixedModeType*=POWER_LAW or BK, and *modeMixRatio*=ENERGY, the table data specify the following:

- Normal mode fracture energy.
- Shear mode fracture energy for failure in the first shear direction.
- Shear mode fracture energy for failure in the second shear direction.
- Temperature, if the data depend on temperature.
- Value of the first field variable, if the data depend on field variables.
- Value of the second field variable.
- Etc.

### Return value

A ContactDamage object.

### Exceptions

None.



## setValues(...)



This method modifies the ContactDamage object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ContactDamage ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactdamagepyc.htm?ContextScope=all#simaker-contactdamagedamagepyc)method.

### Return value

None.

### Exceptions

None.



## Members

The ContactDamage object has the following members:

- *criterion*

  A SymbolicConstant specifying the type of data used to define the initiation of damage. Possible values are MAX_STRESS, MAX_SEPARATION, QUAD_TRACTION, and QUAD_SEPARATION. The default value is MAX_STRESS.

- *initTempDep*

  A Boolean specifying whether the initiation data depend on temperature. The default value is OFF.

- *initDependencies*

  An Int specifying the number of initiation data field variables. The default value is 0.

- *useEvolution*

  A Boolean specifying whether evolution data will be defined. The default value is OFF.

- *evolutionType*

  A SymbolicConstant specifying the type of data used to define the evolution of damage. This argument is valid only when *useEvolution*=ON. Possible values are DISPLACEMENT and ENERGY. The default value is DISPLACEMENT.

- *softening*

  A SymbolicConstant specifying the type of data used to define the evolution softening response. This argument is valid only when *useEvolution*=ON. The TABULAR value can be used only when *evolutionType*=DISPLACEMENT. Possible values are LINEAR, EXPONENTIAL, and TABULAR. The default value is LINEAR.

- *useMixedMode*

  A Boolean specifying whether evolution data be defined using dependent behavior modes. This argument is valid only when *useEvolution*=ON. The default value is OFF.

- *mixedModeType*

  A SymbolicConstant specifying the mode mix fracture criterion. This argument is valid only when *useEvolution*=ON and when *useMixedMode*=ON. The POWER_LAW and BK values can be used only when *evolutionType*=ENERGY. Possible values are TABULAR, POWER_LAW, and BK. The default value is TABULAR.

- *modeMixRatio*

  A SymbolicConstant specifying the mode mix ratio type. This argument is valid only when *useEvolution*=ON and when *useMixedMode*=ON. The TRACTION value can be used only when *mixedModeType*=TABULAR. Possible values are ENERGY and TRACTION. The default value is ENERGY.

- *exponent*

  None or a Float specifying the exponent in the power-law or BK criterion that defines the variation of fracture energy with mode mix. This argument is valid only when *useEvolution*=ON and when *mixedModeType*=POWER_LAW or BK. The default value is None.

- *evolTempDep*

  A Boolean specifying whether the evolution data depend on temperature. This argument is valid only when *useEvolution*=ON. The default value is OFF.

- *evolDependencies*

  An Int specifying the number of evolution data field variables. This argument is valid only when *useEvolution*=ON. The default value is 0.

- *useStabilization*

  A Boolean specifying whether stabilization data will be defined. This argument is valid only when *useEvolution*=ON. The default value is OFF.

- *viscosityCoef*

  None or a Float specifying the viscosity coefficient. This argument is valid only when *useStabilization*=ON. The default value is None.

- *initTable*

  A tuple of tuples of Floats specifying the values defining the damage initiation. The items in the table data are described below.

- *evolTable*

  A tuple of tuples of Floats specifying the values defining the damage evolution. The items in the table data are described below. This argument is valid only when *useEvolution*=ON.



## Corresponding analysis keywords

- [DAMAGE INITIATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damageinitiation.htm?ContextScope=all#simakey-r-damageinitiation)
- [DAMAGE EVOLUTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damageevolution.htm?ContextScope=all#simakey-r-damageevolution)
- [DAMAGE STABILIZATION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-damagestabilization.htm?ContextScope=all#simakey-r-damagestabilization)