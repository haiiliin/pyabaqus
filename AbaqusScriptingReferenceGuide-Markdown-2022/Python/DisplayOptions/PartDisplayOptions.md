# PartDisplayOptions object

The PartDisplayOptions object stores settings that specify how parts are to be displayed in a particular viewport. The PartDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.

## Access

```
session.viewports[name].layers[name].partDisplay
import part
session.viewports[name].partDisplay
```

## setValues(...)



This method modifies the PartDisplayOptions object.



### Required arguments

None.

### Optional arguments

- *renderStyle*

  A SymbolicConstant specifying how the image in the viewport is rendered. Possible values are WIREFRAME, HIDDEN, and SHADED. The default value is WIREFRAME.

- *visibleDisplayGroups*

  A sequence of [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) objects specifying the DisplayGroups visible in the viewport. Currently the sequence can contain a maximum of one [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) object. The default value is an empty sequence.

- *engineeringFeatures*

  A Boolean specifying whether engineering features are shown. The default value is OFF.

- *renderBeamProfiles*

  A Boolean specifying whether to render the beam profiles. The default value is OFF.

- *beamScaleFactor*

  A Float specifying the beam profile scale factor. The beamScaleFactor must be greater than zero. The default value is 1.0.

### Return value

None.

### Exceptions

RangeError.



## Members

The PartDisplayOptions object can have the following members:

- *engineeringFeatures*

  A Boolean specifying whether engineering features are shown. The default value is OFF.

- *renderBeamProfiles*

  A Boolean specifying whether to render the beam profiles. The default value is OFF.

- *beamScaleFactor*

  A Float specifying the beam profile scale factor. The beamScaleFactor must be greater than zero. The default value is 1.0.

- *mesh*

  A Boolean specifying whether the mesh should be displayed.

- *renderStyle*

  A SymbolicConstant specifying how the image in the viewport is rendered. Possible values are WIREFRAME, HIDDEN, and SHADED. The default value is WIREFRAME.

- *displayGroup*

  A [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) object specifying the current display group and referring to an object in the *displayGroups* member of [Session](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sessionpyc.htm?ContextScope=all).

- *displayGroupInstances*

  A repository of [DisplayGroupInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygroupinstancepyc.htm?ContextScope=all) objects.

- *engineeringFeatureOptions*

  An [EngineeringFeatureDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-engineeringfeaturedisplayoptionspyc.htm?ContextScope=all) object.

- *geometryOptions*

  A [GeometryDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometrydisplayoptionspyc.htm?ContextScope=all) object.

- *meshOptions*

  A [MeshDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshdisplayoptionspyc.htm?ContextScope=all) object.