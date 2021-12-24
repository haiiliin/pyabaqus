# ConstrainedSketchImageOptions object

The ConstrainedSketchImageOptions object is used to store values and attributes associated with the background image for a particular sketch. The ConstrainedSketchImageOptions object has no constructor.

## Access

```
import sketch
mdb.models[name].sketches[name].imageOptions
```

## setValues(...)



This method modifies the [ConstrainedSketchOptions](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchoptionspyc.htm?ContextScope=all) object.



### Required arguments

None.

### Optional arguments

- *imageName*

  A String specifying the name of the image. A list of valid image names is in the *images* repository in the *session* object.

- *showImage*

  A Boolean specifying whether an image should be displayed in the sketcher background. The default value is OFF.

- *origin*

  A pair of Floats specifying the *X*- and *Y*-offsets in millimeters from the lower-left corner of the viewport. The default value is (0, 0).

- *xScale*

  A Float specifying the scale applied to the image width. The default value is 1.0.When *xScale* is negative, the image is mirrored about its y-axis but its position is not affected.

- *yScale*

  A Float specifying the scale applied to the image height. The default value is 1.0.When *yScale* is negative, the image is mirrored about its x-axis but its position is not affected.

- *translucency*

  A Float specifying the translucency factor to use when displaying the image. Possible values are 0.0 ≤≤ *translucency* ≤≤ 1.0 with 0.0 being invisible and 1.0 being opaque. The default value is 1.0.

### Return value

None.

### Exceptions

RangeError.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The ConstrainedSketchImageOptions object has members with the same names and descriptions as the arguments to the [setValues ](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchimageoptionspyc.htm?ContextScope=all#simaker-constrainedsketchimageoptionssetvaluespyc)method.