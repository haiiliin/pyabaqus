# OdbStep object

An output database contains the same steps of the model database that originated it.

## Access

```
import odbAccess
session.odbs[name].steps[name]
```

## Step(...)



This method creates an OdbStep object.



### Path

```
session.odbs[name].Step
```

### Required arguments

- *name*

  A String specifying the repository key.

- *description*

  A String specifying the step description.

- *domain*

  A SymbolicConstant specifying the domain of the step. Possible values are TIME, FREQUENCY, ARC_LENGTH, and MODAL.The type of [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object that can be created for this step is based on the value of the *domain* argument.

### Optional arguments

- *timePeriod*

  A Float specifying the time period of the step. *timePeriod* is required if *domain*=TIME; otherwise, this argument is not applicable. The default value is 0.0.

- *previousStepName*

  A String specifying the preceding step. If *previousStepName* is the empty string, the last step in the repository is used. If *previousStepName* is not the last step, this will result in a change to the *previousStepName* member of the step that was in that position. A special value 'Initial' refers to the internal initial model step and may be used exclusively for inserting a new step at the first position before any other existing steps. The default value is an empty string.

- *procedure*

  A String specifying the step procedure. The default value is an empty string. The following is the list of valid procedures:

  ```
  *ANNEAL
  *BUCKLE
  *COMPLEX FREQUENCY
  *COUPLED TEMPERATURE-DISPLACEMENT
  *COUPLED TEMPERATURE-DISPLACEMENT, CETOL
  *COUPLED TEMPERATURE-DISPLACEMENT, STEADY STATE
  *COUPLED THERMAL-ELECTRICAL, STEADY STATE
  *COUPLED THERMAL-ELECTRICAL
  *COUPLED THERMAL-ELECTRICAL, DELTMX
  *DYNAMIC
  *DYNAMIC, DIRECT
  *DYNAMIC, EXPLICIT
  *DYNAMIC, SUBSPACE
  *DYNAMIC TEMPERATURE-DISPLACEMENT, EXPLICT
  *ELECTROMAGNETIC, HIGH FREQUENCY, TIME HARMONIC
  *ELECTROMAGNETIC, LOW FREQUENCY, TIME DOMAIN
  *ELECTROMAGNETIC, LOW FREQUENCY, TIME DOMAIN, DIRECT
  *ELECTROMAGNETIC, LOW FREQUENCY, TIME HARMONIC
  *FREQUENCY
  *GEOSTATIC
  *HEAT TRANSFER
  *HEAT TRANSFER, DELTAMX=__ 
  *HEAT TRANSFER, STEADY STATE
  *MAGNETOSTATIC
  *MAGNETOSTATIC, DIRECT
  *MASS DIFFUSION
  *MASS DIFFUSION, DCMAX=
  *MASS DIFFUSION, STEADY STATE
  *MODAL DYNAMIC
  *RANDOM RESPONSE
  *RESPONSE SPECTRUM
  *SOILS
  *SOILS, CETOL/UTOL
  *SOILS, CONSOLIDATION
  *SOILS, CONSOLIDATION, CETOL/UTOL
  *STATIC
  *STATIC, DIRECT
  *STATIC, RIKS
  *STEADY STATE DYNAMICS
  *STEADY STATE TRANSPORT
  *STEADY STATE TRANSPORT, DIRECT
  *STEP PERTURBATION, *STATIC
  *SUBSTRUCTURE GENERATE
  *USA ADDDED MASS GENERATION
  *VISCO
  ```

- *totalTime*

  A Float specifying the analysis time spend in all the steps previous to this step. The default value is −1.0.

### Return value

An OdbStep object.

### Exceptions

- If *previousStepName* is invalid:

  ValueError: previousStepName is invalid



## getFrame(...)



This method retrieves an [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object associated with a given frame value.



### Required arguments

- *frameValue*

  A Double specifying the value at which the frame is required. *frameValue* can be the step time or frequency.

### Optional arguments

- *match*

  A SymbolicConstant specifying which frame to return if there is no frame at the exact frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is CLOSEST.When *match*=CLOSEST, Abaqus returns the closest frame. If the frame value requested is exactly halfway between two frames, Abaqus returns the frame after the value.When *match*=EXACT, Abaqus raises an exception if the exact frame value does not exist.

### Return value

An [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object.

### Exceptions

- If the [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object is not found:

  OdbError: Frame not found.



## getFrame(...)



This method retrieves an [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object associated with a given load case.



### Required arguments

- *loadCase*

  An [OdbLoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?ContextScope=all) object specifying a load case in the step.

### Optional arguments

None.

### Return value

An [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object.

### Exceptions

- If the [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object is not found:

  OdbError: Frame not found.



## getFrame(...)



This method retrieves an [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object associated with a given load case and frame value.



### Required arguments

- *loadCase*

  An [OdbLoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?ContextScope=all) object specifying a load case in the step.

- *frameValue*

  A Double specifying the value at which the frame is required. *frameValue* can be the step time or frequency.

### Optional arguments

- *match*

  A SymbolicConstant specifying which frame to return if there is no frame at the exact frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is CLOSEST.When *match*=CLOSEST, Abaqus returns the closest frame. If the frame value requested is exactly halfway between two frames, Abaqus returns the frame after the value.When *match*=EXACT, Abaqus raises an exception if the exact frame value does not exist.

### Return value

An [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object.

### Exceptions

- If the [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object is not found:

  OdbError: Frame not found.



## getHistoryRegion(...)



This method retrieves a [HistoryRegion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyregionpyc.htm?ContextScope=all) object associated with a HistoryPoint in the model.



### Required arguments

- *point*

  A [HistoryPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historypointpyc.htm?ContextScope=all) object specifying the point in the model.

### Optional arguments

- *loadCase*

  An [OdbLoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?ContextScope=all) object specifying a load case in the step.

### Return value

A [HistoryRegion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyregionpyc.htm?ContextScope=all) object.

### Exceptions

- If a [HistoryRegion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyregionpyc.htm?ContextScope=all) object is not found:

  OdbError: HistoryRegion not found.



## setDefaultDeformedField(...)



This method sets the default deformed field variable in a step.



### Required arguments

- *field*

  A [FieldOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?ContextScope=all) object specifying the default deformed field variable for visualization.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## setDefaultField(...)



This method sets the default field variable in a step.



### Required arguments

- *field*

  A [FieldOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?ContextScope=all) object specifying the default field variable for visualization.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The OdbStep object has members with the same names and descriptions as the arguments to the [Step](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsteppyc.htm?ContextScope=all#simaker-odbstepsteppyc) method.

In addition, the OdbStep object can have the following members:

- *number*

  An Int specifying the step number.

- *nlgeom*

  A Boolean specifying whether geometric nonlinearity can occur in this step.

- *mass*

  A Float specifying the current value of the mass of the model. This does not include the mass of the acoustic media if any present.

- *acousticMass*

  A Float specifying the current value of the mass of the acoustic media of the model.

- *frames*

  An [OdbFrameArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object.

- *historyRegions*

  A repository of [HistoryRegion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyregionpyc.htm?ContextScope=all) objects.

- *loadCases*

  A repository of [OdbLoadCase](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?ContextScope=all) objects.

- *massCenter*

  A tuple of Floats specifying the coordinates of the center of mass.

- *inertiaAboutCenter*

  A tuple of Floats specifying the moments and products of inertia about the center of mass. For 3-D models inertia quantities are written in the following order: I(XX), I(YY), I(ZZ), I(XY), I(XZ), and I(YZ). For 2-D models only I(ZZ) and I(XY) are outputted.

- *inertiaAboutOrigin*

  A tuple of Floats specifying the moments and products of inertia about the origin of the global coordinate system. For 3-D models inertia quantities are written in the following order: I(XX), I(YY), I(ZZ), I(XY), I(XZ), and I(YZ). For 2-D models only I(ZZ) and I(XY) are outputted.

- *acousticMassCenter*

  A tuple of Floats specifying the coordinates of the center of mass of the acoustic media.