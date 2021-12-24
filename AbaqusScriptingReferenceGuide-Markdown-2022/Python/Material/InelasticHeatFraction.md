# InelasticHeatFraction object

The InelasticHeatFraction object defines the fraction of the rate of inelastic dissipation that appears as a heat source.

## Access

```
import material
mdb.models[name].materials[name].inelasticHeatFraction
import odbMaterial
session.odbs[name].materials[name].inelasticHeatFraction
```

## InelasticHeatFraction(...)



This method creates an InelasticHeatFraction object.



### Path

```
mdb.models[name].materials[name].InelasticHeatFraction
session.odbs[name].materials[name].InelasticHeatFraction
```

### Required arguments

None.

### Optional arguments

- *fraction*

  A Float specifying the fraction of inelastic dissipation rate that appears as a heat flux per unit volume. The fraction may include a unit conversion factor if required. Possible values are 0.0 ≤≤ *fraction* ≤≤ 1.0. The default value is 0.9.

### Return value

An InelasticHeatFraction object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the InelasticHeatFraction object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [InelasticHeatFraction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inelasticheatfractionpyc.htm?ContextScope=all#simaker-inelasticheatfractioninelasticheatfractionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The InelasticHeatFraction object has members with the same names and descriptions as the arguments to the [InelasticHeatFraction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inelasticheatfractionpyc.htm?ContextScope=all#simaker-inelasticheatfractioninelasticheatfractionpyc)method.



## Corresponding analysis keywords

- [INELASTIC HEAT FRACTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-inelasticheatfraction.htm?ContextScope=all#simakey-r-inelasticheatfraction)