# AssemblyDisplayOptions object

The AssemblyDisplayOptions object stores settings that specify how assemblies are to be displayed in a particular viewport. The AssemblyDisplayOptions object has no constructor. When you create a new viewport, the settings are copied from the current viewport.

## Access

```
import assembly
session.viewports[name].assemblyDisplay
session.viewports[name].layers[name].assemblyDisplay
```

## setValues(...)



This method modifies the AssemblyDisplayOptions object.



### Required arguments

None.

### Optional arguments

- *visibleInstances*

  A sequence of Strings specifying the names of the part instances that are visible in the viewport. The default value is an empty sequence.

- *step*

  A String specifying the step for which objects are to be displayed. Possible values are any valid step name. The default value is "Initial".

- *renderStyle*

  A SymbolicConstant specifying how the image in the viewport is rendered. Possible values are WIREFRAME, HIDDEN, SHADED, and FILLED. The default value is WIREFRAME.

- *mesh*

  A Boolean specifying whether the mesh is shown. The default value is OFF.

- *loads*

  A Boolean specifying whether loads are shown. The default value is OFF.

- *bcs*

  A Boolean specifying whether boundary conditions are shown. The default value is OFF.

- *interactions*

  A Boolean specifying whether interactions are shown. The default value is OFF.

- *constraints*

  A Boolean specifying whether constraints are shown. The default value is OFF.

- *connectors*

  A Boolean specifying whether connectors are shown. The default value is OFF.

- *cnxEndPoints*

  A Boolean specifying whether the connector end points are shown. This member is applicable only if *connectors*=ON. The default value is ON.

- *cnxLocalAxes*

  A Boolean specifying whether the connector local coordinate system axes are shown. This member is applicable only if *connectors*=ON. The default value is ON.

- *cnxTypeLabels*

  A Boolean specifying whether the connector section type labels are shown. This member is applicable only if *connectors*=ON. The default value is ON.

- *cnxTagDisplay*

  A Boolean specifying whether the tag information is displayed along with the connector section type labels. This member is applicable only if *connectors*=ON and if *cnxTypeLabels*=ON. The default value is OFF.

- *predefinedFields*

  A Boolean specifying whether fields and initial conditions are shown. The default value is OFF.

- *visibleDisplayGroups*

  A sequence of [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) objects specifying the DisplayGroups visible in the viewport. Currently the sequence can contain a maximum of one [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) object. The default value is an empty sequence.

- *engineeringFeatures*

  A Boolean specifying whether to display engineering features. The default value is OFF.

- *renderBeamProfiles*

  A Boolean specifying whether to render the beam profiles. The default value is OFF.

- *beamScaleFactor*

  A Float specifying the beam profile scale factor. The beamScaleFactor must be greater than zero. The default value is 1.0.

- *optimizationTasks*

  A Boolean specifying whether optimization tasks are shown. The default value is OFF.

- *geometricRestrictions*

  A Boolean specifying whether geometric restrictions are shown. The default value is OFF.

- *stopConditions*

  A Boolean specifying whether stop conditions are shown. The default value is OFF.

### Return value

None.

### Exceptions

RangeError.



## Members

The AssemblyDisplayOptions object can have the following members:

- *bcs*

  A Boolean specifying whether boundary conditions are shown. The default value is OFF.

- *connectors*

  A Boolean specifying whether connectors are shown. The default value is OFF.

- *cnxEndPoints*

  A Boolean specifying whether the connector end points are shown. This member is applicable only if *connectors*=ON. The default value is ON.

- *cnxLocalAxes*

  A Boolean specifying whether the connector local coordinate system axes are shown. This member is applicable only if *connectors*=ON. The default value is ON.

- *cnxTypeLabels*

  A Boolean specifying whether the connector section type labels are shown. This member is applicable only if *connectors*=ON. The default value is ON.

- *cnxTagDisplay*

  A Boolean specifying whether the tag information is displayed along with the connector section type labels. This member is applicable only if *connectors*=ON and if *cnxTypeLabels*=ON. The default value is OFF.

- *constraints*

  A Boolean specifying whether constraints are shown. The default value is OFF.

- *engineeringFeatures*

  A Boolean specifying whether to display engineering features. The default value is OFF.

- *geometricRestrictions*

  A Boolean specifying whether geometric restrictions are shown. The default value is OFF.

- *renderBeamProfiles*

  A Boolean specifying whether to render the beam profiles. The default value is OFF.

- *beamScaleFactor*

  A Float specifying the beam profile scale factor. The beamScaleFactor must be greater than zero. The default value is 1.0.

- *predefinedFields*

  A Boolean specifying whether fields and initial conditions are shown. The default value is OFF.

- *interactions*

  A Boolean specifying whether interactions are shown. The default value is OFF.

- *loads*

  A Boolean specifying whether loads are shown. The default value is OFF.

- *mesh*

  A Boolean specifying whether the mesh is shown. The default value is OFF.

- *optimizationTasks*

  A Boolean specifying whether optimization tasks are shown. The default value is OFF.

- *stopConditions*

  A Boolean specifying whether stop conditions are shown. The default value is OFF.

- *renderStyle*

  A SymbolicConstant specifying how the image in the viewport is rendered. Possible values are WIREFRAME, HIDDEN, SHADED, and FILLED. The default value is WIREFRAME.

- *bcOptions*

  A [BCDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bcdisplayoptionspyc.htm?ContextScope=all) object.

- *constraintOptions*

  A [ConstraintDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constraintdisplayoptionspyc.htm?ContextScope=all) object.

- *displayGroup*

  A [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) object specifying the current display group and referring to an object in the *displayGroups* member of [Session](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sessionpyc.htm?ContextScope=all).

- *displayGroupInstances*

  A repository of [DisplayGroupInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygroupinstancepyc.htm?ContextScope=all) objects.

- *engineeringFeatureOptions*

  An [EngineeringFeatureDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-engineeringfeaturedisplayoptionspyc.htm?ContextScope=all) object.

- *predefinedFieldOptions*

  A [PredefinedFieldDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-predefinedfielddisplayoptionspyc.htm?ContextScope=all) object.

- *geometricRestrictionOptions*

  A [GeometricRestrictionDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictiondisplayoptionspyc.htm?ContextScope=all) object.

- *geometryOptions*

  A [GeometryDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometrydisplayoptionspyc.htm?ContextScope=all) object.

- *interactionOptions*

  An [InteractionDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactiondisplayoptionspyc.htm?ContextScope=all) object.

- *loadOptions*

  A [LoadDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loaddisplayoptionspyc.htm?ContextScope=all) object.

- *meshOptions*

  A [MeshDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshdisplayoptionspyc.htm?ContextScope=all) object.

- *optimizationTaskOptions*

  An [OptimizationTaskDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationtaskdisplayoptionspyc.htm?ContextScope=all) object.

- *stopConditionOptions*

  A [StopConditionDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stopconditiondisplayoptionspyc.htm?ContextScope=all) object.

- *symbolOptions*

  A [SymbolDisplayOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-symboldisplayoptionspyc.htm?ContextScope=all) object.

- *visibleInstances*

  A tuple of Strings specifying the names of the part instances that are visible in the viewport. The default value is an empty sequence.

- *step*

  A String specifying the step for which objects are to be displayed. Possible values are any valid step name. The default value is "Initial".