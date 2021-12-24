# JouleHeatFraction object

The JouleHeatFraction object defines the fraction of electric energy released as heat.

## Access

```
import material
mdb.models[name].materials[name].jouleHeatFraction
import odbMaterial
session.odbs[name].materials[name].jouleHeatFraction
```

## JouleHeatFraction(...)



This method creates a JouleHeatFraction object.



### Path

```
mdb.models[name].materials[name].JouleHeatFraction
session.odbs[name].materials[name].JouleHeatFraction
```

### Required arguments

None.

### Optional arguments

- *fraction*

  A Float specifying the fraction of electrical energy released as heat, including any unit conversion factor. The default value is 1.0.

### Return value

A JouleHeatFraction object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the JouleHeatFraction object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [JouleHeatFraction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jouleheatfractionpyc.htm?ContextScope=all#simaker-jouleheatfractionjouleheatfractionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The JouleHeatFraction object has members with the same names and descriptions as the arguments to the [JouleHeatFraction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jouleheatfractionpyc.htm?ContextScope=all#simaker-jouleheatfractionjouleheatfractionpyc)method.



## Corresponding analysis keywords

- [JOULE HEAT FRACTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-jouleheatfraction.htm?ContextScope=all#simakey-r-jouleheatfraction)