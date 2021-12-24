# DiagnosticPrint object

The DiagnosticPrint object is used to request detailed diagnostic output or to disable specific diagnostic checks

## Access

```
import step
mdb.models[name].steps[name].diagnosticPrint
```

## DiagnosticPrint(...)



This method creates a DiagnosticPrint object.



### Path

```
mdb.models[name].steps[name].DiagnosticPrint
```

### Required arguments

None.

### Optional arguments

- *allke*

  A Boolean specifying a request for a column containing the total kinetic energy. This argument is valid only for an Abaqus/Explicit analysis. The default value is ON.

- *criticalElement*

  A Boolean specifying a request for a column containing the element that has the smallest stable time increment and a column listing the value. This argument is valid only for an Abaqus/Explicit analysis. The default value is ON.

- *dmass*

  A Boolean specifying a request for a column containing the percent change in total mass of the model as a result of mass scaling. This argument is valid only for an Abaqus/Explicit analysis. The default value is OFF unless mass scaling is present in the model.

- *etotal*

  A Boolean specifying a request for a column containing the energy balance of the model. This argument is valid only for an Abaqus/Explicit analysis. The default value is OFF.

- *contact*

  A Boolean specifying a request for detailed output of points that are contacting or separating in interface and gap problems. This argument is valid only for an Abaqus/Standard analysis. The default value is ON.

- *modelChange*

  A Boolean specifying a request for detailed output of which elements are being removed or reactivated in the step. This argument is valid only for an Abaqus/Standard analysis. The default value is OFF.

- *plasticity*

  A Boolean specifying a request for detailed output of element and integration point numbers for which the plasticity algorithms have failed to converge in the material routines. This argument is valid only for an Abaqus/Standard analysis. The default value is OFF.

- *residual*

  A Boolean specifying a request for output of equilibrium residuals during the equilibrium iterations. This argument is valid only for an Abaqus/Standard analysis. The default value is ON.

- *frequency*

  An Int specifying the frequency of output, in increments. The default value is 1.

- *solve*

  A Boolean specifying a request for information regarding the actual number of equations and the wavefront in each iteration. This argument is valid only for an Abaqus/Standard analysis. The default value is ON.

- *mass*

  A Boolean specifying a request for a column containing the total mass of the model as a result of mass scaling. This argument is valid only for an Abaqus/Explicit analysis. The default value is OFF.

### Return value

A DiagnosticPrint object.

### Exceptions

None.



## setValues(...)



This method modifies the DiagnosticPrint object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DiagnosticPrint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diagnosticprintpyc.htm?ContextScope=all#simaker-diagnosticprintdiagnosticprintpyc)method.

### Return value

None.

### Exceptions

None.



## Members

The DiagnosticPrint object has members with the same names and descriptions as the arguments to the [DiagnosticPrint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diagnosticprintpyc.htm?ContextScope=all#simaker-diagnosticprintdiagnosticprintpyc)method.



## Corresponding analysis keywords

- [DIAGNOSTICS](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-diagnostics.htm?ContextScope=all#simakey-r-diagnostics)