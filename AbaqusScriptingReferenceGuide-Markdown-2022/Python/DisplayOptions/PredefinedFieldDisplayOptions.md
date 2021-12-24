# PredefinedFieldDisplayOptions object

The PredefinedFieldDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport when

```
session.viewports[name].assemblyDisplay.predefinedFields=ON
```

The PredefinedFieldDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.

## Access

```
session.viewports[name].assemblyDisplay.predefinedFieldOptions
session.viewports[name].layers[name].assemblyDisplay\
.predefinedFieldOptions
```

## setValues(...)



This method modifies the PredefinedFieldDisplayOptions object.



### Required arguments

None.

### Optional arguments

- *temperatureField*

  A Boolean specifying whether temperature field symbols are shown. The default value is ON.

- *velocityField*

  A Boolean specifying whether translational velocity symbols are shown. The default value is ON.

- *generalField*

  A Boolean specifying whether general field symbols are shown. The default value is ON.

- *stressField*

  A Boolean specifying whether stress field symbols are shown. The default value is ON.

- *hardeningField*

  A Boolean specifying whether hardening field symbols are shown. The default value is ON.

### Return value

None.

### Exceptions

RangeError.



## Members

The PredefinedFieldDisplayOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfielddisplayoptionspyc.htm?ContextScope=all#simaker-predefinedfielddisplayoptionssetvaluespyc)method.