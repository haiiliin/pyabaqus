# EventSeriesType object

The EventSeriesType object is used to define a type of event in a process.

## Access

```
mdb.models[name].eventSeriesTypes[name]
```

## EventSeriesType(...)

This method creates an EventSeriesType object.

### Path

```
mdb.models[name].EventSeriesType
```

### Required arguments

- *name*

  A String specifying the repository key.

- *createStepName*

  A string specifying the step name.

### Optional arguments

- *fields*

  A String array specifying fields. The default value is an empty array.

### Return value

A EventSeriesType object.

### Exceptions

RangeError.



## setValues(...)

This method modifies the EventSeriesType object.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [EventSeriesType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eventseriestypepyc.htm?ContextScope=all#simaker-eventseriestypeeventseriestypepyc) method, except for the *name* argument.

### Exceptions

RangeError.



## Members

The EventSeriesType object has members with the same names and descriptions as the arguments to the [EventSeriesType](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eventseriestypepyc.htm?ContextScope=all#simaker-eventseriestypeeventseriestypepyc) method.



## Corresponding analysis keywords

- [EVENT SERIES TYPE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-eventseriestype.htm?ContextScope=all#simakey-r-eventseriestype)
- [EVENT SERIES](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-propertytable.htm?ContextScope=all#simakey-r-propertytable)