# LayerProperties object

The LayerProperties object defines the properties of a layer of reinforcement for membrane, shell, and surface sections.

## Access

```
import section
mdb.models[name].parts[name].compositeLayups[i].section.rebarLayers\
.layerTable[i]
mdb.models[name].sections[name].rebarLayers.layerTable[i]
import odbSection
session.odbs[name].sections[name].rebarLayers.layerTable[i]
```

## LayerProperties(...)



This method creates a LayerProperties object.



### Path

section.LayerProperties

odbSection.LayerProperties

### Required arguments

- *barArea*

  A Float specifying the area per bar.

- *orientationAngle*

  A Float or a String specifying the orientation of the rebar. A Float specifies the angular orientation; a String specifies an orientation name.

- *layerName*

  A String specifying the name of the rebar layer.

- *material*

  A String specifying the name of the rebar material.

### Optional arguments

- *barSpacing*

  A Float specifying the spacing of the rebar. This argument is only valid if the *rebarSpacing* argument on the parent [RebarLayers](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all) object is set to CONSTANT. The default value is 0.0.

- *layerPosition*

  A Float specifying the position of the rebar from the middle surface of the shell. *layerPosition* applies only for homogeneous shell sections and composite shell sections. The default value is 0.0.

- *spacingAngle*

  A Float specifying the spacing angle of the rebar. This argument is only valid if the *rebarSpacing* argument on the parent [RebarLayers](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all) object is set to ANGULAR. The default value is 0.0.

- *extensionRatio*

  A Float specifying the extension ratio for the rebar. This argument is only valid if the *rebarSpacing* argument on the parent [RebarLayers](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all) object is set to LIFT_EQUATION. The default value is 0.0.

- *radius*

  A Float specifying the radius of the rebar. This argument is only valid if the *rebarSpacing* argument on the parent [RebarLayers](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarlayerspyc.htm?ContextScope=all) object is set to LIFT_EQUATION. The default value is 0.0.

### Return value

A LayerProperties object.

### Exceptions

None.



## Members

The LayerProperties object has members with the same names and descriptions as the arguments to the [LayerProperties ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-layerpropertiespyc.htm?ContextScope=all#simaker-layerpropertieslayerpropertiespyc)method.



## Corresponding analysis keywords

- [REBAR LAYER](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-rebarlayer.htm?ContextScope=all#simakey-r-rebarlayer)