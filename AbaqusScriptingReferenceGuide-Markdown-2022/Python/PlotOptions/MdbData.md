# MdbData object

The MdbData object has no constructor. Abaqus creates an MdbData object when a cae file is opened or a new model is created. There is one MdbData for each model in session. MdbData is updated when it is displayed in a viewport.

## Access

```
import visualization
session.mdbData[name]
```

## Members

The MdbData object has the following members:

- *stepPeriods*

  A tuple of (String, Float) tuples specifying the stepName and the stepPeriod.

- *steps*

  A repository of [MdbDataStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbdatasteppyc.htm?ContextScope=all) objects specifying the list of steps. The repository is read-only.

- *instances*

  A repository of [MdbDataInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbdatainstancepyc.htm?ContextScope=all) objects specifying the list of instances. The repository is read-only.