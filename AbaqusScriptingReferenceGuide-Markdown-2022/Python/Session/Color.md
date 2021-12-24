# Color object

The Color object contains the RGB definition of a system color.

## Access

```
session.colors[name]
```

## setByRGB(...)



This method changes the RGB value of a user-defined color. However, users cannot define colors, and this method does not modify system-defined colors.



### Required arguments

- *rgb*

  A sequence of three Floats specifying the RGB value of the color. The Float values must be between 0.0 and 1.0.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Color object has the following members:

- *name*

  A String specifying the name of the color.

- *rgb*

  A tuple of three Floats specifying the RGB value of the color. The Float values must be between 0.0 and 1.0.