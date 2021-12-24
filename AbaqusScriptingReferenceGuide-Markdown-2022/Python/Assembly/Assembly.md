# Assembly object

An Assembly object is a container for instances of parts. The Assembly object has no constructor command. Abaqus creates the *rootAssembly* member when a [Model](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?ContextScope=all) object is created.

## Access

```
import assembly
mdb.models[name].rootAssembly
```

## backup()



This method makes a backup copy of the features in the assembly. The backup() method is used in conjunction with the restore() method.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## clearGeometryCache()



This method deletes the geometry cache. Deleting the geometry cache reduces the amount of memory being used.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## deleteAllFeatures()



This method deletes all the features in the assembly.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## deleteFeatures(...)



This method deletes specified features from the assembly.



### Required arguments

- *featureNames*

  A sequence of Strings specifying the feature names that will be deleted from the assembly.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## excludeFromSimulation(...)



This method excludes the specified part instances from the analysis.



### Required arguments

- *instances*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects to be excluded from the analysis.

- *exclude*

  A Bool specifying whether to exclude the selected instances from the analysis or include them.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## featurelistInfo()



This method prints the name and status of all the features in the feature lists.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## getMassProperties(...)



This method returns the mass properties of the assembly, or instances or regions. Only beams, trusses, shells, solids, point, nonstructural mass, and rotary inertia elements are supported.



### Required arguments

None.

### Optional arguments

- *regions*

  A MeshElementArray, CellArray, FaceArray, EdgeArray, or list of PartInstance objects specifying the regions whose mass properties are to be queried. The whole assembly is queried by default.

- *relativeAccuracy*

  A SymbolicConstant specifying the relative accuracy for geometry computation. Possible values are LOW, MEDIUM, and HIGH. The default value is LOW.

- *useMesh*

  A Boolean specifying whether the mesh should be used in the computation if the geometry is meshed. The default value is False.

- *specifyDensity*

  A Boolean specifying whether a user-specified density should be used in regions with density errors such as undefined material density. The default value is False.

- *density*

  A double value specifying the user-specified density value to be used in regions with density errors. The user-specified density should be greater than 0.

- *specifyThickness*

  A Boolean specifying whether a user-specified thickness should be used in regions with thickness errors such as undefined thickness. The default value is False.

- *thickness*

  A double value specifying the user-specified thickness value to be used in regions with thickness errors. The user-specified thickness should be greater than 0.

- *miAboutCenterOfMass*

  A Boolean specifying if the moments of inertia should be evaluated about the center of mass. The default value is True.

- *miAboutPoint*

  A tuple of three floats specifying the coordinates of the point about which to evaluate the moment of inertia. By default if the moments of inertia are not being evaluated about the center of mass, they will be evaluated about the origin.

### Return value

A Dictionary object with the following items:

*area*: None or a Float specifying the sum of the area of the specified faces. The area is computed only for one side for shells.

*areaCentroid*: None or a tuple of three Floats representing the coordinates of the area centroid.

*volume*: None or a Float specifying the volume of the specified regions.

*volumeCentroid*: None or a tuple of three Floats representing the coordinates of the volume centroid.

*massFromMassPerUnitSurfaceArea*: None or a Float specifying the mass due to mass per unit surface area.

*mass*: None or a Float specifying the mass of the specified regions. It is the total mass and includes mass from quantities such as mass per unit surface area.

*centerOfMass*: None or a tuple of three Floats representing the coordinates of the center of mass.

*momentOfInertia*: None or a tuple of six Floats representing the moments of inertia about the center of mass or about the point specified.

*warnings*: A tuple of SymbolicConstants representing the problems encountered while computing the mass properties. Possible SymbolicConstants are:

UNSUPPORTED_ENTITIES: Some unsupported entities exist in the specified regions. The mass properties are computed only for beams, trusses, shells, solids, point and non-structural mass elements, and rotary inertia elements. The mass properties are not computed for axisymmetric elements, springs, connectors, gaskets, or any other elements.

