# Viewport object

The following commands operate on Viewport objects. For more information about the Viewport object, see [Viewport object](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewportpyc.htm?ContextScope=all).

## Access

```
import annotationToolset
```

## plotAnnotation(...)



This method plots an [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in aViewport.



### Required arguments

- *annotation*

  An [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object to plot.

### Optional arguments

- *index*

  An Int specifying the index of the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the sequence of annotations to plot. The default value is zero.

### Return value

None.

### Exceptions

None.