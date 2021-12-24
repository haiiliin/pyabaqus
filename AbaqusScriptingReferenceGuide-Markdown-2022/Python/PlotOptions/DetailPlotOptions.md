# DetailPlotOptions object

The DetailPlotOptions object stores values and attributes associated with a [Viewport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewportpyc.htm?ContextScope=all) object. The DetailPlotOptions object has no constructor command. Abaqus creates the *detailPlotOptions* member whenever a [Viewport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewportpyc.htm?ContextScope=all) is created.

## Access

```
session.viewports[name].detailPlotOptions
```

## Members

The DetailPlotOptions object has the following member:

- *plyStackPlotOptions*

  A [PlyStackPlotOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-plystackplotoptionspyc.htm?ContextScope=all) object.