MISSING_THICKNESS: For some regions, the section definitions are missing thickness values.

ZERO_THICKNESS: For some regions, the section definitions have a zero thickness value.

VARIABLE_THICKNESS: The nodal thickness or field thickness specified for some regions has been ignored.

NON_APPLICABLE_THICKNESS: For some regions, the thickness value is not applicable to the corresponding sections specified on the regions.

MISSING_DENSITY: For some regions, the section definitions are missing material density values.

MISSING_MATERIAL_DEFINITION: For some regions, the material definition is missing.

ZERO_DENSITY: For some regions, the section definitions have a zero material density value.

UNSUPPORTED_DENSITY: For some regions, either a negative material density or a temperature dependent density has been specified, or the material value is missing for one or more plies in the composite section.

SHELL_OFFSETS: For shells, this method does not account for any offsets specified.

MISSING_SECTION_DEFINITION: For some regions, the section definition is missing.

UNSUPPORTED_SECTION_DEFINITION: The section definition provided for some regions is not supported.

REINFORCEMENTS: This method does not account for any reinforcements specified on the model.

SMEARED_PROPERTIES: For regions with composite section assignments, the density is smeared across the thickness. The volume centroid and center of mass computations for a composite shell use a lumped mass approach where the volume and mass is assumed to be lumped in the plane of the shell. As a result of these approximations the volume centroid, center of mass and moments of inertia may be slightly inaccurate for regions with composite section assignments.

UNSUPPORTED_NON_STRUCTURAL_MASS_ENTITIES: This method does not account for any non-structural mass on wires.

INCORRECT_MOMENT_OF_INERTIA: For geometry regions with non-structural mass per volume, the non-structural mass is assumed to be a point mass at the centroid of the regions. Thus, the moments of inertia may be inaccurate as the distribution of the non-structural mass is not accounted for. Use the mesh for accurately computing the moments of inertia.

MISSING_BEAM_ORIENTATIONS: For some regions with beam section assignments, the beam section orientations are missing.

UNSUPPORTED_BEAM_PROFILES: This method supports the Box, Pipe, Circular, Rectangular, Hexagonal, Trapezoidal, I, L, T, Arbitrary, and Tapered beam profiles. Any other beam profile is not supported.

TAPERED_BEAM_MI: Moment of inertia calculations for tapered beams are not accurate.

SUBSTRUCTURE_INCORRECT_PROPERTIES: The user assigned density and thickness is not considered for substructures.

### Exceptions

None.



## getAngle(...)



This method returns the angle between the specified entities.



### Required arguments

