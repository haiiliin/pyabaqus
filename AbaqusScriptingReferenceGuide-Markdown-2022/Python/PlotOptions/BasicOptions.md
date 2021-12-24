# BasicOptions object

The BasicOptions object stores values and attributes associated with an OdbDisplay object.

The BasicOptions object has no constructor command. Abaqus creates the *defaultOdbDisplay.basicOptions* member when you import the Visualization module. Abaqus creates a *basicOptions* member when it creates the [OdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdisplaypyc.htm?ContextScope=all) object, using the values from *defaultOdbDisplay.basicOptions*. Abaqus creates the *odbDisplay* member when a viewport is created, using the attributes from the previous active viewport. The previous active viewport contains the attributes from the *defaultOdbDisplay* object for the session. The attributes from the *defaultOdbDisplay* object are copied from the previous active viewport to create the new viewport.

BasicOptions objects are accessed in one of two ways:

- The default basic options: these settings are used as defaults when other *basicOptions* members are created. These settings can be set to customize user preferences.
- The basic options associated with a particular viewport.

## Access

```
import visualization
session.defaultOdbDisplay.basicOptions
session.viewports[name].layers[name].odbDisplay.basicOptions
session.viewports[name].odbDisplay.basicOptions
```

## setValues(...)



This method modifies the BasicOptions object.



### Required arguments

None.

### Optional arguments

- *options*

  A BasicOptions object from which values are to be copied. If other arguments are also supplied to setValues, they will override the values in *options*. The default value is None.

- *cameraCsysName*

  A String specifying the name of the coordinate system driving the moving camera.

- *cameraMovesWithCsys*

  A Boolean specifying whether the camera moves with the coordinate system. The default value is OFF.

- *cameraFollowsRotation*

  A Boolean specifying whether the camera, when it moves, follows the rotation of the coordinate system. The default value is OFF.

- *averagingThreshold*

  A Float specifying the nodal averaging threshold percentage. Possible values are 0 << *averagingThreshold* << 100. The default value is 75.0.

- *quantityToPlot*

  A SymbolicConstant specifying the quantity to plot. Possible values are FIELD_OUTPUT and DISCONTINUITIES. The default value is FIELD_OUTPUT.

- *curveRefinementLevel*

  A SymbolicConstant specifying the refinement level for drawing curves. Possible values are EXTRA_COARSE, COARSE, MEDIUM, FINE, and EXTRA_FINE. The default value is COARSE.

- *noResultsColor*

  A String specifying the color of elements that do not have any results. The default value is "White".

- *featureAngle*

  A Float specifying the feature angle to be used when *visibleEdges*=FEATURE. The default value is 30.0.

- *otherSymbolSize*

  An Int specifying the size of various glyph symbols (boundary conditions, coupling constraints, etc.). The default value is 6.

- *renderBeamProfiles*

  A Boolean specifying whether to render the beam profiles. The default value is OFF.

- *beamScaleFactor*

  A Float specifying the beam profile scale factor. The beamScaleFactor must be greater than zero. The default value is 1.0.

- *renderShellThickness*

  A Boolean specifying whether to render the shell thickness. The default value is OFF.

- *shellScaleFactor*

  A Float specifying the shell thickness scale factor. The shellScaleFactor must be greater than zero. The default value is 1.0.

- *accountForDeactivatedElems*

  A Boolean specifying whether to account for deactivated elements. The default value is ON.

- *bcDisplay*

  A Boolean specifying whether to display boundary conditions. The default value is OFF.

- *connectorDisplay*

  A Boolean specifying whether to display connectors. The default value is OFF.

- *highlightConnectorPts*

  A Boolean specifying whether to highlight connector points. The default value is ON.

- *showConnectorAxes*

  A Boolean specifying whether to display connector orientations or coordinate systems. The default value is ON.

- *showConnectorType*

  A Boolean specifying whether to display the text that describes the connector type. The default value is ON.

- *pointElements*

  A Boolean specifying whether to display point type elements. The default value is ON.

- *referencePoints*

  A Boolean specifying whether to display reference points. *referencePoints* is valid only when *pointElements*=ON. The default value is ON.

- *massElements*

  A Boolean specifying whether to display mass, heat capacity and inertia elements. *massElements* is valid only when *pointElements*=ON. The default value is OFF.

