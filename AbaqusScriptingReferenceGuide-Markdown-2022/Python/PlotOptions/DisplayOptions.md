# DisplayOptions object

The DisplayOptions object stores a plot state.

## Access

```
import visualization
session.viewports[name].layers[name].odbDisplay.display
session.viewports[name].odbDisplay.display
```

## setValues(...)



This method modifies the DisplayOptions object.



### Required arguments

None.

### Optional arguments

- *options*

  A DisplayOptions object from which values are to be copied. If other arguments are also supplied to setValues, they will override the values in *options*. The default value is None.

- *plotState*

  A sequence of SymbolicConstants specifying the plot state of the display. Possible values are UNDEFORMED, DEFORMED, CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, SYMBOLS_ON_UNDEF, SYMBOLS_ON_DEF, ORIENT_ON_UNDEF, and ORIENT_ON_DEF. The default value is (UNDEFORMED).

### Return value

None.

### Exceptions

None.



## Members

The DisplayOptions object can have the following member:

- *plotState*

  A tuple of SymbolicConstants specifying the plot state of the display. Possible values are UNDEFORMED, DEFORMED, CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, SYMBOLS_ON_UNDEF, SYMBOLS_ON_DEF, ORIENT_ON_UNDEF, and ORIENT_ON_DEF. The default value is (UNDEFORMED).