# EventSeries object

The EventSeries object is used to define an event based on an already defined EventSeriesType object.

After EventSeries is instantiated, making changes to EventSeriesType may lead to data corruption.

## Access

```
mdb.models[name].eventSeriesDatas[name]
```

## EventSeries(...)

This method creates an EventSeries object.

### Path

```
mdb.models[name].EventSeriesData
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A string specifying the step name.

- *eventSeriesType*

  A string specifying the type of event series.

### Optional arguments

- *transformType*

  A Symbolic constant specifying the type of transformation. Possible values are NONE, BOTH, TRANSLATE, and ROTATE. The default value is NONE.

- *timeSpan*

  A Symbolic constant specifying time. Possible values are TOTAL_TIME and STEP_TIME. The default value is STEP_TIME.

- *transformations*

  An Array specifying the required transformations over event series data.

- *fileName*

  A String specifying the filename.

- *data*

  An Array of double specifying the values of fields provided in EventSeriesType.

### Return value

An EventSeries object.

### Exceptions

RangeError.



## setValues(...)

This method modifies the EventSeries object.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [EventSeries](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eventseriespyc.htm?ContextScope=all#simaker-eventserieseventseriespyc) method, except for the *name* argument.

### Exceptions

RangeError.



## Members

The EventSeries object has members with the same names and descriptions as the arguments to the [EventSeries](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eventseriespyc.htm?ContextScope=all#simaker-eventserieseventseriespyc) method.



## Corresponding analysis keywords

- [EVENT SERIES TYPE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-eventseries.htm?ContextScope=all#simakey-r-eventseries)
- [EVENT SERIES](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-propertytable.htm?ContextScope=all#simakey-r-propertytable)