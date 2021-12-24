# OdbDisplayOptions object

The OdbDisplayOptions object stores the display options associated with an [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) object. This object does not have a constructor. Abaqus creates the OdbDisplayOptions object when an [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) object is created using the display options associated with the current viewport at the time of creation.

## Access

```
import assembly
session.viewports[name].assemblyDisplay.displayGroupInstances[name]\
.odbDisplayOptions
session.viewports[name].layers[name].assemblyDisplay\
.displayGroupInstances[name].odbDisplayOptions
import visualization
session.viewports[name].layers[name].odbDisplay\
.displayGroupInstances[name].odbDisplayOptions
import part
session.viewports[name].layers[name].partDisplay\
.displayGroupInstances[name].odbDisplayOptions
session.viewports[name].odbDisplay.displayGroupInstances[name]\
.odbDisplayOptions
session.viewports[name].partDisplay.displayGroupInstances[name]\
.odbDisplayOptions
```

## Members

The OdbDisplayOptions object has the following members:

- *commonOptions*

  A [DGCommonOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgcommonoptionspyc.htm?ContextScope=all) object.

- *superimposeOptions*

  A [DGSuperimposeOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgsuperimposeoptionspyc.htm?ContextScope=all) object.

- *contourOptions*

  A [DGContourOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgcontouroptionspyc.htm?ContextScope=all) object.

- *symbolOptions*

  A [DGSymbolOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgsymboloptionspyc.htm?ContextScope=all) object.

- *materialOrientationOptions*

  A [DGOrientationOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgorientationoptionspyc.htm?ContextScope=all) object.

- *displayBodyOptions*

  A [DGDisplayBodyOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-dgdisplaybodyoptionspyc.htm?ContextScope=all) object.