- *springElements*

  A Boolean specifying whether to display spring and dashpot elements. *springElements* is valid only when *pointElements*=ON. The default value is OFF.

- *spotWelds*

  A Boolean specifying whether to display spot weld and distributed coupling elements. *spotWelds* is valid only when *pointElements*=ON. The default value is OFF.

- *tracerParticles*

  A Boolean specifying whether to display tracer particles. *tracerParticles* is valid only when *pointElements*=ON. The default value is OFF.

- *pc3dElements*

  A Boolean specifying whether to display PC3D elements. *pc3dElements* is valid only when *pointElements*=ON. The default value is ON.

- *pd3dElements*

  A Boolean specifying whether to display PD3D elements. *pd3dElements* is valid only when *pointElements*=ON. The default value is ON.

- *sweepArs*

  A Boolean specifying whether to sweep the analytical surfaces. The default value is ON or OFF, depending on the characteristics of your model.

- *sweepElem*

  A Boolean specifying whether to sweep the deformable elements. The default value is ON or OFF, depending on the characteristics of your model.

- *sweepStartAngleArs*

  A Float specifying the starting angle (in degrees) from which to sweep the analytical surfaces when *sweepArs*=ON. The default value is 0.0.

- *sweepStartAngleElem*

  A Float specifying the starting angle (in degrees) from which to sweep the model when *sweepElem*=ON. The default value is 0.0.

- *sweepEndAngleArs*

  A Float specifying the angle (in degrees) through which to sweep the analytical surfaces when *sweepArs*=ON. The default value is 360.0.

- *sweepEndAngleElem*

  A Float specifying the angle (in degrees) through which to sweep the model when *sweepElem*=ON. The default value is 180.0.

- *numSweepSegmentsArs*

  An Int specifying the number of segments to display when *sweepArs*=ON. The default value is 10 or 20, depending on characteristics of your model.

- *numSweepSegmentsElem*

  An Int specifying the number of segments to display when *sweepElem*=ON. The default value is 10 or 20, depending on characteristics of your model.

- *numericForm*

  A SymbolicConstant specifying the numeric form in which to display results that contain complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY, COMPLEX_MAG_AT_ANGLE, COMPLEX_ENVELOPE_MAX_ABS, COMPLEX_ENVELOPE_MAX, and COMPLEX_ENVELOPE_MIN. The default value is REAL.

- *complexAngle*

  A Float specifying the angle (in degrees) at which to display results that contain complex numbers when *numericForm*=COMPLEX_MAG_AT_ANGLE. The default value is 0.0.

- *sectionResults*

  A SymbolicConstant specifying which of the section points to use. Possible values are USE_BOTTOM, USE_TOP, USE_BOTTOM_AND_TOP, and USE_ENVELOPE. The default value is USE_BOTTOM.

- *envelopeCriteria*

  A SymbolicConstant specifying the envelope criterion. Possible values are MAX_VALUE, MIN_VALUE, and MAX_ABS_VALUE. The default value is MAX_ABS_VALUE.

- *envelopeDataPosition*

  A SymbolicConstant specifying the output position for envelope calculations. Possible values are CENTROID, ELEMENT_NODAL, and INTEGRATION_POINT. The default value is INTEGRATION_POINT.

- *plyResultLocation*

  A SymbolicConstant specifying the ply result location. Possible values are BOTTOM, MIDDLE, TOP, and TOP_AND_BOTTOM. The default value is MIDDLE.

- *sectionPointScheme*

  A SymbolicConstant specifying the section point scheme. Possible values are CATEGORY_BASED and PLY_BASED. The default value is CATEGORY_BASED.

- *sweepSectors*

  A Boolean specifying whether to sweep the cyclic symmetry sectors. The default value is OFF.

- *sectorSelectionType*

  A SymbolicConstant specifying how sectors will be selected for sweeping. Possible values are SELECT_BY_NUMBER, SELECT_BY_ANGLE, and SELECT_ALL. The default value is SELECT_BY_NUMBER.

- *selectedSectorNumbers*

  A sequence of Ints specifying which sectors to display when *sectorSelectionType*=SELECT_BY_NUMBER. Possible values are 1 ≤≤ *selectedSectorNumbers* ≤≤ the number of sectors. The default value is (1).

