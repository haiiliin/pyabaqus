# Feature object

The following commands operate on Feature objects. For more information about the Feature object, see [Feature object](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all).

## Access

```
import part
```

## AutoRepair()



This method carries out a sequence of geometry repair operations if it contains invalid entities. It is expected to improve the geometry, but it does not guarantee that the number of invalid entities will decrease. In some cases, it can also increase the number of invalid entities. Since a number of geometry repair operations and validity checks are performed, it could be a slow operation depending on the complexity of the geometry.



### Path

mdb.models[*name*].parts[*name*].AutoRepair

### Arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## AddCells(...)



This method tries to convert a shell entity to a solid entity. The conversion is not always successful.



### Path

mdb.models[*name*].parts[*name*].AddCells

### Required arguments

- *faceList*

  A sequence of Face objects specifying the faces bounding the cell to add.

### Optional arguments

- *flipped*

  A Boolean specifying the direction of feature creation. The possible values are True and False. The default is True indicating that the direction is opposite to the face normal. When multiple faces are selected, Abaqus attempts to create cells on both sides of the selected faces and ignores the *flipped* argument.

### Return value

A Feature object.

### Exceptions

None.



## AnalyticRigidSurf2DPlanar(...)



This method creates a first Feature object for an analytical rigid surface by creating a planar wire from the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

mdb.models[*name*].parts[*name*].AnalyticRigidSurf2DPlanar

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar wire.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## AnalyticRigidSurfExtrude(...)



This method creates a first Feature object for an analytical rigid surface by extruding the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given depth, creating a surface.



### Path

mdb.models[*name*].parts[*name*].AnalyticRigidSurfExtrude

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar wire.

### Optional arguments

- *depth*

  A Float specifying the extrusion depth. The default value is 1.0.

### Return value

A Feature object.

### Exceptions

None.



## AnalyticRigidSurfRevolve(...)



This method creates a first Feature object for an analytical rigid surface by revolving the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by 360° about the *Y*-axis.



### Path

mdb.models[*name*].parts[*name*].AnalyticRigidSurfRevolve

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the surface to be revolved.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## AssignMidsurfaceRegion(...)



This method assign a mid-surface property to sequence of [Cell](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) objects. If a reference representation of the part does not exist, it creates one. It also copies the *cells* to the reference representation and deletes the *cells* from the active representation of the part.



### Path

mdb.models[*name*].parts[*name*].AssignMidsurfaceRegion

### Required arguments

- *cellList*

  A sequence of [Cell](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) objects specifying the regions that will be used for mid-surface construction. These regions will be copied to the reference representation of the part.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## BaseSolidExtrude(...)



This method creates a first Feature object by extruding the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given depth, creating a solid. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile.



### Path

mdb.models[*name*].parts[*name*].BaseSolidExtrude

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the plane shape to be extruded.

- *depth*

  A Float specifying the extrusion depth. Possible values are 10–5 ≤≤ *depth* ≤≤ 105.

### Optional arguments

- *draftAngle*

  A Float specifying the draft angle in degrees. Possible values are -90.0 ≤≤ *draftAngle* ≤≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and an inner loop will draft inward. The opposite is true for a negative draft angle. The default value, 0, implies a normal extrude. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction by the sketch when the sketch has completed one full revolution about the twist axis. Pitch can be specified as positive or negative to achieve right-handed or left-handed twist about the twist axis, respectively. The default value, 0, implies a normal extrude. Possible values are –105 ≤≤ *pitch* ≤≤ 105. The arguments *draftAngle* and *pitch* are mutually exclusive.

### Return value

A Feature object.

### Exceptions

RangeError.



## BaseSolidRevolve(...)



This method creates a first Feature object by revolving the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given angle, creating a solid. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile and an axis of revolution. The axis is defined by a single construction line.



### Path

mdb.models[*name*].parts[*name*].BaseSolidRevolve

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the shape to be revolved.

- *angle*

  A Float specifying the revolve angle in degrees. Possible values are 10–4 ≤≤ *angle* ≤≤ 360.Note:If *pitch* >>0, there is no upper limit for *angle*.

### Optional arguments

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction, measured between corresponding points on the sketch when it has completed one full revolution about the axis of revolution. Possible values are 0 ≤≤ *pitch* ≤≤ 105. The default value, 0, implies a normal revolve.

- *flipRevolveDirection*

  A Boolean specifying whether to override the direction of feature creation. If *flipRevolveDirection*=OFF, the default direction of revolution is used. If *flipRevolveDirection*=ON, the revolve direction is reversed. The default value is OFF.

- *flipPitchDirection*

  A Boolean specifying whether to override the direction of translation. If *flipPitchDirection*=OFF, the direction of translation is given by the direction of the revolve axis. If *flipPitchDirection*=ON, the translation direction is reversed. The default value is OFF.

- *moveSketchNormalToPath*

  A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the *pitch* option. If *moveSketchNormalToPath*=OFF, the sketch plane remains parallel to the revolve axis. If *moveSketchNormalToPath*=ON, the sketch is moved to match the angle created by the *pitch* before being revolved. The default value is OFF.

### Return value

A Feature object.

### Exceptions

RangeError.



## BaseSolidSweep(...)



