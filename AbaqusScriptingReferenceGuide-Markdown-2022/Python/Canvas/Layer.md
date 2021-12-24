# Layer object

Objects can be superimposed by displaying them in different layers of a viewport.

## Access

```
session.viewports[name].layers[name]
```

## Layer(...)



This method creates a Layer object in the Layer repository.



### Path

```
session.viewports[name].Layer
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *copyViewName*

  A String specifying the name of the layer to copy.

### Return value

A Layer object.

### Exceptions

None.



## moveBefore(...)



This method moves the layer object before another object in the layer repository.



### Required arguments

- *name*

  A String specifying the name of the other Layer object.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## moveAfter(...)



This method moves the layer object after another object in the layer repository.



### Required arguments

- *name*

  A String specifying the name of the other Layer object.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Layer object has members with the same names and descriptions as the arguments to the [Layer](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-layerpyc.htm?ContextScope=all#simaker-layerlayerpyc) method.

In addition, the Layer object can have the following members:

- *displayedObject*

  A Displayable object specifying the object to be displayed. The Displayable type is an abstract generalization. The concrete possible types are [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all), [Assembly](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?ContextScope=all), [ConstrainedSketch](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all), [Odb](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?ContextScope=all), or [XYPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all).

- *view*

  A [View](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewpyc.htm?ContextScope=all) object specifying the object that controls viewing of the layer.

- *odbDisplay*

  An [OdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdisplaypyc.htm?ContextScope=all) object specifying the display options for the [Odb](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?ContextScope=all) object.

- *partDisplay*

  A [PartDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partdisplayoptionspyc.htm?ContextScope=all) object specifying the display options for the [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object.

- *assemblyDisplay*

  An [AssemblyDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblydisplayoptionspyc.htm?ContextScope=all) object specifying the display options for the [Assembly](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?ContextScope=all) object.