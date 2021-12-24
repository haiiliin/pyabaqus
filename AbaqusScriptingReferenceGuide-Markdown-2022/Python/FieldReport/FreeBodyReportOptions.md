# FreeBodyReportOptions object

The FreeBodyReportOptions object stores settings used by the writeFreeBodyReport method when you write free body computational results to an ASCII file. The FreeBodyReportOptions object has no constructor. Abaqus creates the *freeBodyReportOptions* member when you import the Visualization module.

## Access

```
import visualization
session.defaultFreeBodyReportOptions
session.freeBodyReportOptions
```

## setValues(...)



This method modifies the FreeBodyReportOptions object.



### Required arguments

None.

### Optional arguments

- *numDigits*

  An Int specifying the number of decimal places. The default value is 3.

- *forceThreshold*

  A Float specifying the threshold value for force. The default value is 10–6.

- *momentThreshold*

  A Float specifying the threshold value for moment. The default value is 10–6.

- *numberFormat*

  A SymbolicConstant specifying the number format. Possible values are SCIENTIFIC, FIXED, and ENGINEERING. The default value is SCIENTIFIC.

- *reportFormat*

  A SymbolicConstant specifying the report format. Possible values are NORMAL_ANNOTATED and COMMA_SEPARATED_VALUES. The default value is NORMAL_ANNOTATED.

- *csysType*

  A SymbolicConstant specifying the coordinate system type. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.

### Return value

A FreeBodyReportOptions object.

### Exceptions

None.



## Members

The FreeBodyReportOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-freebodyreportoptionspyc.htm?ContextScope=all#simaker-freebodyreportoptionssetvaluespyc)method.