This method creates a first Feature object by sweeping the given profile [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object along the path defined by the path [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object, creating a solid. The profile [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile. The origin of the profile sketch is positioned at the start of the sweep path and swept perpendicular to the path. No checks are made for self-intersection.



### Path

mdb.models[*name*].parts[*name*].BaseSolidSweep

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the profile to be swept.

- *path*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the path of the sweep.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## BaseShell(...)



This method creates a first Feature object by creating a planar shell from the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile.



### Path

mdb.models[*name*].parts[*name*].BaseShell

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar shell.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## BaseShellExtrude(...)



This method creates a first Feature object by extruding the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given depth, creating a shell. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object can define either an open or closed profile.



### Path

mdb.models[*name*].parts[*name*].BaseShellExtrude

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the shape to be extruded.

- *depth*

  A Float specifying the extrusion depth. Possible values are Floats > 0.

### Optional arguments

- *draftAngle*

  A Float specifying the draft angle in degrees. Possible values are -90.0 ≤≤ *draftAngle* ≤≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and an inner loop will draft inward. The opposite is true for a negative draft angle. The default value, 0, implies a normal extrude. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction by the sketch when the sketch has completed one full revolution about the twist axis. Pitch can be specified as positive or negative to achieve right-handed or left-handed twist about the twist axis, respectively. The default value, 0, implies a normal extrude. Possible values are –105 ≤≤ *pitch* ≤≤ 105. The arguments *draftAngle* and *pitch* are mutually exclusive.

### Return value

A Feature object.

### Exceptions

RangeError.



## BaseShellRevolve(...)



This method creates a first Feature object by revolving the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given angle, creating a shell. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object can define either an open or closed profile and an axis of revolution. The axis is defined by a single construction line.



### Path

mdb.models[*name*].parts[*name*].BaseShellRevolve

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the shape to be revolved.

- *angle*

  A Float specifying the revolve angle in degrees. Possible values are 0 ≤≤ *angle* ≤≤ 360.Note:If *pitch* >> 0, there is no upper limit for *angle*.

### Optional arguments

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction, measured between corresponding points on the sketch when it has completed one full revolution about the axis of revolution. Possible values are 0 ≤≤ *pitch* ≤≤ 105. The default value, 0, implies a normal revolve.

- *flipRevolveDirection*

  A Boolean specifying whether to override the direction of feature creation. If *flipRevolveDirection*=OFF, the default direction of revolution is used. If *flipRevolveDirection*=ON, the revolve direction is reversed. The default value is OFF.

- *flipPitchDirection*

  A Boolean specifying whether to override the direction of translation. If *flipPitchDirection*=OFF, the direction of translation is given by the direction of the revolve axis. If *flipPitchDirection*=ON, the translation direction is reversed. The default value is OFF.

- *moveSketchNormalToPath*

  A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the *pitch* option. If *moveSketchNormalToPath*=OFF, the sketch plane remains parallel to the revolve axis. If *moveSketchNormalToPath*=ON, the sketch is moved to match the angle created by the *pitch* before being revolved. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## BaseShellSweep(...)



This method creates a first Feature object by sweeping the given section [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object along the path defined by the path [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object, creating a shell. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object can define either an open or closed profile. The origin of the profile sketch is positioned at the start of the sweep path and swept perpendicular to the path. No checks are made for self-intersection.



### Path

mdb.models[*name*].parts[*name*].BaseShellSweep

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the section to be swept.

- *path*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the path of the sweep.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## BaseWire(...)



This method creates a first Feature object by creating a planar wire from the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

mdb.models[*name*].parts[*name*].BaseWire

### Required arguments

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar wire.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## BlendFaces(...)



This method creates a Feature object by creating new faces that blends two sets of faces.



### Path

mdb.models[*name*].parts[*name*].BlendFaces

### Required arguments

- *side1*

  A sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying one side of the blend. The edges must form a continuous chain without branches.

- *side2*

  A sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) or [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects specifying the second side of the blend. If *side2* contains Edge objects then they must form a continuous chain without branches.

### Optional arguments

- *method*

  A SymbolicConstant indicating a method for creating blends. This argument is a required argument if *side2* contains [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object and it is ignored if *side2* contains [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all)objects. It can have one of the following values:TANGENT: The blend is tangent to the sides.SHORTEST_PATH: The blend connects the two sides based on linear interpolation between the two sides.SPECIFY_PATH: The blend connects the two sides along a specified path.

- *path*

  An Edge object that connects *side1* to *side2* and specifies the path for creating the blend. This argument is required if *method*=SPECIFY_PATH; otherwise, it is ignored.

### Return value

A Feature object.

### Exceptions

None.



## Chamfer(...)



This method creates an additional Feature object by chamfering the given list of edges with a given length.



### Path

mdb.models[*name*].parts[*name*].Chamfer

### Required arguments

- *length*

  A Float specifying the length of the chamfer.

- *edgeList*

  A sequence of Edge objects specifying the edges to chamfer.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## Mirror(...)



This method mirrors existing part geometry across a plane to create new geometry.



### Path

mdb.models[*name*].parts[*name*].Mirror

### Required arguments

- *mirrorPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *keepOriginal*

  A boolean specifying whether or not the original part geometry should be retained.

### Optional arguments

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## ConvertToAnalytical()



This method attempts to change entities into a simpler form that will speed up processing and make entities available during feature operations.



### Path

mdb.models[*name*].parts[*name*].ConvertToAnalytical

### Arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## ConvertToPrecise(...)



This method attempts to change imprecise entities so that the geometry becomes precise.



### Path

mdb.models[*name*].parts[*name*].ConvertToPrecise

### Required arguments

None.

### Optional arguments

- *method*

  A SymbolicConstant specifying the method to be used to convert the part to precise. Possible values are RECOMPUTE_GEOMETRY and TIGHTEN_GAPS. The default value is RECOMPUTE_GEOMETRY.

### Return value

A Feature object.

### Exceptions

None.



## CoverEdges(...)



This method generates a face using the given edges as the face's boundaries. The CoverEdges method generates a face by creating the geometry consisting of the underlying surface, associated edges, and vertices.



### Path

mdb.models[*name*].parts[*name*].CoverEdges

### Required arguments

- *edgeList*

  A sequence of Edge objects specifying the edges that bound the new face.

### Optional arguments

- *tryAnalytical*

  A Boolean specifying whether the newly created face should be analytical or not. The default is False.

### Return value

A Feature object.

### Exceptions

- If the given boundary is not a closed loop:

  Parterror: Cannot find a closed loop

- If the given boundary contains a zero length component:

  Parterror: Cannot find a closed loop

- If the underlying surface is too difficult to fit:

  Parterror: Cannot construct face geometry



## Cut(...)



This method creates an additional Feature object by cutting a hole using the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.



### Path

mdb.models[*name*].parts[*name*].Cut

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar cut.

### Optional arguments

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM.

### Return value

A Feature object.

### Exceptions

None.



## CutExtrude(...)



This method creates an additional Feature object by extruding the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given depth and cutting away material in the solid and shell regions of the part. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile. The CutExtrude method creates a blind cut (using *depth*), an up-to-face cut (using *upToFace*), or a through-all cut (if *depth* and *upToFace* are not specified).



### Path

mdb.models[*name*].parts[*name*].CutExtrude

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar sketch to be extruded.

### Optional arguments

- *depth*

  A Float specifying the extrusion depth. If *depth* is specified, the cut will be a blind cut. The default is to not specify a depth.

- *upToFace*

  A Face specifying the face up to which to cut. If *upToFace* is specified, the cut will be an up-to-face cut. The default is to not specify a face.Note:If neither *depth* nor *upToFace* is specified, the cut will be a through-all cut.

- *draftAngle*

  A Float specifying the draft angle in degrees. Possible values are -90.0 ≤≤ *draftAngle* ≤≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and an inner loop will draft inward. The opposite is true for a negative draft angle. The default value, 0, implies a normal extrude. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction by the sketch when the sketch has completed one full revolution about the twist axis. Pitch can be specified as positive or negative to achieve right-handed or left-handed twist about the twist axis, respectively. The default value, 0, implies a normal extrude. Possible values are –105 ≤≤ *pitch* ≤≤ 105. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *flipExtrudeDirection*

  A Boolean specifying whether to override the direction of feature creation. If the value is OFF, it means use the direction defined by the *sketchPlaneSide*; if the value is ON, it means use the opposite direction to the one defined by *sketchPlaneSide*. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## CutLoft(...)



This method creates an additional Feature object by lofting between the given sections and cutting away material from the part. You define the sections using a sequence of edges from the part or an [EdgeArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all).



### Path

mdb.models[*name*].parts[*name*].CutLoft

### Required arguments

- *loftsections*

  A sequence of sequences of edges specifying the cross-sections to be lofted. Each outer sequence specifies a section through which the method will pass the loft feature. Each outer sequence can be defined as a sequence of edges or as an [EdgeArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all). The edges specifying a section must form a simple closed profile and must not contain multiple loops.

### Optional arguments

- *startCondition*

  A SymbolicConstant specifying the tangent direction at the start section of the loft feature. Possible values are NONE, NORMAL, RADIAL, and SPECIFIED. You can specify this argument only if the start and end sections are planar. You cannot use this argument in conjunction with the *path* argument. You must use the *startCondition* argument in conjunction with the *endCondition* argument.

- *endCondition*

  A SymbolicConstant specifying the tangent direction at the end section of the loft feature. Possible values are NONE, NORMAL, RADIAL, and SPECIFIED. You can specify this argument only if the start and end sections are planar. You cannot use this argument in conjunction with the *path* argument. You must use the *endCondition* argument in conjunction with the *startCondition* argument.

- *startTangent*

  A Float specifying the angle in degrees of the tangent with respect to the plane in which the start section lies. You must specify the *startTangent* argument if *startCondition*=SPECIFIED. Possible values are 0.0 ≤≤ *startTangent* ≤≤ 180.0.

- *startMagnitude*

  A Float specifying the magnitude of the *startTangent*. You must specify the *startMagnitude* argument if *startCondition*=SPECIFIED. Possible values are 0.0 << *startMagnitude* << 100.0.

- *endTangent*

  A Float specifying the angle in degrees of the tangent with respect to the plane in which the end section lies. You must specify the *endTangent* argument if *startCondition*=SPECIFIED. Possible values are 0.0 ≤≤ *endTangent* ≤≤ 180.0.

- *endMagnitude*

  A Float specifying the magnitude of the *endTangent*. This argument is to be used when the *endCondition* argument has the value SPECIFIED. Possible values are 0.0 << *endMagnitude* << 100.0.

- *globalSmoothing*

  A Boolean specifying whether each path defined in the *paths* argument is applied locally or globally.If the path is applied locally, its effect is felt only on faces created from the edges on the *loftSections* through which the *paths* pass through.If the path is applied globally, an averaging algorithm is applied over all the paths defined and is distributed over all the faces created.The default value is ON (globally).

### Return value

A Feature object.

### Exceptions

None.



## CutRevolve(...)



This method creates an additional Feature object by revolving the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given angle and cutting away material from the part. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile and an axis of revolution.



### Path

mdb.models[*name*].parts[*name*].CutRevolve

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar sketch to be revolved.

- *angle*

  A Float specifying the angle in degrees to be revolved.

### Optional arguments

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction, measured between corresponding points on the sketch when it has completed one full revolution about the axis of revolution. Possible values are 0 ≤≤ *pitch* ≤≤ 105. The default value, 0, implies a normal revolve.

- *flipRevolveDirection*

  A Boolean specifying whether to override the direction of feature creation. If *flipRevolveDirection*=OFF, the default direction of revolution is used. If *flipRevolveDirection*=ON, the revolve direction is reversed. The default value is OFF.

- *flipPitchDirection*

  A Boolean specifying whether to override the direction of translation. If *flipPitchDirection*=OFF, the direction of translation is given by the direction of the revolve axis. If *flipPitchDirection*=ON, the translation direction is reversed. The default value is OFF.

- *moveSketchNormalToPath*

  A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the *pitch* option. If *moveSketchNormalToPath*=OFF, the sketch plane remains parallel to the revolve axis. If *moveSketchNormalToPath*=ON, the sketch is moved to match the angle created by the *pitch* before being revolved. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## CutSweep(...)



This method creates an additional Feature object by sweeping the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object along a path which may be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) or a sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects and cutting away material from the part. If the profile section is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object, it must define a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all). No checks are made for self-intersection.



### Path

mdb.models[*name*].parts[*name*].CutSweep

### Required arguments

- *path*

  Path may either be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object or a sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the path of the sweep.

- *profile*

  Profile may either be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object or a [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the section to be swept.

### Optional arguments

- *pathPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *pathUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the path sketch. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *pathOrientation*

  A SymbolicConstant specifying the orientation of *pathUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the plane on which to sketch the profile. Not required when profile is a [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object. When profile is chosen as a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object, user may or may not give this as input. If user does not give this as input, the normal plane at the start of the path will be the sketchPlane.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the profile sketch. Only required when profile is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when profile is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *draftAngle*

  A Float specifying the draft angle in degrees. Possible values are -90.0 ≤≤ *draftAngle* ≤≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and an inner loop will draft inward. The opposite is true for a negative draft angle. The default value, 0, implies a normal extrude. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction by the sketch when the sketch has completed one full revolution about the twist axis. Pitch can be specified as positive or negative to achieve right-handed or left-handed twist about the twist axis, respectively. The default value, 0, implies a normal extrude. Possible values are –105 ≤≤ *pitch* ≤≤ 105. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *profileNormal*

  A Boolean specifying whether to keep the profile normal same as original or varying through out the sweep path. When *profileNormal*=OFF, the profile normal will vary through out the sweep path. When *profileNormal*=ON, the profile normal will be same as original through out the sweep path. The default value is OFF.

- *flipSweepDirection*

  A Boolean specifying whether to flip the direction in which sweep operation will be performed. When *flipSweepDirection*=OFF, sweep operation will be performed in the direction of path direction. When *flipSweepDirection*=ON, sweep operation will be performed in the direction opposite to the path direction. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## ExtendFaces(...)



This method extends faces along its free edges by offsetting the external edges along the surfaces. One of *distance*, *upToReferenceRep*, or *upToFaces* must be used to specify how far the faces need to be extended.



### Path

mdb.models[*name*].parts[*name*].ExtendFaces

### Required arguments

None.

### Optional arguments

- *faces*

  A sequence of Face objects specifying the faces to be extended. The faces cannot belong to the reference representation. The *faces* and *extendAlong* arguments are mutually exclusive. One of them must be specified.

- *extendAlong*

  A sequence of Edge objects specifying the edges where to extend the faces. Only free edges are considered. The interior edges will be ignored. The *faces* and *extendAlong* arguments are mutually exclusive. One of them must be specified.

- *distance*

  A Float indicating the distance to extend the faces along the edges. Either *distance*, *upToReferenceRep*, or *upToFaces* must be specified.

- *upToFaces*

  A sequence of Face objects specifying the faces that the selected faces should be extended up to.

- *trimToExtendedTargetSurfaces*

  A Boolean indicating that the surfaces of up to target faces should be extended before extending and trimming the selected faces. The default value is True.

- *upToReferenceRep*

  A Boolean indicating that the selected faces should be extended along the selected edges and be trimmed along their intersection with the reference representation.

### Return value

A Feature object.

### Exceptions

None.



## FaceFromElementFaces(...)



This method creates a geometry face from a collection of orphan element faces.



### Path

mdb.models[*name*].parts[*name*].FaceFromElementFaces

### Required arguments

- *elementFaces*

  A Region object specifying the collection of orphan element faces.

### Optional arguments

- *stitch*

  A Boolean specifying whether the created geometry face should be stitched with existing geometry faces. Default value is TRUE.

- *stitchTolerance*

  A Float indicating the maximum gap to be stitched. The value should be smaller than the minimum feature size and bigger than the maximum gap expected to be stitched in the model. Otherwise this command may remove small (sliver) edges that are smaller than the tolerance. If stitch tolerance is not provided then default value of 0.001 will be used for stitching.

- *analyticFitTolerance*

  A Float indicating the analytical surface fitting tolerance. If analytical tolerance is not provided then default value of 0.015 will be used for analytical surface fitting.

- *associateFace*

  A Boolean specifying whether the created geometry face should be associated with the mesh. Default value is TRUE.

### Return value

A Feature object.

### Exceptions

None.



## HoleBlindFromEdges(...)



This method creates an additional Feature object by creating a circular blind hole of the given diameter and depth and cutting away material in the solid and shell regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.



### Path

mdb.models[*name*].parts[*name*].HoleBlindFromEdges

### Required arguments

- *plane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *planeSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *diameter*

  A Float specifying the diameter of the hole.

- *edge1*

  An Edge object specifying the edge from which *distance1* is measured.

- *distance1*

  A Float specifying the offset from *edge1*.

- *edge2*

  An Edge object specifying the edge from which *distance2* is measured.

- *distance2*

  A Float specifying the offset from *edge2*.

- *depth*

  A Float specifying the depth of the hole.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## HoleFromEdges(...)



This method creates an additional Feature object by creating a circular hole of the given diameter in a 2D planar part and cutting away material in the shell and wire regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.



### Path

mdb.models[*name*].parts[*name*].HoleFromEdges

### Required arguments

- *diameter*

  A Float specifying the diameter of the hole.

- *edge1*

  An Edge object specifying the edge from which *distance1* is measured.

- *distance1*

  A Float specifying the offset from *edge1*.

- *edge2*

  An Edge object specifying the edge from which *distance2* is measured.

- *distance2*

  A Float specifying the offset from *edge2*.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## HoleThruAllFromEdges(...)



This method creates an additional Feature object by creating a circular through hole of the given diameter and cutting away material in the solid and shell regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.



### Path

mdb.models[*name*].parts[*name*].HoleThruAllFromEdges

### Required arguments

- *plane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *planeSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *diameter*

  A Float specifying the diameter of the hole.

- *edge1*

  An Edge object specifying the edge from which *distance1* is measured.

- *distance1*

  A Float specifying the offset from *edge1*.

- *edge2*

  An Edge object specifying the edge from which *distance2* is measured.

- *distance2*

  A Float specifying the offset from *edge2*.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## MergeEdges(...)



This method merges edges either by extending the user selection or using only the selected edges.



### Path

mdb.models[*name*].parts[*name*].MergeEdges

### Required arguments

None.

### Optional arguments

- *edgeList*

  A sequence of Edge objects specifying the edges to be merged.

- *extendSelection*

  A Boolean specifying whether the user selection needs to be extended to include edges till branching occurs. Branching is said to occur when the vertex of an edge is shared by more than two edges.

### Return value

A Feature object.

### Exceptions

None.



## OffsetFaces(...)



This method creates new faces by offsetting existing faces.



### Path

mdb.models[*name*].parts[*name*].OffsetFaces

### Required arguments

- *faceList*

  A sequence of Face objects specifying the faces that will be offset. The faces may belong to the part or to the reference representation associated with the part.

### Optional arguments

- *distance*

  A Float indicating the distance to offset the faces. Either *distance* or *targetFaces* must be specified.

- *targetFaces*

  A sequence of Face objects whose distance to the faces argument together with the *targetFacesMethod* determines the distance to offset the faces. Either *distance* or *targetFaces* must be specified.

- *targetFacesMethod*

  A SymbolicConstant indicating how to calculate the distance to offset. It can have one of the following values:HALF_OF_AVERAGE: Offset the faces by a distance equals to half the average distance to target faces.CLOSEST_POINT_FRACTION: Offset the faces by a distance equals to the fraction of the distance to the approximate closest point on the selected target faces.FARTHEST_POINT_FRACTION: Offset the faces by a distance equals to the fraction of the distance to the approximate farthest point on the selected target faces.

- *fractionDistance*

  A Float indicating the fraction of the distance to the closest or the farthest point on the target faces. Its default value is 0.5.

- *trimToReferenceRep*

  A Boolean indicating whether to extend the offset faces and trim them along their intersection with the reference representation.

### Return value

A Feature object.

### Exceptions

None.



## RemoveCells(...)



This method converts a solid entity to a shell entity.



### Path

mdb.models[*name*].parts[*name*].RemoveCells

### Required arguments

- *cellList*

  A sequence of Cell objects specifying the cells to remove.

### Optional arguments

None.

### Return value

A Boolean value.

### Exceptions

- If the intended volume to be turned into a shell entity is not three-dimensional.

  Parterror: Geometry that is not 3-dimensional does not contain cells.



## RemoveFaces(...)



This method removes faces from a solid entity or from a shell entity.



### Path

mdb.models[*name*].parts[*name*].RemoveFaces

### Required arguments

- *faceList*

  A sequence of Face objects specifying the faces to remove.

### Optional arguments

- *deleteCells*

  A Boolean specifying whether all cells are to be deleted when the faces are removed. The default value is False.

### Return value

A Feature object.

### Exceptions

None.



## RemoveFacesAndStitch(...)



This method removes faces from a solid entity and attempts to close the resulting gap by extending the neighboring faces of the solid.



### Path

mdb.models[*name*].parts[*name*].RemoveFacesAndStitch

### Required arguments

- *faceList*

  A sequence of Face objects specifying the faces to remove.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## RemoveRedundantEntities(...)



This method removes redundant edges and vertices from a solid or a shell entity. One of the two arguments is required.



### Path

mdb.models[*name*].parts[*name*].RemoveRedundantEntities

### Required arguments

None.

### Optional arguments

- *vertexList*

  A sequence of Vertex objects specifying the vertices to be removed.

- *edgeList*

  A sequence of Edge objects specifying the edges to be removed.

- *removeEdgeVertices*

  A Boolean specifying whether the vertices of the redundant edges need to be removed. The default is True.

### Return value

A Feature object.

### Exceptions

- If the selected entity is not a redundant entity.

  Parterror: None of the selected entities are redundant.



## RepairFaceNormals(...)



This method works on the entire part or a sequence of shell faces. When the entire part is selected, it aligns all the shell face normals, and inverts all of the solid faces' normals if the solid was originally inside out. When a few shell faces are selected, it inverts the normals of the selected faces.



### Path

mdb.models[*name*].parts[*name*].RepairFaceNormals

### Required arguments

None.

### Optional arguments

- *faceList*

  A sequence of Face objects.

### Return value

A Feature object.

### Exceptions

None.



## RepairInvalidEdges(...)



This method repairs invalid edges. It will always attempt to improve edges even if none of selected edges are initially invalid and may leave behind invalid edges that could not be repaired.



### Path

mdb.models[*name*].parts[*name*].RepairInvalidEdges

### Required arguments

- *edgeList*

  A sequence of Edge objects.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## RepairSliver(...)



This method repairs the selected sliver from the selected face. The sliver area is specified using two points. A face partition is carried out at the specified points and the smaller of the two faces is removed.



### Path

mdb.models[*name*].parts[*name*].RepairSliver

### Required arguments

- *face*

  A Face object specifying the face on which the sliver is located.

- *point1*

  A point specifying the location for partition creation. It can be a Vertex object, an Interesting Point or three coordinates specifying the point on an edge of the *face*.

- *point2*

  A point specifying the location for partition creation. It can be a Vertex object, an Interesting Point or three coordinates specifying the point on an edge of the *face*.

### Optional arguments

- *toleranceChecks*

  A Boolean specifying whether to use internal tolerance checks to restrict the size of the sliver face being removed. The default is True.

### Return value

A Feature object.

### Exceptions

None.



## RepairSmallEdges(...)



This method repairs small edges. This method will attempt to replace selected small edges with vertices and extend the adjacent faces and edges. This method might leave behind some small edges that cannot be removed.



### Path

mdb.models[*name*].parts[*name*].RepairSmallEdges

### Required arguments

- *edgeList*

  A sequence of Edge objects.

### Optional arguments

- *toleranceChecks*

  A Boolean specifying whether to use internal tolerance checks to restrict the size of the edges being removed. The default is True.

### Return value

A Feature object.

### Exceptions

None.



## RepairSmallFaces(...)



This method repairs small faces. It will attempt to replace the selected small faces with edges or vertices and extend the adjacent faces. This method might leave behind some small faces that cannot be removed.



### Path

mdb.models[*name*].parts[*name*].RepairSmallFaces

### Required arguments

- *faceList*

  A sequence of Face objects.

### Optional arguments

- *toleranceChecks*

  A Boolean specifying whether to use internal tolerance checks to restrict the size of the faces being removed. The default is True.

### Return value

A Feature object.

### Exceptions

None.



## ReplaceFaces(...)



This method replaces the selected faces with a single face. If one single face is selected, that alone is replaced with a new face.



### Path

mdb.models[*name*].parts[*name*].ReplaceFaces

### Required arguments

- *faceList*

  A sequence of Face objects to be replaced.

### Optional arguments

- *stitch*

  A Boolean specifying whether the newly created face needs to be stitched to the existing geometry. The default is True.

### Return value

A Feature object.

### Exceptions

None.



## Round(...)



This method creates an additional Feature object by rounding (filleting) the given list of entities with the given radius.



### Path

mdb.models[*name*].parts[*name*].Round

### Required arguments

- *radius*

  A Float specifying the radius of the fillets.

- *edgeList*

  A sequence of Edge objects. Solid and Shell edges of a part can be rounded. The operation will fail for non-manifold edges. The *edgeList* and *vertexList* arguments are mutually exclusive. One of them must be specified.

- *vertexList*

  A sequence of Vertex objects. Vertices that are connected to two wire edges can be rounded. The operation will fail for a vertex connected to a face. The *edgeList* and *vertexList* arguments are mutually exclusive. One of them must be specified.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.



## Shell(...)



This method creates an additional Feature object by creating a planar shell from the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile.



### Path

mdb.models[*name*].parts[*name*].Shell

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar shell.

### Optional arguments

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

### Return value

A Feature object.

### Exceptions

None.



## ShellExtrude(...)



This method creates an additional Feature object by extruding the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given depth, creating a shell protrusion. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object can define either an open or closed profile.



### Path

mdb.models[*name*].parts[*name*].ShellExtrude

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar sketch to be extruded.

### Optional arguments

- *depth*

  A Float specifying the extrusion depth. The default is to not specify a depth. Either *depth* or *upToFace* must be used to define the extrusion depth.

- *upToFace*

  A Face specifying the face up to which to extrude. If *upToFace* is specified, the extrusion will be an up-to-face extrusion. The default is to not specify a face. Either *depth* or *upToFace* must be used to define the extrusion depth.

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

- *draftAngle*

  A Float specifying the draft angle in degrees. Possible values are -90.0 ≤≤ *draftAngle* ≤≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and an inner loop will draft inward. The opposite is true for a negative draft angle. The default value, 0, implies a normal extrude. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction by the sketch when the sketch has completed one full revolution about the twist axis. Pitch can be specified as positive or negative to achieve right-handed or left-handed twist about the twist axis, respectively. The default value, 0, implies a normal extrude. Possible values are –105 ≤≤ *pitch* ≤≤ 105. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *flipExtrudeDirection*

  A Boolean specifying whether to override the direction of feature creation. If the value is OFF, it means use the direction defined by the *sketchPlaneSide*; if the value is ON, it means use the opposite direction to the one defined by *sketchPlaneSide*. The default value is OFF.

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## ShellLoft(...)



This method creates an additional Feature object by lofting between the given sections and adding shell faces to the part. You define the sections using a sequence of edges from the part or an [EdgeArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all).



### Path

mdb.models[*name*].parts[*name*].ShellLoft

### Required arguments

- *loftsections*

  A sequence of sequences of edges specifying the cross-sections to be lofted. Each outer sequence specifies a section through which the method will pass the loft feature. Each outer sequence can be defined as a sequence of edges or as an [EdgeArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all). The edges specifying a section must form a simple closed profile and must not contain multiple loops.

### Optional arguments

- *startCondition*

  A SymbolicConstant specifying the tangent direction at the start section of the loft feature. Possible values are NONE, NORMAL, RADIAL and SPECIFIED. You can specify this argument only if the start and end sections are planar. You cannot use this argument in conjunction with the *path* argument. You must use the *startCondition* argument in conjunction with the *endCondition* argument.

- *endCondition*

  A SymbolicConstant specifying the tangent direction at the end section of the loft feature. Possible values are NONE, NORMAL, RADIAL and SPECIFIED. You can specify this argument only if the start and end sections are planar. You cannot use this argument in conjunction with the *path* argument. You must use the *endCondition* argument in conjunction with the *startCondition* argument.

- *startTangent*

  A Float specifying the angle in degrees of the tangent with respect to the plane in which the start section lies. You must specify the *startTangent* argument if *startCondition*=SPECIFIED. Possible values are 0.0 ≤≤ *startTangent* ≤≤ 180.0.

- *startMagnitude*

  A Float specifying the magnitude of the *startTangent*. You must specify the *startMagnitude* argument if *startCondition*=SPECIFIED. Possible values are 0.0 << *startMagnitude* << 100.0.

- *endTangent*

  A Float specifying the angle in degrees of the tangent with respect to the plane in which the end section lies. You must specify the *endTangent* argument if *startCondition*=SPECIFIED. Possible values are 0.0 ≤≤ *endTangent* ≤≤ 180.0.

- *endMagnitude*

  A Float specifying the magnitude of the *endTangent*. This argument is to be used when the *endCondition* argument has the value SPECIFIED. Possible values are 0.0 << *endMagnitude* << 100.0.

- *paths*

  A sequence of sequences of edges that pass through each section in the loft feature. Each sequence specifies a path followed by the face or an edge created by a loft feature. Each path must start at the first section, end at the last section, and pass through each section. In addition, the order of the sequences must be the same as the order of the sections in the *loftsections* argument. Each path must not self-intersect and must be tangent continuous. In addition, the paths must not intersect each other. You cannot use the *paths* argument in conjunction with the *startCondition* and *endCondition* arguments.

- *globalSmoothing*

  A Boolean specifying whether each path defined in the *paths* argument is applied locally or globally.If the path is applied locally, its effect is felt only on faces created from the edges on the *loftsections* through which the *paths* pass through.If the path is applied globally, an averaging algorithm is applied over all the paths defined and is distributed over all the faces created.The default value is ON (globally).

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## ShellRevolve(...)



This method creates an additional Feature object by revolving the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given angle, creating a shell protrusion. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object can define either an open or closed profile and an axis of revolution. The axis is defined by a single construction line. For a description of the plane positioning arguments, see SolidExtrude.



### Path

mdb.models[*name*].parts[*name*].ShellRevolve

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar sketch to be revolved.

- *angle*

  A Float specifying the angle in degrees to be revolved.

### Optional arguments

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction, measured between corresponding points on the sketch when it has completed one full revolution about the axis of revolution. Possible values are 0 ≤≤ *pitch* ≤≤ 105. The default value, 0, implies a normal revolve.

- *flipRevolveDirection*

  A Boolean specifying whether to override the direction of feature creation. If *flipRevolveDirection*=OFF, the default direction of revolution is used. If *flipRevolveDirection*=ON, the revolve direction is reversed. The default value is OFF.

- *flipPitchDirection*

  A Boolean specifying whether to override the direction of translation. If *flipPitchDirection*=OFF, the direction of translation is given by the direction of the revolve axis. If *flipPitchDirection*=ON, the translation direction is reversed. The default value is OFF.

- *moveSketchNormalToPath*

  A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the *pitch* option. If *moveSketchNormalToPath*=OFF, the sketch plane remains parallel to the revolve axis. If *moveSketchNormalToPath*=ON, the sketch is moved to match the angle created by the *pitch* before being revolved. The default value is OFF.

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## ShellSweep(...)



This method creates an additional Feature object by sweeping the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object or a sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects along a path which may be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) or a sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects, creating a shell swept protrusion. The section can be an open or a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all). No checks are made for self-intersection.



### Path

mdb.models[*name*].parts[*name*].ShellSweep

### Required arguments

- *path*

  Path may either be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object or a sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the path of the sweep.

- *profile*

  Profile may either be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object or a sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the section to be swept.

### Optional arguments

- *pathPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *pathUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the path sketch. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *pathOrientation*

  A SymbolicConstant specifying the orientation of *pathUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the plane on which to sketch the profile. Not required when profile is a [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object. When profile is chosen as [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object, user may or may not give this as input. If user does not give this as input, the normal plane at the start of the path will be the sketchPlane.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the profile sketch. Only required when profile is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when profile is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *draftAngle*

  A Float specifying the draft angle in degrees. Possible values are -90.0 ≤≤ *draftAngle* ≤≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and an inner loop will draft inward. The opposite is true for a negative draft angle. The default value, 0, implies a normal extrude. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction by the sketch when the sketch has completed one full revolution about the twist axis. Pitch can be specified as positive or negative to achieve right-handed or left-handed twist about the twist axis, respectively. The default value, 0, implies a normal extrude. Possible values are –105 ≤≤ *pitch* ≤≤ 105. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *profileNormal*

  A Boolean specifying whether to keep the profile normal same as original or varying through out the sweep path. When *profileNormal*=OFF, the profile normal will vary through out the sweep path. When *profileNormal*=ON, the profile normal will be same as original through out the sweep path. The default value is OFF.

- *flipSweepDirection*

  A Boolean specifying whether to flip the direction in which sweep operation will be performed. When *flipSweepDirection*=OFF, sweep operation will be performed in the direction of path direction. When *flipSweepDirection*=ON, sweep operation will be performed in the direction opposite to the path direction. The default value is OFF.

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## SolidExtrude(...)



This method creates an additional Feature object by extruding the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given depth, creating a solid protrusion. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile.



### Path

mdb.models[*name*].parts[*name*].SolidExtrude

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar sketch to be extruded.

### Optional arguments

- *depth*

  A Float specifying the extrusion depth. The default is to not specify a depth. Either *depth* or *upToFace* must be used to define the extrusion depth.

- *upToFace*

  A Face specifying the face up to which to extrude. If *upToFace* is specified, the extrusion will be an up-to-face extrusion. The default is to not specify a face. Either *depth* or *upToFace* must be used to define the extrusion depth.

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

- *draftAngle*

  A Float specifying the draft angle in degrees. Possible values are -90.0 ≤≤ *draftAngle* ≤≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and an inner loop will draft inward. The opposite is true for a negative draft angle. The default value, 0, implies a normal extrude. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction by the sketch when the sketch has completed one full revolution about the twist axis. Pitch can be specified as positive or negative to achieve right-handed or left-handed twist about the twist axis, respectively. The default value, 0, implies a normal extrude. Possible values are –105 ≤≤ *pitch* ≤≤ 105. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *flipExtrudeDirection*

  A Boolean specifying whether to override the direction of feature creation. If the value is OFF, it means use the direction defined by the *sketchPlaneSide*; if the value is ON, it means use the opposite direction to the one defined by *sketchPlaneSide*. The default value is OFF.

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## SolidLoft(...)



This method creates an additional Feature object by lofting between the given sections and adding material to the part. You define the sections using a sequence of edges from the part or an [EdgeArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all).



### Path

mdb.models[*name*].parts[*name*].SolidLoft

### Required arguments

- *loftsections*

  A sequence of sequences of edges specifying the cross-sections to be lofted. Each outer sequence specifies a section through which Abaqus will pass the loft feature. Each outer sequence can be defined as a sequence of edges or as an [EdgeArray](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all). The edges specifying a section must form a simple closed profile and must not contain multiple loops.

### Optional arguments

- *startCondition*

  A SymbolicConstant specifying the tangent direction at the start section of the loft feature. Possible values are NONE, NORMAL, RADIAL and SPECIFIED. You can specify this argument only if the start and end sections are planar. You cannot use this argument in conjunction with the *path* argument. You must use the *startCondition* argument in conjunction with the *endCondition* argument.

- *endCondition*

  A SymbolicConstant specifying the tangent direction at the end section of the loft feature. Possible values are NONE, NORMAL, RADIAL and SPECIFIED. You can specify this argument only if the start and end sections are planar. You cannot use this argument in conjunction with the *path* argument. You must use the *endCondition* argument in conjunction with the *startCondition* argument.

- *startTangent*

  A Float specifying the angle in degrees of the tangent with respect to the plane in which the start section lies. You must specify the *startTangent* argument if *startCondition*=SPECIFIED. Possible values are 0.0 ≤≤ *startTangent* ≤≤ 180.0.

- *startMagnitude*

  A Float specifying the magnitude of the *startTangent*. You must specify the *startMagnitude* argument if *startCondition*=SPECIFIED. Possible values are 0.0 << *startMagnitude* << 100.0.

- *endTangent*

  A Float specifying the angle in degrees of the tangent with respect to the plane in which the end section lies. You must specify the *endTangent* argument if *startCondition*=SPECIFIED. Possible values are 0.0 ≤≤ *endTangent* ≤≤ 180.0.

- *endMagnitude*

  A Float specifying the magnitude of the *endTangent*. This argument is to be used when the *endCondition* argument has the value SPECIFIED. Possible values are 0.0 << *endMagnitude* << 100.0.

- *paths*

  A sequence of sequences of edges that pass through each section in the loft feature. Each sequence specifies a path followed by the face or an edge created by a loft feature. Each path must start at the first section, end at the last section, and pass through each section. In addition, the order of the sequences must be the same as the order of the sections in the *loftsections* argument. Each path must not self-intersect and must be tangent continuous. In addition, the paths must not intersect each other. You cannot use the *paths* argument in conjunction with the *startCondition* and *endCondition* arguments.

- *globalSmoothing*

  A Boolean specifying whether each path defined in the *paths* argument is applied locally or globally.If the path is applied locally, its effect is felt only on faces created from the edges on the *loftsections* through which the *paths* pass through.If the path is applied globally, an averaging algorithm is applied over all the paths defined and is distributed over all the faces created.The default value is ON (globally).

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## SolidRevolve(...)



This method creates an additional Feature object by revolving the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object by the given angle, creating a solid protrusion. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile and an axis of revolution. The axis is defined by a single construction line.



### Path

mdb.models[*name*].parts[*name*].SolidRevolve

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar sketch to be revolved.

- *angle*

  A Float specifying the angle in degrees to be revolved.

### Optional arguments

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction, measured between corresponding points on the sketch when it has completed one full revolution about the axis of revolution. Possible values are 0 ≤≤ *pitch* ≤≤ 105. The default value, 0, implies a normal revolve.

- *flipRevolveDirection*

  A Boolean specifying whether to override the direction of feature creation. If *flipRevolveDirection*=OFF, the default direction of revolution is used. If *flipRevolveDirection*=ON, the revolve direction is reversed. The default value is OFF.

- *flipPitchDirection*

  A Boolean specifying whether to override the direction of translation. If *flipPitchDirection*=OFF, the direction of translation is given by the direction of the revolve axis. If *flipPitchDirection*=ON, the translation direction is reversed. The default value is OFF.

- *moveSketchNormalToPath*

  A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the *pitch* option. If *moveSketchNormalToPath*=OFF, the sketch plane remains parallel to the revolve axis. If *moveSketchNormalToPath*=ON, the sketch is moved to match the angle created by the *pitch* before being revolved. The default value is OFF.

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## SolidSweep(...)



This method creates an additional Feature object by sweeping the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object or a [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object along a path which may be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) or a sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects, creating a solid swept protrusion. If the profile section is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object, it must define a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all). No checks are made for self-intersection.



### Path

mdb.models[*name*].parts[*name*].SolidSweep

### Required arguments

- *path*

  Path may either be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object or a sequence of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the path of the sweep.

- *profile*

  Profile may either be a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object or a [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the section to be swept.

### Optional arguments

- *pathPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *pathUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the path sketch. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *pathOrientation*

  A SymbolicConstant specifying the orientation of *pathUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when path is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the plane on which to sketch the profile. Not required when profile is a [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object. When profile is chosen as [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object, user may or may not give this as input. If user does not give this as input, the normal plane at the start of the path will be the sketchPlane.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the profile sketch. Only required when profile is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when profile is a [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object.

- *draftAngle*

  A Float specifying the draft angle in degrees. Possible values are -90.0 ≤≤ *draftAngle* ≤≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and an inner loop will draft inward. The opposite is true for a negative draft angle. The default value, 0, implies a normal extrude. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *pitch*

  A Float specifying the pitch. The pitch is the distance traveled along the axial direction by the sketch when the sketch has completed one full revolution about the twist axis. Pitch can be specified as positive or negative to achieve right-handed or left-handed twist about the twist axis, respectively. The default value, 0, implies a normal extrude. Possible values are –105 ≤≤ *pitch* ≤≤ 105. The arguments *draftAngle* and *pitch* are mutually exclusive.

- *profileNormal*

  A Boolean specifying whether to keep the profile normal same as original or varying through out the sweep path. When *profileNormal*=OFF, the profile normal will vary through out the sweep path. When *profileNormal*=ON, the profile normal will be same as original through out the sweep path. The default value is OFF.

- *flipSweepDirection*

  A Boolean specifying whether to flip the direction in which sweep operation will be performed. When *flipSweepDirection*=OFF, sweep operation will be performed in the direction of path direction. When *flipSweepDirection*=ON, sweep operation will be performed in the direction opposite to the path direction. The default value is OFF.

- *keepInternalBoundaries*

  A Boolean specifying whether internal boundaries will be retained. The default value is OFF.

### Return value

A Feature object.

### Exceptions

None.



## Stitch(...)



This method attempts to create a valid part by binding together free and imprecise edges of all the faces of a part. If *edgeList* is not given, a global stitch will be performed. If *stitchTolerance* is not specified, a value of 1.0 will be used.



### Path

mdb.models[*name*].parts[*name*].Stitch

### Required arguments

None.

### Optional arguments

- *edgeList*

  A sequence of Edge objects specifying the edges that need to be stitched.

- *stitchTolerance*

  A Float indicating the maximum gap to be stitched. The value should be smaller than the minimum feature size and bigger than the maximum gap expected to be stitched in the model. Otherwise this command may remove small (sliver) edges that are smaller than the tolerance.

### Return value

A Feature object.

### Exceptions

None.



## Wire(...)



This method creates an additional Feature object by creating a planar wire from the given [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object. The [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object must define a closed profile.



### Path

mdb.models[*name*].parts[*name*].Wire

### Required arguments

- *sketchPlane*

  A [Datum](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) plane object or a planar [Face](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the plane on which to sketch.

- *sketchPlaneSide*

  A SymbolicConstant specifying the direction of feature creation. Possible values are SIDE1 and SIDE2.

- *sketchUpEdge*

  An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the sketch.

- *sketch*

  A [ConstrainedSketch](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object specifying the planar sketch to be revolved.

### Optional arguments

- *sketchOrientation*

  A SymbolicConstant specifying the orientation of *sketchUpEdge* on the sketch. Possible values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

### Return value

A Feature object.

### Exceptions

None.



## WireSpline(...)



This method creates an additional Feature object by creating a spline wire that passes through a sequence of given points. Each point can be a datum point, a vertex, an interesting point, or a tuple.



### Path

mdb.models[*name*].parts[*name*].WireSpline

### Required arguments

- *points*

  A sequence of Vertex, Datum point, or InterestingPoint objects specifying the points through which the spline wire will pass. *points* can also be a sequence of tuples of Floats. You must specify at least two values in the sequence.

### Optional arguments

- *mergeType*

  A SymbolicConstant specifying the merge behavior of the wire with existing geometry. If *mergeType* is MERGE, Abaqus merges the wire into solid regions of the part if the wire passes through them. If *mergeType* is IMPRINT, Abaqus imprints the spline wire on existing geometry as edges. If *mergeType* is SEPARATE, Abaqus neither merges nor imprints the spline wire with existing geometry. It creates the wire separately. The default value is IMPRINT.

- *smoothClosedSpline*

  A Boolean specifying the behavior of Abaqus when the points defining a spline wire form a closed loop (the start and end points are the same). If *smoothClosedSpline*=ON, Abaqus creates a smooth spline wire where the tangencies at the end point meet smoothly. If *smoothClosedSpline*=OFF, Abaqus does not automatically create a smooth end condition. The default value in OFF.

### Return value

A Feature object.

### Exceptions

None.



## WirePolyLine(...)



This method creates an additional Feature object by creating a polyline wire that passes through a sequence of given points. Each point can be a datum point, a vertex, an interesting point, or a tuple.



### Path

mdb.models[*name*].parts[*name*].WirePolyLine

### Required arguments

- *points*

  A sequence of Vertex, Datum point, or InterestingPoint objects specifying the points through which the polyline wire will pass. *points* can also be a sequence of tuples of Floats. You must specify at least two values in the sequence.

### Optional arguments

- *mergeType*

  A SymbolicConstant specifying the merge behavior of the wire with existing geometry. If *mergeType* is MERGE, Abaqus merges the wire into solid regions of the part if the wire passes through them. If *mergeType* is IMPRINT, Abaqus imprints the wire on existing geometry as edges. If *mergeType* is SEPARATE, Abaqus neither merges nor imprints the spline wire with existing geometry. It creates the wire separately. The default value is IMPRINT.

- *meshable*

  A Boolean specifying whether the wire should be available for selection in meshing operations. If *meshable*=OFF, the wire can be used for connector section assignment. The default value is ON.

### Return value

A Feature object.

### Exceptions

None.



## WireFromEdge(...)



This method creates an additional Feature object by creating a Wire by selecting one or more [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects of a Solid or Shell part.



### Path

mdb.models[*name*].parts[*name*].WireFromEdge

### Required arguments

- *edgeList*

  A list of [Edge](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects specifying the edges from which the wire is to be created.

### Optional arguments

None.

### Return value

A Feature object.

### Exceptions

None.