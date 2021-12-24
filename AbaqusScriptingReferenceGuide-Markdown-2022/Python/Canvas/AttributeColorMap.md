# AttributeColorMap object

The AttributeColorMap object is used to store values and attributes associated with AttributeColorMap type objects. AttributeColorMap objects can be modified using the methods described below. The methods accessed via the [Viewport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewportpyc.htm?ContextScope=all) object cause the AttributeColorMap object to be updated in the session.viewports[name].colorMappings repository.

## Access

```
session.viewports[name].colorMappings[name]
```

## setDefaults()



This method resets the AttributeColorMap object to its default state.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the AttributeColorMap object.



### Required arguments

None.

### Optional arguments

At least one of the following must be provided:

- *overrides*

  A Dictionary object specifying a color mapping. Each key is of String type and specifies an attribute in the map; the corresponding values specify the color definition to apply to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines the active status for the attribute. For example:`overrides={                        'Part-1':(1,'#00FF00', '#00CCFF',                        '#00FF00')}`

- *defaultOverrides*

  A Dictionary object specifying a custom color mapping similar to overrides. For example:`defaultOverrides={                        'Copper':(1,''#00FF00', '#00CCFF',                        '#00FF00')}`The color mapping can contain keys that have not been created. When the key is created, it gets the appropriate values from this mapping.

### Return value

None.

### Exceptions

None.



## updateOverrides(...)



This method specifies additional overrides to be added to the current object definition.



### Required arguments

None.

### Optional arguments

At least one of the following must be provided:

- *overrides*

  A Dictionary object specifying a color mapping. Each key is of String type and specifies an attribute in the map; the corresponding values specify the color definition to apply to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines the active status for the attribute. For example:`overrides={                        'Part-1':(1,'#00FF00', '#00CCFF',                        '#00FF00')}`

- *defaultOverrides*

  A Dictionary object specifying a custom color mapping similar to overrides. For example:`defaultOverrides={                        'Copper':(1,''#00FF00', '#00CCFF',                        '#00FF00')}`The color mapping can contain keys that have not been created. When the key is created, it gets the appropriate values from this mapping.

### Return value

None.

### Exceptions

None.



## Members

The AttributeColorMap object has the following members:

- *mapType*

  A SymbolicConstant specifying the type of AttributeColorMap . Possible values are MATERIAL_MAP, SECTION_MAP, PART_MAP, ELSET_MAP, AVERAGING_REGION_MAP, and ELTYPE_MAP.

- *overrides*

  A Dictionary object specifying a color mapping. Each key is of String type and specifies an attribute in the map; the corresponding values specify the color definition to apply to that attribute in the form (0|1, wire color, edge color, face color). The 0|1 defines the active status for the attribute. For example:`overrides={                        'Part-1':(1,'#00FF00', '#00CCFF',                        '#00FF00')}`

- *defaultOverrides*

  A Dictionary object specifying a custom color mapping similar to overrides. For example:`defaultOverrides={                        'Copper':(1,''#00FF00', '#00CCFF',                        '#00FF00')}`The color mapping can contain keys that have not been created. When the key is created, it gets the appropriate values from this mapping.

- *attributeColors*

  A Dictionary object specifying the color settings of each attribute as described in the [updateOverrides ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-attributecolormappyc.htm?ContextScope=all#simaker-attributecolormapupdateoverridespyc)method.