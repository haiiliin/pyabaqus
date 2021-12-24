# Annotation object

The Annotation object is the abstract base type for other Annotation objects. The Annotation object has no explicit constructor. The methods and members of the Annotation object are common to all objects derived from Annotation.

## Access

```
import annotationToolset
mdb.annotations[name]
session.odbs[name].userData.annotations[name]
session.viewports[name].annotationsToPlot[i]
```

## bringToFront()



This method brings the Annotation object to the top of the annotation stack.



### Arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## sendToBack()



This method sends the Annotation object to the bottom of the annotation stack.



### Arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## bringForward()



This method brings the Annotation object one position up in the annotation stack.



### Arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## sendBackward()



This method sends the Annotation object one position down in the annotation stack.



### Arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## moveBefore(...)



This method moves the Annotation object before another object in the same repository.



### Required arguments

- *name*

  A String specifying the name of the other Annotation object.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## moveAfter(...)



This method moves the Annotation object after another object in the same repository.



### Required arguments

- *name*

  A String specifying the name of the other Annotation object.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## translate(...)



This method translates the Annotation object on the viewport plane.



### Required arguments

None.

### Optional arguments

- *x*

  A Float specifying the *X* translation amount in millimeters.

- *y*

  A Float specifying the *Y* translation amount in millimeters.

### Return value

None.

### Exceptions

None.

![img](https://help.3ds.com/2021/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

## Members

The Annotation object has the following member:

- *name*

  A String specifying the annotation repository key.