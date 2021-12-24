# FluidInflatorProperty object

The FluidInflatorProperty object is an interaction property that defines a fluid inflator property to model the deployment of an airbag. The inflator property defines the mass flow rate and temperature as a function of inflation time either directly or by entering tank test data. It also defines the mixture of gases entering the fluid cavity.

The FluidInflatorProperty object is derived from the [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactionProperties[name]
```

## FluidInflatorProperty(...)



This method creates a FluidInflatorProperty object.



### Path

```
mdb.models[name].FluidInflatorProperty
```

### Required arguments

- *name*

  A String specifying the interaction property repository key.

- *definition*

  A Symbolic constant specifying the method used for modeling the flow characteristics of inflators. The default value is *definition*=DUAL PRESSURE. The possible values are DUAL PRESSURE, PRESSURE AND MASS, TANK TEST, and TEMPERATURE AND MASS.

- *effectiveArea*

  A Float specifying the total inflator orifice area. This argument is applicable only if *definition*=DUAL PRESSURE or *definition*=PRESSURE AND MASS.

- *tankVolume*

  A Float specifying the tank volume. This argument is applicable only if *definition*=DUAL PRESSURE or *definition*=TANK TEST.

### Optional arguments

- *dischargeCoefficient*

  A Float specifying the discharge coefficient. This argument is applicable only if *definition*=DUAL PRESSURE or *definition*=PRESSURE AND MASS.

- *dataTable*

  A sequence of sequences of Floats specifying the items described in the "Table data" section below.

- *numFluids*

  An Int specifying the number of gas species used for this inflator.

- *mixtureType*

  A Symbolic constant specifying whether to use mass fraction or the molar fraction for a mixture of ideal gases. The default value is MASS FRACTION. The possible values are MASS FRACTION or MOLAR FRACTION.

- *inflationTime*

  A sequence of sequences of Floats specifying the inflation time.

- *fluidbehaviorName*

  A sequence of sequences of Strings specifying fluid behavior names.

- *massFraction*

  A sequence of sequences of Floats specifying the mass fraction or the molar fraction corresponding to entered fluid behavior.

### Table data

If *definition*=DUAL PRESSURE, the table data specify the following:

- Inflation time.
- Inflator pressure.
- Tank pressure.



If *definition*=PRESSURE AND MASS, the table data specify the following:

- Inflation time.
- Inflator pressure.
- Inflator mass flow rate.



If *definition*=TANK TEST, the table data specify the following:

- Inflation time.
- Inflator gas temperature.
- Tank pressure.



If *definition*=TEMPERATURE AND MASS, the table data specify the following:

- Inflation time.
- Inflator gas temperature.
- Inflator mass flow rate.



### Return value

A FluidInflatorProperty object.

### Exceptions

None.



## setValues(...)



This method modifies the FluidInflatorProperty object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [FluidInflatorProperty ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidinflatorpropertypyc.htm?ContextScope=all#simaker-fluidinflatorpropertypyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The FluidInflatorProperty object has members with the same names and descriptions as the arguments to the [FluidInflatorProperty ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidinflatorpropertypyc.htm?ContextScope=all#simaker-fluidinflatorpropertypyc)method.



## Corresponding analysis keywords

- [FLUID INFLATOR PROPERTY](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-fluidinflatorproperty.htm?ContextScope=all#simakey-r-fluidinflatorproperty)