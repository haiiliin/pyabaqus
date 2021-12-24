# UserData object

The UserData object contains user-defined XY data. The UserData object has no constructor; it is created automatically when an [Odb](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?ContextScope=all) object is created.

## Access

```
import odbAccess
session.odbs[name].userData
```

## XYData(...)



This method creates an [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) object from a sequence of *X–Y* data pairs.



### Path

session.odbs[name].userData.XYData

### Required arguments

- *name*

  A String specifying the repository key.

- *data*

  A sequence of pairs of Floats specifying the *X–Y* data pairs.

### Optional arguments

- *sourceDescription*

  A String specifying the source of the *X–Y* data (e.g., “Entered from keyboard”, “Taken from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string.

- *contentDescription*

  A String specifying the content of the *X–Y* data (e.g., “field 1 vs. field 2”). The default value is an empty string.

- *positionDescription*

  A String specifying additional information about the *X–Y* data (e.g., “for whole model”). The default value is an empty string.

- *legendLabel*

  A String specifying the label to be used in the legend. The default value is the name of the XYData object.

- *xValuesLabel*

  A String specifying the label for the X-values. This value may be overridden if the *X–Y* data are combined with other *X–Y* data. The default value is an empty string.

- *yValuesLabel*

  A String specifying the label for the Y-values. This value may be overridden if the *X–Y* data are combined with other *X–Y* data. The default value is an empty string.

- *axis1QuantityType*

  A [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object specifying the [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object associated to the X -axis1- values.

- *axis2QuantityType*

  A [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object specifying the [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object associated to the Y -axis2- values.

### Return value

An [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) object.

### Exceptions

InvalidNameError.



## Members

The UserData object can have the following members:

- *name*

  A String specifying the repository key.

- *sourceDescription*

  A String specifying the source of the *X–Y* data (e.g., “Entered from keyboard”, “Taken from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string.

- *contentDescription*

  A String specifying the content of the *X–Y* data (e.g., “field 1 vs. field 2”). The default value is an empty string.

- *positionDescription*

  A String specifying additional information about the *X–Y* data (e.g., “for whole model”). The default value is an empty string.

- *xValuesLabel*

  A String specifying the label for the X-values. This value may be overridden if the *X–Y* data are combined with other *X–Y* data. The default value is an empty string.

- *yValuesLabel*

  A String specifying the label for the Y-values. This value may be overridden if the *X–Y* data are combined with other *X–Y* data. The default value is an empty string.

- *axis1QuantityType*

  A [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object specifying the [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object associated to the X -axis1- values.

- *axis2QuantityType*

  A [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object specifying the [QuantityType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quantitytypepyc.htm?ContextScope=all) object associated to the Y -axis2- values.

- *legendLabel*

  A String specifying the label to be used in the legend. The default value is the name of the XYData object.

- *xyDataObjects*

  A repository of [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) objects.

- *annotations*

  A repository of [Annotation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) objects.

- *data*

  A tuple of pairs of Floats specifying the *X–Y* data pairs.