# HistoryRegion object

The HistoryRegion object contains history data for a single location in the model.

## Access

```
import odbAccess
session.odbs[name].steps[name].historyRegions[name]
```

## HistoryRegion(...)



This method creates a HistoryRegion object.



### Path

```
session.odbs[name].steps[name].HistoryRegion
```

### Required arguments

- *name*

  A String specifying the name of the HistoryRegion object.

- *description*

  A String specifying the description of the HistoryRegion object.

- *point*

  A [HistoryPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historypointpyc.htm?ContextScope=all) object specifying the point to which the history data refer.

### Optional arguments

- *loadCase*

  None or an [OdbLoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?ContextScope=all) object specifying the load case associated with the HistoryRegion object. The default value is None.

### Return value

A HistoryRegion object.

### Exceptions

None.



## getSubset(...)



This method returns a subset of the data in the HistoryRegion object.



### Required arguments

- *variableName*

  A String specifying the name of the output variable to return.

### Optional arguments

None.

### Return value

A HistoryRegion object.

### Exceptions

None.



## getSubset(...)



This method returns a subset of the data in the HistoryRegion object.



### Required arguments

- *start*

  A Float specifying the start of the subset. This is the same as the first item in the data array member of the [HistoryOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputpyc.htm?ContextScope=all) object.

### Optional arguments

None.

### Return value

A HistoryRegion object.

### Exceptions

None.



## getSubset(...)



This method returns a subset of the data in the HistoryRegion object.



### Required arguments

- *start*

  A Float specifying the start of the subset. This is the same as the first item in the data array member of the [HistoryOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputpyc.htm?ContextScope=all) object.

- *end*

  A Float specifying the end of the subset.

### Optional arguments

None.

### Return value

A HistoryRegion object.

### Exceptions

None.



## Members

The HistoryRegion object has members with the same names and descriptions as the arguments to the [HistoryRegion ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyregionpyc.htm?ContextScope=all#simaker-historyregionhistoryregionpyc)method.

In addition, the HistoryRegion object can have the following members:

- *position*

  A SymbolicConstant specifying the position of the history output. Possible values are NODAL, INTEGRATION_POINT, WHOLE_ELEMENT, WHOLE_REGION, and WHOLE_MODEL.

- *historyOutputs*

  A repository of [HistoryOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputpyc.htm?ContextScope=all) objects.