- *sweepSectorStartAngle*

  A Float specifying the angle (in degrees) from which to sweep cyclic symmetry sectors when *sweepSectors*=ON. Possible values are multiples of the sector angle such that 0 ≤≤ *sweepSectorStartAngle* ≤≤ 360. The default value is 0.0.

- *sweepSectorEndAngle*

  A Float specifying the angle (in degrees) through which to sweep cyclic symmetry sectors when *sweepSectors*=ON. Possible values are multiples of the sector angle such that 0 << *sweepSectorEndAngle* ≤≤ 360. The default value is 360.0.

- *extrudeArs*

  A Boolean specifying whether to extrude analytical surfaces. The default value is ON or OFF depending on characteristics of your model.

- *extrudeArsDepthAutoCompute*

  A Boolean specifying whether to use automatic depth determination when extruding analytical surfaces. The default value is ON. The default value is ON.

- *extrudeElem*

  A Boolean specifying whether to extrude deformable elements. The default value is ON or OFF depending on characteristics of your model.

- *extrudeArsDepth*

  A Float specifying the depth (in model units) by which the analytical surfaces are to be extruded when *extrudeArs*=ON. The default value is 1.0.

- *extrudeElemDepth*

  A Float specifying the depth (in model units) by which the deformable elements are to be extruded when *extrudeElem*=ON. The default value is 1.0.

- *mirrorPatternOrder*

  A SymbolicConstant specifying the order of operations to create the mirror pattern. Possible values are MIRROR_RECT_CIRC, RECT_MIRROR_CIRC, MIRROR_CIRC_RECT, RECT_CIRC_MIRROR, CIRC_MIRROR_RECT, and CIRC_RECT_MIRROR. The default value is MIRROR_RECT_CIRC.

- *mirrorCsysName*

  The SymbolicConstant GLOBAL or a String specifying the name of the mirror's coordinate system. The default value is GLOBAL.

- *mirrorAboutXyPlane*

  A Boolean specifying whether to mirror about the XY plane. The default value is OFF.

- *mirrorAboutXzPlane*

  A Boolean specifying whether to mirror about the XZ plane. The default value is OFF.

- *mirrorAboutYzPlane*

  A Boolean specifying whether to mirror about the YZ plane. The default value is OFF.

- *mirrorDisplayBodies*

  A Boolean specifying whether to mirror display bodies. The default value is OFF.

- *patternCsysName*

  The SymbolicConstant GLOBAL or a String specifying the name of the pattern's coordinate system. The default value is GLOBAL.

- *patternNumX*

  An Int specifying the number of patterns to create in the X-direction for a rectangular pattern. The default value is 1.

- *patternNumY*

  An Int specifying the number of patterns to create in the Y-direction for a rectangular pattern. The default value is 1.

- *patternNumZ*

  An Int specifying the number of patterns to create in the Z-direction for a rectangular pattern. The default value is 1.

- *patternOffsetX*

  A Float specifying the offset of the pattern along the X-axis for a rectangular pattern. The default value is 0.0.

- *patternOffsetY*

  A Float specifying the offset of the pattern along the Y-axis for a rectangular pattern. The default value is 0.0.

- *patternOffsetZ*

  A Float specifying the offset of the pattern along the Z-axis for a rectangular pattern. The default value is 0.0.

- *patternRotationAxis*

  A SymbolicConstant specifying the axis of rotation for a circular. Possible values are XAXIS, YAXIS, and ZAXIS. The default value is ZAXIS.

- *patternTotalAngle*

  A Float specifying the total angle of a circular pattern. The default value is 360.0.

- *patternNumCircular*

  An Int specifying the number of patterns to create in a circular pattern. The default value is 1.

- *couplingDisplay*

  A Boolean specifying whether to display coupling constraints. The default value is ON.

- *coordSystemDisplay*

  A Boolean specifying whether to display coordinate systems. The default value is OFF.

- *scratchCoordSystemDisplay*

  A Boolean specifying whether to display coordinate systems that represent user-defined orientations. The default value is OFF.

