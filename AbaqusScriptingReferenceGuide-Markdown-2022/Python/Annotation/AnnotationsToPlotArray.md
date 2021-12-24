# AnnotationsToPlotArray object

The AnnotationsToPlotArray object is a sequence that stores references to plotted annotations. By adding annotations to and removing annotations from this sequence, you can control which annotations are displayed in a particular viewport.

## Access

```
import annotationToolset
session.viewports[name].annotationsToPlot
```

## bringForward(...)



This method brings the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object one position forward in the AnnotationsToPlotArray sequence.



### Required arguments

- *index*

  An Int specifying the index of the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the AnnotationsToPlotArray sequence.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## bringToFront(...)



This method brings the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object to the beginning of the AnnotationsToPlotArray sequence.



### Required arguments

- *index*

  An Int specifying the index of the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the AnnotationsToPlotArray sequence.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## moveAfter(...)



This method moves the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object after another object in the same AnnotationsToPlotArray sequence.



### Required arguments

- *index*

  An Integer specifying the index of the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the AnnotationsToPlotArray sequence.

- *other*

  An Integer specifying the index of the other [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the AnnotationsToPlotArray sequence after which this object will be moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## moveBefore(...)



This method moves the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object before another object in the same AnnotationsToPlotArray sequence.



### Required arguments

- *index*

  An Int specifying the index of the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the AnnotationsToPlotArray sequence.

- *other*

  An Int specifying the index of the other [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the AnnotationsToPlotArray sequence before which this object will be moved.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## sendBackward(...)



This method sends the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object one position backward in the AnnotationsToPlotArray sequence.



### Required arguments

- *index*

  An Int specifying the index of the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the AnnotationsToPlotArray sequence.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## sendToBack(...)



This method sends the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object to the end of the AnnotationsToPlotArray sequence.



### Required arguments

- *index*

  An Int specifying the index of the [Annotation](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) object in the AnnotationsToPlotArray sequence.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The AnnotationsToPlotArray object has no members.