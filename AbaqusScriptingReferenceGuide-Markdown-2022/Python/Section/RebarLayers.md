# RebarLayers object

The RebarLayers object defines the rebar properties of a section.

## Access

```
import section
mdb.models[name].parts[name].compositeLayups[i].section.rebarLayers
mdb.models[name].sections[name].rebarLayers
import odbSection
session.odbs[name].sections[name].rebarLayers
```

## RebarLayers(...)



This method creates a RebarLayers object.



### Path

```
mdb.models[name].parts[name].compositeLayups[i].section.RebarLayers
mdb.models[name].sections[name].RebarLayers
session.odbs[name].sections[name].RebarLayers
```

### Required arguments

- *rebarSpacing*

  A SymbolicConstant specifying the type of rebar geometry. Possible values are CONSTANT, ANGULAR, and LIFT_EQUATION.

- *layerTable*

  A [LayerPropertiesArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-layerpropertiespyc.htm?ContextScope=all) object specifying the layers of reinforcement.

### Optional arguments

None.

### Return value

A RebarLayers object.

### Exceptions

None.



## setValues(...)



This method modifies the RebarLayers object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [RebarLayers ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all#simaker-rebarlayersrebarlayerspyc)method.

### Return value

None.

### Exceptions

None.



## Members

The RebarLayers object has members with the same names and descriptions as the arguments to the [RebarLayers ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all#simaker-rebarlayersrebarlayerspyc)method.



## Corresponding analysis keywords

- [REBAR LAYER](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-rebarlayer.htm?ContextScope=all#simakey-r-rebarlayer)