- *transformationType*

  A SymbolicConstant specifying the transformation to apply to the PrimaryVariable. Possible values are DEFAULT, NODAL, USER_SPECIFIED, ANGULAR, and LAYUP_ORIENTATION. The default value is DEFAULT.If *transformationType*=NODAL, Abaqus will transform nodal vector fields into any orientation defined in the analysis with the [TRANSFORM](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-transform.htm?ContextScope=all#simakey-r-transform) option. Setting *transformationType*=NODAL has no effect on element-based results.If *transformationType*=USER_SPECIFIED, Abaqus will transform tensor and vector fields into the coordinate system specified by *datumCsys*.If *transformationType*=LAYUP_ORIENTATION, Abaqus will transform tensor and vector fields into the layup orientation defined in the composite section. The odb should contain the field SORIENT in order to use this option.

- *datumCsys*

  A [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the coordinate system to use for results transformation when *transformationType*=USER_SPECIFIED.

- *rigidTransformPrimary*

  A Boolean specifying whether to perform a rigid transformation of nodal vector datasets based on the active user specific system The default value is OFF.

- *rigidTransformDeformed*

  A Boolean specifying whether to perform a rigid transformation of current deformedVariable based on the active user specific system The default value is OFF.

- *transformOnDeformed*

  A Boolean specifying whether to include the effects of deformation on the transformation calculations The default value is ON.

- *averageElementOutput*

  A Boolean specifying whether to average the element output. The default value is ON.

- *averageOnlyDisplayed*

  A Boolean specifying whether to average only values on displayed elements. The default value is ON.

- *computeOutput*

  A SymbolicConstant specifying the order or the computations to be performed. Possible values are EXTRAPOLATE_AVERAGE_COMPUTE, EXTRAPOLATE_COMPUTE_AVERAGE, EXTRAPOLATE_COMPUTE, EXTRAPOLATE_COMPUTE_DISCONTINUITIES, and RAW_DATA. The default value is EXTRAPOLATE_AVERAGE_COMPUTE.

- *regionBoundaries*

  A SymbolicConstant specifying the type of averaging region boundaries. Possible values are NONE, ODB_REGIONS, ELEMENT_SET, and DISPLAY_GROUPS. The default value is ODB_REGIONS.

- *useRegionBoundaries*

  A Boolean specifying whether to use region boundaries when averaging. The default value is ON.

- *userRegions*

  A sequence of Strings specifying either element set or display group names (depending on the value of regionBoundaries) defining the averaging region boundaries. The default value is an empty sequence.

- *includeFeatureBoundaries*

  A Boolean specifying whether to include additional averaging boundaries for shells and membranes based on feature edges. The default value is ON.

### Return value

None.

### Exceptions

- If *featureAngle* is not in the valid range:

  RangeError: featureAngle must be a float in the range 0-90, inclusive



## Members

The BasicOptions object can have the following members:

- *regionAveraging*

  A Boolean specifying whether to ignore region boundaries when computing values. The default value is ON.

- *cameraMovesWithCsys*

  A Boolean specifying whether the camera moves with the coordinate system. The default value is OFF.

- *cameraFollowsRotation*

  A Boolean specifying whether the camera, when it moves, follows the rotation of the coordinate system. The default value is OFF.

- *averagingThreshold*

  A Float specifying the nodal averaging threshold percentage. Possible values are 0 << *averagingThreshold* << 100. The default value is 75.0.

- *quantityToPlot*

  A SymbolicConstant specifying the quantity to plot. Possible values are FIELD_OUTPUT and DISCONTINUITIES. The default value is FIELD_OUTPUT.

- *extrapAlgorithm*

  A SymbolicConstant specifying the extrapolation algorithm. This member is for internal use only. The only possible value is EXTRAP_COMPUTE_AVERAGE.

- *curveRefinementLevel*

  A SymbolicConstant specifying the refinement level for drawing curves. Possible values are EXTRA_COARSE, COARSE, MEDIUM, FINE, and EXTRA_FINE. The default value is COARSE.

- *featureAngle*

  A Float specifying the feature angle to be used when *visibleEdges*=FEATURE. The default value is 30.0.

- *otherSymbolSize*

  An Int specifying the size of various glyph symbols (boundary conditions, coupling constraints, etc.). The default value is 6.

- *renderBeamProfiles*

  A Boolean specifying whether to render the beam profiles. The default value is OFF.

- *beamScaleFactor*

  A Float specifying the beam profile scale factor. The beamScaleFactor must be greater than zero. The default value is 1.0.

- *renderShellThickness*

  A Boolean specifying whether to render the shell thickness. The default value is OFF.

- *shellScaleFactor*

  A Float specifying the shell thickness scale factor. The shellScaleFactor must be greater than zero. The default value is 1.0.

- *accountForDeactivatedElems*

  A Boolean specifying whether to account for deactivated elements. The default value is ON.

- *bcDisplay*

  A Boolean specifying whether to display boundary conditions. The default value is OFF.

- *connectorDisplay*

  A Boolean specifying whether to display connectors. The default value is OFF.

- *highlightConnectorPts*

  A Boolean specifying whether to highlight connector points. The default value is ON.

- *showConnectorAxes*

  A Boolean specifying whether to display connector orientations or coordinate systems. The default value is ON.

- *showConnectorType*

  A Boolean specifying whether to display the text that describes the connector type. The default value is ON.

- *pointElements*

  A Boolean specifying whether to display point type elements. The default value is ON.

- *referencePoints*

  A Boolean specifying whether to display reference points. *referencePoints* is valid only when *pointElements*=ON. The default value is ON.

- *massElements*

  A Boolean specifying whether to display mass, heat capacity and inertia elements. *massElements* is valid only when *pointElements*=ON. The default value is OFF.

- *springElements*

  A Boolean specifying whether to display spring and dashpot elements. *springElements* is valid only when *pointElements*=ON. The default value is OFF.

- *spotWelds*

  A Boolean specifying whether to display spot weld and distributed coupling elements. *spotWelds* is valid only when *pointElements*=ON. The default value is OFF.

- *tracerParticles*

  A Boolean specifying whether to display tracer particles. *tracerParticles* is valid only when *pointElements*=ON. The default value is OFF.

- *pc3dElements*

  A Boolean specifying whether to display PC3D elements. *pc3dElements* is valid only when *pointElements*=ON. The default value is ON.

- *pd3dElements*

  A Boolean specifying whether to display PD3D elements. *pd3dElements* is valid only when *pointElements*=ON. The default value is ON.

- *sweepArs*

  A Boolean specifying whether to sweep the analytical surfaces. The default value is ON or OFF, depending on the characteristics of your model.

- *sweepElem*

  A Boolean specifying whether to sweep the deformable elements. The default value is ON or OFF, depending on the characteristics of your model.

- *sweepStartAngleArs*

  A Float specifying the starting angle (in degrees) from which to sweep the analytical surfaces when *sweepArs*=ON. The default value is 0.0.

- *sweepStartAngleElem*

  A Float specifying the starting angle (in degrees) from which to sweep the model when *sweepElem*=ON. The default value is 0.0.

- *sweepEndAngleArs*

  A Float specifying the angle (in degrees) through which to sweep the analytical surfaces when *sweepArs*=ON. The default value is 360.0.

- *sweepEndAngleElem*

  A Float specifying the angle (in degrees) through which to sweep the model when *sweepElem*=ON. The default value is 180.0.

- *numSweepSegmentsArs*

  An Int specifying the number of segments to display when *sweepArs*=ON. The default value is 10 or 20, depending on characteristics of your model.

- *numSweepSegmentsElem*

  An Int specifying the number of segments to display when *sweepElem*=ON. The default value is 10 or 20, depending on characteristics of your model.

- *numericForm*

  A SymbolicConstant specifying the numeric form in which to display results that contain complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY, COMPLEX_MAG_AT_ANGLE, COMPLEX_ENVELOPE_MAX_ABS, COMPLEX_ENVELOPE_MAX, and COMPLEX_ENVELOPE_MIN. The default value is REAL.

- *complexAngle*

  A Float specifying the angle (in degrees) at which to display results that contain complex numbers when *numericForm*=COMPLEX_MAG_AT_ANGLE. The default value is 0.0.

- *sectionResults*

  A SymbolicConstant specifying which of the section points to use. Possible values are USE_BOTTOM, USE_TOP, USE_BOTTOM_AND_TOP, and USE_ENVELOPE. The default value is USE_BOTTOM.

- *envelopeCriteria*

  A SymbolicConstant specifying the envelope criterion. Possible values are MAX_VALUE, MIN_VALUE, and MAX_ABS_VALUE. The default value is MAX_ABS_VALUE.

- *envelopeDataPosition*

  A SymbolicConstant specifying the output position for envelope calculations. Possible values are CENTROID, ELEMENT_NODAL, and INTEGRATION_POINT. The default value is INTEGRATION_POINT.

- *plyResultLocation*

  A SymbolicConstant specifying the ply result location. Possible values are BOTTOM, MIDDLE, TOP, and TOP_AND_BOTTOM. The default value is MIDDLE.

- *sectionPointScheme*

  A SymbolicConstant specifying the section point scheme. Possible values are CATEGORY_BASED and PLY_BASED. The default value is CATEGORY_BASED.

- *sweepSectors*

  A Boolean specifying whether to sweep the cyclic symmetry sectors. The default value is OFF.

- *sectorSelectionType*

  A SymbolicConstant specifying how sectors will be selected for sweeping. Possible values are SELECT_BY_NUMBER, SELECT_BY_ANGLE, and SELECT_ALL. The default value is SELECT_BY_NUMBER.

- *sweepSectorStartAngle*

  A Float specifying the angle (in degrees) from which to sweep cyclic symmetry sectors when *sweepSectors*=ON. Possible values are multiples of the sector angle such that 0 ≤≤ *sweepSectorStartAngle* ≤≤ 360. The default value is 0.0.

- *sweepSectorEndAngle*

  A Float specifying the angle (in degrees) through which to sweep cyclic symmetry sectors when *sweepSectors*=ON. Possible values are multiples of the sector angle such that 0 << *sweepSectorEndAngle* ≤≤ 360. The default value is 360.0.

- *extrudeArs*

  A Boolean specifying whether to extrude analytical surfaces. The default value is ON or OFF depending on characteristics of your model.

- *extrudeArsDepthAutoCompute*

  A Boolean specifying whether to use automatic depth determination when extruding analytical surfaces. The default value is ON. The default value is ON.

- *extrudeElem*

  A Boolean specifying whether to extrude deformable elements. The default value is ON or OFF depending on characteristics of your model.

- *extrudeArsDepth*

  A Float specifying the depth (in model units) by which the analytical surfaces are to be extruded when *extrudeArs*=ON. The default value is 1.0.

- *extrudeElemDepth*

  A Float specifying the depth (in model units) by which the deformable elements are to be extruded when *extrudeElem*=ON. The default value is 1.0.

- *mirrorPatternOrder*

  A SymbolicConstant specifying the order of operations to create the mirror pattern. Possible values are MIRROR_RECT_CIRC, RECT_MIRROR_CIRC, MIRROR_CIRC_RECT, RECT_CIRC_MIRROR, CIRC_MIRROR_RECT, and CIRC_RECT_MIRROR. The default value is MIRROR_RECT_CIRC.

- *mirrorAboutXyPlane*

  A Boolean specifying whether to mirror about the XY plane. The default value is OFF.

- *mirrorAboutXzPlane*

  A Boolean specifying whether to mirror about the XZ plane. The default value is OFF.

- *mirrorAboutYzPlane*

  A Boolean specifying whether to mirror about the YZ plane. The default value is OFF.

- *mirrorDisplayBodies*

  A Boolean specifying whether to mirror display bodies. The default value is OFF.

- *patternNumX*

  An Int specifying the number of patterns to create in the X-direction for a rectangular pattern. The default value is 1.

- *patternNumY*

  An Int specifying the number of patterns to create in the Y-direction for a rectangular pattern. The default value is 1.

- *patternNumZ*

  An Int specifying the number of patterns to create in the Z-direction for a rectangular pattern. The default value is 1.

- *patternOffsetX*

  A Float specifying the offset of the pattern along the X-axis for a rectangular pattern. The default value is 0.0.

- *patternOffsetY*

  A Float specifying the offset of the pattern along the Y-axis for a rectangular pattern. The default value is 0.0.

- *patternOffsetZ*

  A Float specifying the offset of the pattern along the Z-axis for a rectangular pattern. The default value is 0.0.

- *patternRotationAxis*

  A SymbolicConstant specifying the axis of rotation for a circular. Possible values are XAXIS, YAXIS, and ZAXIS. The default value is ZAXIS.

- *patternTotalAngle*

  A Float specifying the total angle of a circular pattern. The default value is 360.0.

- *patternNumCircular*

  An Int specifying the number of patterns to create in a circular pattern. The default value is 1.

- *couplingDisplay*

  A Boolean specifying whether to display coupling constraints. The default value is ON.

- *coordSystemDisplay*

  A Boolean specifying whether to display coordinate systems. The default value is OFF.

- *scratchCoordSystemDisplay*

  A Boolean specifying whether to display coordinate systems that represent user-defined orientations. The default value is OFF.

- *transformationType*

  A SymbolicConstant specifying the transformation to apply to the PrimaryVariable. Possible values are DEFAULT, NODAL, USER_SPECIFIED, ANGULAR, and LAYUP_ORIENTATION. The default value is DEFAULT.If *transformationType*=NODAL, Abaqus will transform nodal vector fields into any orientation defined in the analysis with the [TRANSFORM](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-transform.htm?ContextScope=all#simakey-r-transform) option. Setting *transformationType*=NODAL has no effect on element-based results.If *transformationType*=USER_SPECIFIED, Abaqus will transform tensor and vector fields into the coordinate system specified by *datumCsys*.If *transformationType*=LAYUP_ORIENTATION, Abaqus will transform tensor and vector fields into the layup orientation defined in the composite section. The odb should contain the field SORIENT in order to use this option.

- *rigidTransformPrimary*

  A Boolean specifying whether to perform a rigid transformation of nodal vector datasets based on the active user specific system The default value is OFF.

- *rigidTransformDeformed*

  A Boolean specifying whether to perform a rigid transformation of current deformedVariable based on the active user specific system The default value is OFF.

- *transformOnDeformed*

  A Boolean specifying whether to include the effects of deformation on the transformation calculations The default value is ON.

- *modelCanExtrude*

  A Boolean specifying whether the model contains any elements or surfaces that can be extruded.

- *sweepModelType*

  An Int specifying the types of sweepable elements and surfaces contained in the model, if any.

- *averageElementOutput*

  A Boolean specifying whether to average the element output. The default value is ON.

- *averageOnlyDisplayed*

  A Boolean specifying whether to average only values on displayed elements. The default value is ON.

- *regionBoundaries*

  A SymbolicConstant specifying the type of averaging region boundaries. Possible values are NONE, ODB_REGIONS, ELEMENT_SET, and DISPLAY_GROUPS. The default value is ODB_REGIONS.

- *useRegionBoundaries*

  A Boolean specifying whether to use region boundaries when averaging. The default value is ON.

- *includeFeatureBoundaries*

  A Boolean specifying whether to include additional averaging boundaries for shells and membranes based on feature edges. The default value is ON.

- *numSectors*

  An Int specifying the number of sectors of a cyclic symmetric model. The value is automatically computed from the cyclic symmetric model. This value is read-only.

- *sectorAngle*

  A Float specifying the sector angle of a cyclic symmetric model. The value is automatically computed from the cyclic symmetric model. This value is read-only.

- *automaticExtrudeDepth*

  A Float specifying the automatic extrude depth used to extrude analytical rigid surfaces in the default setting. This value is read-only.

- *cameraCsysName*

  A String specifying the name of the coordinate system driving the moving camera.

- *noResultsColor*

  A String specifying the color of elements that do not have any results. The default value is "White".

- *mirrorCsysName*

  The SymbolicConstant GLOBAL or a String specifying the name of the mirror's coordinate system. The default value is GLOBAL.

- *patternCsysName*

  The SymbolicConstant GLOBAL or a String specifying the name of the pattern's coordinate system. The default value is GLOBAL.

- *datumCsys*

  A [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object specifying the coordinate system to use for results transformation when *transformationType*=USER_SPECIFIED.

- *selectedSectorNumbers*

  A tuple of Ints specifying which sectors to display when *sectorSelectionType*=SELECT_BY_NUMBER. Possible values are 1 ≤≤ *selectedSectorNumbers* ≤≤ the number of sectors. The default value is (1).

- *userRegions*

  A tuple of Strings specifying either element set or display group names (depending on the value of regionBoundaries) defining the averaging region boundaries. The default value is an empty sequence.