# PartInstance object

A PartInstance object is an instance of a Part object.

## Access

```
import assembly
mdb.models[name].rootAssembly.allInstances[name]
mdb.models[name].rootAssembly.instances[name]
```

## Instance(...)



This method creates a PartInstance object and puts it into the instances repository.



### Path

```
mdb.models[name].rootAssembly.Instance
```

### Required arguments

- *name*

  A String specifying the repository key. The name must be a valid Abaqus object name.

- *part*

  A [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object to be instanced. If the part does not exist, no PartInstance object is created.

### Optional arguments

- *autoOffset*

  A Boolean specifying whether to apply an auto offset to the new part instance that will offset it from existing part instances. The default value is OFF.

- *dependent*

  A Boolean specifying whether the part instance is dependent or independent. If *dependent*=OFF, the part instance is independent. The default value is OFF.

### Return value

A PartInstance object.

### Exceptions

None.



## InstanceFromBooleanCut(...)



This method creates a PartInstance in the instances repository after subtracting or cutting the geometries of a group of part instances from that of a base part instance.



### Path

```
mdb.models[name].rootAssembly.InstanceFromBooleanCut
```

### Required arguments

- *name*

  A String specifying the repository key. The name must be a valid Abaqus object name.

- *instanceToBeCut*

  A PartInstance specifying the base instance from which to cut other instances.

- *cuttingInstances*

  A sequence of PartInstance objects specifying the instances with which to cut the base instance.

### Optional arguments

- *originalInstances*

  A SymbolicConstant specifying whether the original instances should be suppressed or deleted after the merge operation. Possible values are SUPPRESS or DELETE. The default value is SUPPRESS.

### Return value

A PartInstance object.

### Exceptions

None.



## InstanceFromBooleanMerge(...)



This method creates a PartInstance in the instances repository after merging two or more part instances.



### Path

```
mdb.models[name].rootAssembly.InstanceFromBooleanMerge
```

### Required arguments

- *name*

  A String specifying the repository key. The name must be a valid Abaqus object name.

- *instances*

  A sequence of PartInstance objects specifying the part instances to merge.

### Optional arguments

- *keepIntersections*

  A Boolean specifying whether the boundary intersections of Abaqus native part instances should be retained after the merge operation. The default value is False.

- *originalInstances*

  A SymbolicConstant specifying whether the original instances should be suppressed or deleted after the merge operation. Possible values are SUPPRESS or DELETE. The default value is SUPPRESS.

- *domain*

  A SymbolicConstant specifying whether geometry or mesh of the specified part instances is to be merged. Possible values are GEOMETRY, MESH or BOTH. The default value is GEOMETRY.

- *mergeNodes*

  A SymbolicConstant specifying which nodes of the specified part instances should be considered for merging. This argument is only applicable if *domain* is MESH. Possible values are BOUNDARY_ONLY, ALL, or NONE. The default value is BOUNDARY_ONLY.

- *nodeMergingTolerance*

  A Float specifying the maximum distance between nodes of the specified part instances that will be merged and replaced with a single node in the new part. The location of the new node is the average position of the deleted nodes. This argument is only applicable if *domain* is MESH. The default value is 10–6.

- *removeDuplicateElements*

  A Boolean specifying whether elements with the same connectivity in the new part will be merged into a single element. This argument is only applicable if *domain* is MESH. The default value is True.

### Return value

A PartInstance object.

### Exceptions

None.



## LinearInstancePattern(...)



This method creates multiple PartInstance objects in a linear pattern and puts them into the instances repository.



### Path

```
mdb.models[name].rootAssembly.LinearInstancePattern
```

### Required arguments

- *instanceList*

  A sequence of Strings specifying the names of instances to pattern.

- *number1*

  An Int specifying the total number of instances, including the original instances, that appear along the first direction in the pattern.

- *spacing1*

  A Float specifying the spacing between instances along the first direction in the pattern.

- *number2*

  An Int specifying the total number of instances, including the original instances, that appear along the second direction in the pattern.

- *spacing2*

  A Float specifying the spacing between instances along the second direction in the pattern.

### Optional arguments

- *direction1*

  A sequence of three Floats specifying a vector along the first direction. The default value is (1.0, 0.0, 0.0).

- *direction2*

  A sequence of three Floats specifying a vector along the second direction. The default value is (0.0, 1.0, 0.0).

### Return value

A sequence of PartInstance objects.

### Exceptions

None.



## RadialInstancePattern(...)



This method creates multiple PartInstance objects in a radial pattern and puts them into the instances repository.



### Path

```
mdb.models[name].rootAssembly.RadialInstancePattern
```

### Required arguments

- *instanceList*

  A sequence of Strings specifying the names of instances to pattern.

- *number*

  An Int specifying the total number of instances, including the original instances, that appear in the radial pattern.

- *totalAngle*

  A Float specifying the total angle in degrees between the first and last instance in the pattern. A positive angle corresponds to a counter-clockwise direction. The values 360° and −360° represent a special case where the pattern makes a full circle. In this case, because the copy would overlay the original, the copy is not placed at the last position. Possible values are −360.0 ≤≤ *totalAngle* ≤≤ 360.0.

### Optional arguments

- *point*

  A sequence of three Floats specifying the center of the radial pattern. The default value is (0.0, 0.0, 0.0).

- *axis*

  A sequence of three Floats specifying the central axis of the radial pattern. The default value is (0.0, 0.0, 1.0).

### Return value

A sequence of PartInstance objects.

### Exceptions

None.



## checkGeometry(...)



This method checks the validity of the geometry of the part instance and prints a count of all topological entities on the part instance (faces, edges, vertices, etc.).



### Required arguments

None.

### Optional arguments

- *detailed*

  A Boolean specifying whether detailed output will be printed to the replay file. The default value is OFF.

- *level*

  An Int specifying which level of checking is performed. Values can range from 20 to 70, with higher values reporting less and less important errors. The default value is 20, which reports all critical errors. When the default value is used, the stored validity status is updated to agree with the result of this check.

### Return value

None.

### Exceptions

- An exception is thrown if this is a dependent part instance and *level* was either not specified or was set to 20, because the validity status cannot be updated for a dependent part instance. In this case, this command should be called on the [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) instead.

  The geometry of dependent part instances cannot be changed.



## Contact(...)



This method translates an instance along the specified direction until it is in contact with a fixed instance.



### Required arguments

- *movableList*

  A sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) or [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects on the part instance to be moved.

- *fixedList*

  A sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) or [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects on the part instance to remain fixed.

- *direction*

  A sequence of three Floats specifying the direction of contact.

- *clearance*

  A Float specifying the distance between the two faces along the direction of contact.

### Optional arguments

- *isFaceEdges*

  A Boolean specifying how Abaqus calculates the contact. If *isFaceEdges* is OFF, contact is computed from the movable face to the fixed face. If *isFaceEdges* is ON, contact is computed using only the edges of the movable face and not its interior. The default value is OFF.

### Return value

A [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) object.

### Exceptions

None.



## ConvertConstraints()



This method converts the position constraints of an instance to absolute positions. The method deletes the constraint features on the instance but preserves the position in space.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## getPosition()



This method prints the sum of the translations and rotations applied to the PartInstance object.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## getRotation()



This method returns a tuple including the point of rotation, axis of rotation, and rotation angle (in degrees).



### Arguments

None.

### Return value

A tuple including the point of rotation, axis of rotation, and rotation angle (in degrees).

### Exceptions

None.



## getTranslation()



This method returns a tuple of three Floats representing translation in the *X*-, *Y*-, and *Z*-directions.



### Arguments

None.

### Return value

A tuple of three Floats representing the translation.

### Exceptions

None.



## replace(...)



This method replaces one instance with an instance of another part.



### Required arguments

- *instanceOf*

  A [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object specifying which Part will be instanced in place of the original [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all).

### Optional arguments

- *applyConstraints*

  A Boolean specifying whether to apply existing constraints on the new instance or to position the new instance in the same place as the original instance. The default value is True. A value of False indicates that constraints applies to the instance are deleted will be deleted from the feature list.

### Return value

None.

### Exceptions

None.



## rotateAboutAxis(...)



This method translates an instance by the specified amount.



### Required arguments

- *axisPoint*

  A sequence of three Floats specifying the *X*-, *Y*-, and *Z*-coordinates of a point on the axis.

- *axisDirection*

  A sequence of three Floats specifying the direction vector of the axis.

- *angle*

  A Float specifying the rotation angle in degrees. Use the right-hand rule to determine the direction.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## translate(...)



This method translates an instance by the specified amount.



### Required arguments

- *vector*

  A sequence of three Floats specifying a translation vector.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## translateTo(...)



This method translates an instance along the specified direction until it is in contact with a fixed instance.



### Required arguments

- *movableList*

  A sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) or [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects on the part instance to be moved.

- *fixedList*

  A sequence of [Face](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) or [Edge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) objects on the part instances to remain fixed.

- *direction*

  A sequence of three Floats specifying the direction of contact.

- *clearance*

  A Float specifying the distance between the two faces along the direction of contact.

### Optional arguments

- *vector*

  A sequence of three Floats specifying a translation vector. If this argument is specified, the movable instance will be translated by the specified amount without solving for the actual contact.

### Return value

A [Feature](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) object.

### Exceptions

None.



## Members

The PartInstance object can have the following members:

- *name*

  A String specifying the repository key. The name must be a valid Abaqus object name.

- *dependent*

  A Boolean specifying whether the part instance is dependent or independent. If *dependent*=OFF, the part instance is independent. The default value is OFF.

- *excludedFromSimulation*

  A Boolean specifying whether the part instance is excluded from the simulation. If *excludedFromSimulation*=ON, the part instance is excluded from the simulation. The default value is OFF.

- *geometryValidity*

  A Boolean specifying the validity of the geometry of the instance. The value is computed, but it can be set to ON to perform feature and mesh operations on an invalid instance. There is no guarantee that such operations will work if the instance was originally invalid.

- *analysisType*

  A SymbolicConstant specifying the part type. Possible values are DEFORMABLE_BODY, EULERIAN, DISCRETE_RIGID_SURFACE, and ANALYTIC_RIGID_SURFACE.

- *referenceNode*

  An Int specifying the reference node number. This member is valid only if *analysisType*=DISCRETE_RIGID_SURFACE or ANALYTIC_RIGID_SURFACE.

- *part*

  A [Part](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?ContextScope=all) object specifying the instanced part.

- *sets*

  A repository of [Set](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-setpyc.htm?ContextScope=all) objects specifying the sets created on the part. For more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *surfaces*

  A repository of [Surface](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacepyc.htm?ContextScope=all) objects specifying the surfaces created on the part. For more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *skins*

  A repository of [Skin](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-skinpyc.htm?ContextScope=all) objects specifying the skins created on the part. For more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *stringers*

  A repository of [Stringer](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stringerpyc.htm?ContextScope=all) objects specifying the stringers created on the part. For more information, see [Region commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all).

- *vertices*

  A [VertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vertexpyc.htm?ContextScope=all) object.

- *ignoredVertices*

  An [IgnoredVertexArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignoredvertexpyc.htm?ContextScope=all) object.

- *edges*

  An [EdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgepyc.htm?ContextScope=all) object.

- *ignoredEdges*

  An [IgnoredEdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ignorededgepyc.htm?ContextScope=all) object.

- *faces*

  A [FaceArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facepyc.htm?ContextScope=all) object.

- *cells*

  A [CellArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cellpyc.htm?ContextScope=all) object.

- *datums*

  A repository of [Datum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumpyc.htm?ContextScope=all) objects.

- *elements*

  A [MeshElementArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?ContextScope=all) object.

- *nodes*

  A [MeshNodeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?ContextScope=all) object.

- *elemFaces*

  A repository of [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) objects specifying all the element faces in the part instance. For a given element and a given face index within that element, the corresponding [MeshFace](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object can be retrieved from the repository by using the key calculated as (i*8 + j), where i and j are zero-based element and face indices, respectively.

- *elementFaces*

  A [MeshFaceArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?ContextScope=all) object.

- *elemEdges*

  A repository of [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) objects specifying all the element edges in the part instance. For a given element and a given edge index on a given face within that element, the corresponding [MeshEdge](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object can be retrieved from the repository by using the key calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge indices, respectively.

- *elementEdges*

  A [MeshEdgeArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?ContextScope=all) object.

- *referencePoints*

  A repository of [ReferencePoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-referencepointpyc.htm?ContextScope=all) objects.

- *partName*

  A String specifying the name of the part from which the instance was created.