- *plane1*

  A [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all), [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all), or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object specifying the first plane. The [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object must represent a datum plane. The *plane1* and *line1* arguments are mutually exclusive. One of them must be specified.

- *plane2*

  A [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all), [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all), or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object specifying the second plane. The [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object must represent a datum plane. The *plane2* and *line2* arguments are mutually exclusive. One of them must be specified.

- *line1*

  An [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all), [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all), or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object specifying the first curve. The [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object must represent a datum axis. The *plane1* and *line1* arguments are mutually exclusive. One of them must be specified.

- *line2*

  An [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all), [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all), or a [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object specifying the second curve. The [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) object must represent a datum axis. The *plane2* and *line2* arguments are mutually exclusive. One of them must be specified.

### Optional arguments

- *commonVertex*

  If the two selected [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects have more than one vertex in common, this [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifies the vertex at which to evaluate the angle.

### Return value

A Float specifying the angle between the specified entities. If you provide a plane as an argument, Abaqus/CAE computes the angle using the normal to the plane.

### Exceptions

None.



## getCoordinates(...)



This method returns the coordinates of a specified point.



### Required arguments

- *entity*

  A [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) point, [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all), or [ReferencePoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-referencepointpyc.htm?ContextScope=all) specifying the entity to query.

### Optional arguments

None.

### Return value

A tuple of three Floats representing the coordinates of the specified point.

### Exceptions

None.



## getDistance(...)



Depending on the arguments provided, this method returns one of the following:

- The distance between two points.
- The minimum distance between a point and an edge.
- The minimum distance between two edges.



### Required arguments

- *entity1*

  A [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) point, [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all), or [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) specifying the first entity from which to measure.

- *entity2*

  A [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all), [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) point, [MeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all), or [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) specifying the second entity to which to measure.

### Optional arguments

- *printResults*

  A Boolean that determines whether a verbose output is to be printed. The default is True

### Return value

A Float specifying the calculated distance.

### Exceptions

None.



## getFacesAndVerticesOfAttachmentLines(...)



Given an array of edge objects, this method returns a tuple of dictionary objects. Each object consists of five members including the attachment line and associated face and vertex objects.



### Required arguments

- *edges*

  An [EdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object which is a sequence of [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects.

### Optional arguments

None.

### Return value

A tuple of dictionary objects. Each dictionary contains five items with the following keys:

*edge*: An [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object specifying the attachment line.

*startFace*: A [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the face associated with one end of the attachment line.

*endFace*: A [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object specifying the face associated with the other end of the attachment line.

*startVertex*: A [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifying the vertex associated with one end of the attachment line. This end is also associated with the startFace.

*endVertex*: A [Vertex](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifying the vertex associated with the other end of the attachment line. This end is also associated with the endFace.

### Exceptions

None.



## getSurfaceSections(...)



This method returns a list of the sections assigned to the regions encompassed by the specified surface.



### Required arguments

- *surface*

  A string specifying the Surface name.

### Optional arguments

None.

### Return value

A tuple of strings representing the section names. If no section names are found, the tuple will contain one empty string.

### Exceptions

None.



## importEafFile(...)



This method imports an assembly from an EAF file into the root assembly.



### Required arguments

- *filename*

  A String specifying the path to the EAF file from which to import the assembly.

### Optional arguments

You use the following optional argument only to import specific instances and their associated parts.

- *ids*

  A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in the assembly tree or component identifier associated with the part in the EAF file. If *ids* is an empty sequence, all occurrences or parts will be imported. The default value is an empty sequence.

### Return value

None.

### Exceptions

None.



## importParasolidFile(...)



This method imports an assembly from the Parasolid file into the root assembly.



### Required arguments

- *filename*

  A String specifying the path to a Parasolid file from which to import the assembly.

### Optional arguments

You use the following optional argument only to import specific instances and their associated parts.

- *ids*

  A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in the assembly tree or component identifier associated with the part in the EAF file. If *ids* is an empty sequence, all occurrences or parts will be imported. The default value is an empty sequence.

### Return value

None.

### Exceptions

None.



## importCatiaV5File(...)



This method imports an assembly from a CATIA V5 Elysium Neutral file into the root assembly.



### Required arguments

- *filename*

  A String specifying the path to the CATIA V5 Elysium Neutral file from which to import the assembly.

### Optional arguments

You use the following optional argument only to import specific instances and their associated parts.

- *ids*

  A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in the assembly tree or component identifier associated with the part in the EAF file. If *ids* is an empty sequence, all occurrences or parts will be imported. The default value is an empty sequence.

### Return value

None.

### Exceptions

None.



## importEnfFile(...)



This method imports an assembly from an Elysium Neutral file created by Pro/ENGINEER, I-DEAS, or CATIA V5 into the root assembly.



### Required arguments

- *filename*

  A String specifying the path to the Elysium Neutral file from which to import the assembly.

### Optional arguments

You use the following optional argument only to import specific instances and their associated parts.

- *ids*

  A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in the assembly tree or component identifier associated with the part in the EAF file. If *ids* is an empty sequence, all occurrences or parts will be imported. The default value is an empty sequence.

### Return value

None.

### Exceptions

None.



## importIdeasFile(...)



This method imports an assembly from an I-DEAS Elysium Neutral file into the root assembly.



### Required arguments

- *filename*

  A String specifying the path to the I-DEAS Elysium Neutral file from which to import the assembly.

### Optional arguments

You use the following optional argument only to import specific instances and their associated parts.

- *ids*

  A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in the assembly tree or component identifier associated with the part in the EAF file. If *ids* is an empty sequence, all occurrences or parts will be imported. The default value is an empty sequence.

### Return value

None.

### Exceptions

None.



## importProEFile(...)



This method imports an assembly from a Pro/ENGINEER Elysium Neutral file into the root assembly.



### Required arguments

- *filename*

  A String specifying the path to the Pro/ENGINEER Elysium Neutral file from which to import the assembly.

### Optional arguments

You use the following optional argument only to import specific instances and their associated parts.

- *ids*

  A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in the assembly tree or component identifier associated with the part in the EAF file. If *ids* is an empty sequence, all occurrences or parts will be imported. The default value is an empty sequence.

### Return value

None.

### Exceptions

None.



## makeDependent(...)



This method converts the specified part instances from independent to dependent part instances.



### Required arguments

- *instances*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects to convert to dependent part instances.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## makeIndependent(...)



This method converts the specified part instances from dependent to independent part instances.



### Required arguments

- *instances*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects to convert to independent part instances.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## printAssignedSections()



This method prints a summary of assigned connector sections.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## printConnectorOrientations()



This method prints a summary of connector orientations.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## projectReferencesOntoSketch(...)



This method projects the specified edges, vertices, and datum points from the assembly onto the specified [ConstrainedSketch](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object. The edges, vertices, and datum points appear on the sketch as reference geometry.



### Required arguments

- *sketch*

  The [ConstrainedSketch](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object on which the edges, vertices, and datum points are projected.

### Optional arguments

- *filter*

  A SymbolicConstant specifying how to limit the amount of projection. Possible values are ALL_EDGES and COPLANAR_EDGES. If *filter*=COPLANAR_EDGES, edges that are coplanar to the sketching plane are the only candidates for projection. The default value is ALL_EDGES.

- *upToFeature*

  A Feature object specifying a marker in the feature-based history of the part. Abaqus/CAE projects onto the sketch only the part entities that were created before the feature specified by this marker. By default, all part entities are candidates for projection.

- *edges*

  A sequence of candidate edges to be projected onto the sketch. By default, all edges are candidates for projection.

- *vertices*

  A sequence of candidate vertices to be projected onto the sketch. By default, all vertices are candidates for projection.

### Return value

None.

### Exceptions

None.



## queryCachedStates()



This method displays the position of geometric states relative to the sequence of features in the assembly cache. The output is displayed in the message area.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## regenerate()



This method regenerates the assembly and brings it up to date with the latest values of the assembly parameters. When you modify features of an assembly, it may be convenient to postpone regeneration until you make all your changes, since regeneration can be time consuming. In contrast, when you modify features of a part that is included in the assembly, you should use this command to regenerate the assembly. When you regenerate the assembly, it will reflect the changes that you made to the part.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## regenerationWarnings()



This method prints any regeneration warnings associated with the features.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## restore()



This method restores the parameters of all features in the assembly to the value they had before a failed regeneration. Use the restore method after a failed regeneration, followed by a regenerate command.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## resumeAllFeatures()



This method resumes all the suppressed features in the part or assembly.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## resumeFeatures(...)



This method resumes the specified suppressed features in the assembly.



### Required arguments

- *featureNames*

  A sequence of Strings specifying the names of features to resume.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## resumeLastSetFeatures()



This method resumes the last set of features to be suppressed in the assembly.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## rotate(...)



This method rotates given instances by the specified amount.



### Required arguments

- *instanceList*

  A sequence of Strings specifying the names of instances to rotate.

- *axisPoint*

  A sequence of three Floats specifying the coordinates of a point on the axis.

- *axisDirection*

  A sequence of three Floats specifying the direction of the axis.

- *angle*

  A Float specifying the rotation angle in degrees. Use the right-hand rule to determine the direction.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## translate(...)



This method translates given instances by the specified amount.



### Required arguments

- *instanceList*

  A sequence of Strings specifying the names of instances to translate.

- *vector*

  A sequence of three Floats specifying a translation vector.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## saveGeometryCache()



This method caches the current geometry, which improves regeneration performance.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setValues(...)



This method modifies the behavior associated with the specified assembly.



### Required arguments

- *regenerateConstraintsTogether*

  A Boolean specifying whether the positioning constraints in the assembly should be regenerated together before regenerating other assembly features. The default value is ON.If the assembly has position constraint features and you modify the value of *regenerateConstraintsTogether*, Abaqus/CAE will regenerate the assembly features.

### Optional arguments

None.

### Return value

None.

### Exceptions

- If one or more features in the assembly fails to regenerate:

  FeatureError: Regeneration failed



## suppressFeatures(...)



This method suppresses specified features.



### Required arguments

- *featureNames*

  A sequence of Strings specifying the names of features to suppress in the assembly.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## unlinkInstances(...)



This method converts the specified [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects from linked child instances to regular instances. The parts associated with the selected instances will be converted to regular parts as well.



### Required arguments

- *instances*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects to be converted to regular part instances.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## writeAcisFile(...)



This method exports the assembly to a named file in ACIS part (SAT) or assembly (ASAT) format.



### Required arguments

- *fileName*

  A String specifying the name of the file to which to write. The file name's extension is used to determine whether a part or assembly is written. Use the file extension .asat for the assembly format.

### Optional arguments

- *version*

  A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS Version 12.0. The default value is the current version of ACIS.

### Return value

None.

### Exceptions

None.



## writeCADParameters(...)



This method writes the parameters that were imported from the CAD system to a parameter file.



### Required arguments

- *paramFile*

  A String specifying the parameter file name.

### Optional arguments

- *modifiedParams*

  A tuple of tuples each containing the part name, the parameter name and the modified parameter value. Default is an empty tuple.

- *updatePaths*

  A Bool specifying whether to update the path of the CAD model file specified in the *parameterFile* to the current directory, if the CAD model is present in the current directory.

### Return value

None.

### Exceptions

None.



## lock()



This method locks the assembly. Locking the assembly prevents any further changes to the assembly that can trigger regeneration of the assembly.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## unlock()



This method unlocks the assembly. Unlocking the assembly allows it to be regenerated after any modifications to the assembly.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## setMeshNumberingControl(...)



This method changes the start node and/or element labels on the specified independent part instances before or after Abaqus/CAE generates the meshes. For the meshed instances, Abaqus/CAE changes the node and/or element labels while preserving the original order and incrementation.



### Required arguments

- *instances*

  A sequence of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects to change the start node and/or element labels.

### Optional arguments

- *startNodeLabel*

  A positive Integer specifying the new start node label.

- *startElemLabel*

  A positive Integer specifying the new start element label.

### Return value

None.

### Exceptions

None.



## copyMeshPattern(...)



This method copies a mesh pattern from a source region consisting of a set of shell elements or element faces onto a target face, mapping nodes and elements in a one-one correspondence between source and target.



### Required arguments

None.

### Optional arguments

- *elements*

  A sequence of [MeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) objects or a Set object containing elements and specifying the source region.

- *faces*

  A sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) objects that have associated with shell elements or element faces and specifying the source region.

- *elemFaces*

  A sequence of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects specifying the source region.

- *targetFace*

  A [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object specifying the target region. The target face can be of a different part instance.

- *nodes*

  A sequence of MeshNode objects or a Set object containing nodes on the boundary of source region which are to be positioned to the boundary of target face.

- *coordinates*

  A sequence of three-dimensional coordinate tuples specifying the coordinates for each of the given nodes. When specified, the number of coordinate tuples must match the number of given nodes, and be ordered to correspond to the given nodes in *ascending order* according to index. These coordinates are positions of the nodes of a mesh that will be the target face corresponding to nodes provided.

### Return value

None.

### Exceptions

None.



## smoothNodes(...)



This method smooths the given nodes of a native mesh, moving them locally to a more optimal location that improves the quality of the mesh



### Required arguments

- *nodes*

  A sequence of MeshNode objects or a Set object containing nodes.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The Assembly object can have the following members:

- *isOutOfDate*

  An Int specifying that feature parameters have been modified but that the assembly has not been regenerated. Possible values are 0 and 1.

- *timeStamp*

  A Float specifying which gives an indication when the assembly was last modified.

- *isLocked*

  An Int specifying whether the assembly is locked or not. Possible values are 0 and 1.

- *regenerateConstraintsTogether*

  A Boolean specifying whether the positioning constraints in the assembly should be regenerated together before regenerating other assembly features. The default value is ON.If the assembly has position constraint features and you modify the value of *regenerateConstraintsTogether*, Abaqus/CAE will regenerate the assembly features.

- *vertices*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object specifying all the vertices existing at the assembly level. This member does not provide access to the vertices at the instance level.

- *edges*

  An [EdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object specifying all the edges existing at the assembly level. This member does not provide access to the edges at the instance level.

- *elements*

  A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object specifying all the elements existing at the assembly level. This member does not provide access to the elements at the instance level.

- *nodes*

  A [MeshNodeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object specifying all the nodes existing at the assembly level. This member does not provide access to the nodes at the instance level.

- *instances*

  A repository of [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) objects.

- *datums*

  A repository of [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) objects specifying all [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) objects in the assembly.

- *features*

  A repository of [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) objects specifying all [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) objects in the assembly.

- *featuresById*

  A repository of [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) objects specifying all [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) objects in the assembly.The [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) objects in the featuresById repository are the same as the [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) objects in the features repository. However, the key to the objects in the featuresById repository is an integer specifying the *ID*, whereas the key to the objects in the features repository is a string specifying the *name*.

- *surfaces*

  A repository of [Surface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacepyc.htm?ContextScope=all) objects specifying for more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *allSurfaces*

  A repository of [Surface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacepyc.htm?ContextScope=all) objects specifying for more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *allInternalSurfaces*

  A repository of [Surface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacepyc.htm?ContextScope=all) objects specifying picked regions.

- *sets*

  A repository of [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) objects.

- *allSets*

  A repository of [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) objects specifying for more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *allInternalSets*

  A repository of [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) objects specifying picked regions.

- *skins*

  A repository of [Skin](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-skinpyc.htm?ContextScope=all) objects specifying the skins created on the assembly.

- *stringers*

  A repository of [Stringer](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stringerpyc.htm?ContextScope=all) objects specifying the stringers created on the assembly.

- *referencePoints*

  A repository of [ReferencePoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-referencepointpyc.htm?ContextScope=all) objects.

- *modelInstances*

  A repository of [ModelInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelinstancepyc.htm?ContextScope=all) objects.

- *allinstances*

  A [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object specifying the PartInstances and A [ModelInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelinstancepyc.htm?ContextScope=all) object specifying the ModelInstances.

- *engineeringFeatures*

  An [EngineeringFeature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-engineeringfeaturepyc.htm?ContextScope=all) object.

- *modelName*

  A String specifying the name of the model to which the assembly belongs.

- *connectorOrientations*

  A [ConnectorOrientationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectororientationpyc.htm?ContextScope=all) object.

- *sectionAssignments*

  A [SectionAssignmentArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionassignmentpyc.htm?ContextScope=all) object.