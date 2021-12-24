# FieldOutput object

A FieldOutput object contains field data for a specific output variable.

## Access

```
import
odbAccess
session.odbs[name].steps[name].frames[i].fieldOutputs[name]
```

## FieldOutput(...)



This method creates a FieldOutput object.



### Path

```
session.odbs[name].steps[name].frames[i].FieldOutput
```

### Required arguments

- *name*

  A String specifying the output variable name.

- *description*

  A String specifying the output variable. Colon (:) should not be used as a part of the field output description.

- *type*

  A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR, TENSOR_3D_FULL, TENSOR_3D_PLANAR, TENSOR_3D_SURFACE, TENSOR_2D_PLANAR, and TENSOR_2D_SURFACE.

### Optional arguments

- *componentLabels*

  A sequence of Strings specifying the labels for each component of the value. The length of the sequence must match the type. If *type*=TENSOR, the default value is *name* with the suffixes ('11', '22', '33', '12', '13', '23'). If *type*=VECTOR, the default value is *name* with the suffixes ('1', '2', '3'). If *type*=SCALAR, the default value is an empty sequence.

- *validInvariants*

  A sequence of SymbolicConstants specifying which invariants should be calculated for this field. An empty sequence indicates that no invariants are valid for this field. Possible values are:MAGNITUDEMISESTRESCAPRESSINV3MAX_PRINCIPALMID_PRINCIPALMIN_PRINCIPALMAX_INPLANE_PRINCIPALMIN_INPLANE_PRINCIPALOUTOFPLANE_PRINCIPALThe default value is an empty sequence.

- *isEngineeringTensor*

  A Boolean specifying whether the field is an engineering tensor or not. Setting isEngineeringTensor to true makes a tensor field behave as a strain like quantity where the off-diagonal components of tensor are halved for invariants computation. This parameter applies only to tensor field outputs. The default value is OFF.

### Return value

A FieldOutput object.

### Exceptions

None.

## FieldOutput(...)



This method creates a FieldOutput object from an existing FieldOutput object of the same output database.



### Path

```
session.odbs[name].steps[name].frames[i].FieldOutput
```

### Required arguments

- *field*

  A FieldOutput object.

### Optional arguments

- *name*

  A String specifying the name of the FieldOutput object.

- *description*

  A String specifying the output variable. Colon (:) should not be used as a part of the field output description.

### Return value

A FieldOutput object.

### Exceptions

None.



## addData(...)



This method adds data to a FieldOutput object.



### Required arguments

- *position*

  A SymbolicConstant specifying the position of the output. Possible values are:

  - NODAL, specifying the values calculated at the nodes.
  - INTEGRATION_POINT, specifying the values calculated at the integration points.
  - ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at the integration points.
  - CENTROID, specifying the value at the centroid obtained by extrapolating results calculated at the integration points.
  - ELEMENT_FACE_INTEGRATION_POINT, specifying the values calculated at the element face integration points.
  - SURFACE_INTEGRATION_POINT, specifying the values calculated at the surface integration points. Selecting this value prompts the Visualization module to calculate the sum of the values at the ELEMENT_FACE_INTEGRATION_POINT position from multiple surfaces.

- *instance*

  An [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) object specifying the namespace for labels.

- *labels*

  A sequence of Ints specifying the labels of the nodes or elements where the values in *data* are located. For better performance, the node or element labels are preferred to be sorted in ascending order and must be specified in the same order as the values provided for the *data* argument.

- *data*

  A sequence of sequences of Floats specifying the data values for the specified *position*, *instance*, and *labels*. The values must be given in the correct order. Element nodal data follow the order of nodal connectivity defined in the Abaqus documentation. Integration point data follow the order defined in the Abaqus documentation. Section point data for beams and shells follow the convention given in the Abaqus documentation. For more information, see the [Abaqus Elements Guide](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-ov.htm?ContextScope=all). These data create [FieldValue](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldvaluepyc.htm?ContextScope=all) objects internally.

### Optional arguments

- *sectionPoint*

  A [SectionPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?ContextScope=all) object specifying the location in the section. Although *sectionPoint* is an optional argument to the addData method, omitting the argument does have consequences for visualization. If you omit the argument when you are writing field output data for a shell or a beam, you cannot subsequently select the section point to display when you are displaying the field output data using the Visualization module.

- *localCoordSystem*

  The *localCoordSystem* parameter can be specified using either of the following:A sequence of sequences of Floats specifying the 3 × 3 matrix of direction cosines of the local coordinate system. This argument is available only for fields with type=TENSOR or VECTOR.A sequence of matrices of floats specifying the direction cosines of the local coordinates systems, where the sequence is the same length as *data*. If *localCoordSystem* is a matrix, a different local coordinate system applies to each data value.User supplied values of localCoordSystem are transposed before storing in the database.

### Return value

None.

### Exceptions

- The addData method throws many exceptions of type odbException. For example, if the local coordinate system is specified for scalar data:

  odbException: Transformation not allowed for scalar data.



## addData(...)



This method adds the data from a field created using the getSubset method and mathematical operators to the database. The user must create a field to contain the new data and then use the addData method to assign the data from the fields.



### Required arguments

- *field*

  A FieldOutput object specifying the data to add.

### Optional arguments

None.

### Return value

None.

### Exceptions

- The addData method throws many exceptions of type odbException. For example, if the local coordinate system is specified for scalar data:

  odbException: Transformation not allowed for scalar data.



## addData(...)



This method adds data to a FieldOutput object.



### Required arguments

- *position*

  A SymbolicConstant specifying the position of the output. Possible values are:NODAL, specifying the values calculated at the nodes.INTEGRATION_POINT, specifying the values calculated at the integration points.ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at the integration points.CENTROID, specifying the value at the centroid obtained by extrapolating results calculated at the integration points.ELEMENT_FACE_INTEGRATION_POINT, specifying the values calculated at the element face integration points.SURFACE_INTEGRATION_POINT, specifying the values calculated at the surface integration points. Selecting this value prompts the Visualization module to calculate the sum of the values at the ELEMENT_FACE_INTEGRATION_POINT position from multiple surfaces.

- *set*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the instance-level set defining the region for addData. The set must be defined in the same output database as the output database into which the new field output data is being written. For better performance, the node or element labels in the set are preferred to be sorted in ascending order and must be specified in the same order as the values provided for the *data* argument.

- *data*

  A sequence of sequences of Floats specifying the data values for the specified position and labels in the set. Each row of data provides the value at one unique position. The width of each row should match the number of required components for the data. The values must be given in the order that matches the ordering of labels in the set.The order of the element nodal data, integration point data, and section point data for beams and shells follows the conventions defined in the [Abaqus Elements Guide](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-ov.htm?ContextScope=all).

### Optional arguments

- *sectionPoint*

  A [SectionPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?ContextScope=all) object specifying the location in the section. Although*sectionPoint* is an optional argument to theaddData method, omitting the argument does have consequences for visualization. If you omit the argument when you are writing field output data for a shell or a beam, you cannot subsequently select the section point to display when you are displaying the field output data using the Visualization module.

- *conjugateData*

  An odb_SequenceSequenceFloat object specifying the imaginary data values for the specified position, instance, and labels. You must provide this data when you add complex fields to the output database. The order of the values follows the conventions defined in the [Abaqus Elements Guide](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-ov.htm?ContextScope=all).

### Return value

None.

### Exceptions

- If you specify an odbSet containing entities from multiple instances:

  odbException: Entities from multiple instances present in set.

- The addData method throws many exceptions of type odbException. For example, if the local coordinate system is specified for scalar data:

  odbException: Transformation not allowed for scalar data.



## getScalarField(...)



This method generates a scalar field containing the extracted component or calculated invariant values. The new field will hold values for the same nodes or elements as the parent field. Abaqus will perform this operation on only the real part of the FieldOutput object. The operation is not performed on the conjugate data (the imaginary portion of a complex result).



### Required arguments

- *invariant*

  A SymbolicConstant specifying the invariant. Possible values areMAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL, MID_PRINCIPAL, MIN_PRINCIPAL, MAX_INPLANE_PRINCIPAL, MIN_INPLANE_PRINCIPAL, and OUTOFPLANE_PRINCIPAL.

### Optional arguments

None.

### Return value

AFieldOutput object.

### Exceptions

None.



## getScalarField(...)



This method generates a scalar field containing the extracted component or calculated invariant values. The new field will hold values for the same nodes or elements as the parent field. Abaqus will perform this operation on only the real part of the FieldOutput object. The operation is not performed on the conjugate data (the imaginary portion of a complex result).



### Required arguments

- *componentLabel*

  A String specifying the component label, such as “S11”.

### Optional arguments

None.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *position*

  *position*

  A SymbolicConstant specifying the position of the output in the element. Possible values are:

  - NODAL, specifying the values calculated at the nodes.
  - INTEGRATION_POINT, specifying the values calculated at the integration points.
  - ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at the integration points.
  - CENTROID, specifying the value at the centroid obtained by extrapolating results calculated at the integration points.

  If the requested field values are not found in the output database at the specified ELEMENT_NODAL or CENTROID positions, they are extrapolated from the field data at the INTEGRATION_POINT position for the entire field region. If the field values are found at the specified positions, only these field values are returned without any extrapolation. This could potentially be only for a subset of the field region, depending on the output request.

- *readOnly*

  A Boolean specifying whether the extrapolated data returned by this call is written to the output database. The default value is OFF.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) specifying the region for which to extract values. For better performance, the node or element labels in the sets are preferred to be sorted in ascending order.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *localCoordSystem*

  A sequence of sequences of Floats specifying the 3 × 3 matrix of direction cosines. Field values associated with the supplied coordinate system will be extracted.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *sectionPoint*

  A [SectionPoint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?ContextScope=all) object.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *location*

  A [FieldLocation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldlocationpyc.htm?ContextScope=all) object.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *region*

  An [OdbMeshElement](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?ContextScope=all) specifying the region for which to extract values.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *region*

  An [OdbMeshNode](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?ContextScope=all) specifying the region for which to extract values.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *region*

  An [OdbInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?ContextScope=all) specifying the region for which to extract values.

### Return value

A FieldOutput object.

### Exceptions

None.



## getSubset(...)



A FieldOutput object with a subset of the field values.



### Required arguments

None.

### Optional arguments

- *elementType*

  A String specifying the element type for which to extract values. The string must correspond to a valid Abaqus element type.

### Return value

A FieldOutput object.

### Exceptions

None.



## getTransformedField(...)



This method generates a new vector or tensor field containing the transformed component values of the parent field. The new field will hold values for the same nodes or elements as the parent field. Results will be transformed based on the orientations specified by the input [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object. Abaqus will perform this operation on only the real part of the FieldOutput object. The operation is not performed on the conjugate data (the imaginary portion of a complex result).



### Required arguments

- *datumCsys*

  A valid [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object designating the coordinate system. Valid systems can be fixed or positioned with respect to nodes on the model and can be cartesian, cylindrical, or spherical.

### Optional arguments

- *projected22Axis*

  An Int specifying which axis of the coordinate system will be projected as the second component for local result orientations. Valid values are 1, 2, or 3; the default value is 2.

- *projectionTol*

  A Double specifying the minimum allowable angle (radians) between the specified projection axis and the element normal. The next axis will be used for projection if this tolerance test fails.

### Return value

A FieldOutput object.

### Exceptions

- The getTransformedField method throws an exception if the field contains any assembly level nodes.

  odbException: Cannot apply transformation to field containing assembly level nodes.



## getTransformedField(...)



This method generates a new vector or tensor field containing the transformed component values of the parent field. The new field will hold values for the same nodes or elements as the parent field. Results will be transformed based on the orientations specified by the input [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object. Abaqus will perform this operation on only the real part of the FieldOutput object. The operation is not performed on the conjugate data (the imaginary portion of a complex result).



### Required arguments

- *datumCsys*

  A valid [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object designating the coordinate system. Valid systems can be fixed or positioned with respect to nodes on the model and can be cartesian, cylindrical, or spherical.

### Optional arguments

- *deformationField*

  A FieldOutput object specifying the nodal displacement vectors required by moving coordinate systems to determine instantaneous configurations.

- *projected22Axis*

  An Int specifying which axis of the coordinate system will be projected as the second component for local result orientations. Valid values are 1, 2, or 3; the default value is 2.

- *projectionTol*

  A Double specifying the minimum allowable angle (radians) between the specified projection axis and the element normal. The next axis will be used for projection if this tolerance test fails.

### Return value

A FieldOutput object.

### Exceptions

- The getTransformedField method throws an exception if the field contains any assembly level nodes.

  odbException: Cannot apply transformation to field containing assembly level nodes.



## getTransformedField(...)



This method generates a new vector or tensor field containing the transformed component values of the parent field. The new field will hold values for the same nodes or elements as the parent field. Results will be transformed based on the orientations specified by the input [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object. Abaqus will perform this operation on only the real part of the FieldOutput object. The operation is not performed on the conjugate data (the imaginary portion of a complex result).



### Required arguments

- *datumCsys*

  A valid [DatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?ContextScope=all) object designating the coordinate system. Valid systems can be fixed or positioned with respect to nodes on the model and can be cartesian, cylindrical, or spherical.

### Optional arguments

- *deformationField*

  A FieldOutput object specifying the nodal displacement vectors required by moving coordinate systems to determine instantaneous configurations.

- *rotationField*

  A FieldOutput object specifying the nodal rotational displacement vectors required by moving coordinate systems that follow a 6-dof node, to determine instantaneous configurations.

- *projected22Axis*

  An Int specifying which axis of the coordinate system will be projected as the second component for local result orientations. Valid values are 1, 2, or 3; the default value is 2.

- *projectionTol*

  A Double specifying the minimum allowable angle (radians) between the specified projection axis and the element normal. The next axis will be used for projection if this tolerance test fails.

### Return value

A FieldOutput object.

### Exceptions

- The getTransformedField method throws an exception if the field contains any assembly level nodes.

  odbException: Cannot apply transformation to field containing assembly level nodes.



## getConnectorFieldXformedToNodeA(...)



This method generates a new vector field containing the transformed component values of the parent connector field to the node A coordinate system. The new field will hold values for the same connector elements as the parent field. Some connection types such as Axial, Link, Slip Ring, and Radial Thrust require that the deformationField be specified.



### Required arguments

None.

### Optional arguments

- *deformationField*

  A FieldOutput object specifying the nodal displacement vectors required by moving coordinate systems to determine instantaneous configurations.

### Return value

A FieldOutput object.

### Exceptions

- The getConnectorFieldXformedToNodeA method throws an exception if the field requires a deformationField and the argument is not supplied.

  odbException: Deformation field is required for transforming this connector field.



## setComponentLabels(...)



This method sets the component labels for the FieldOutput object.



### Required arguments

- *componentLabels*

  A sequence of Strings specifying the labels for each component of the value. The length of the sequence must match the type. If *type*=TENSOR, the default value is *name* with the suffixes ('11', '22', '33', '12', '13', '23'). If *type*=VECTOR, the default value is *name* with the suffixes ('1', '2', '3'). If *type*=SCALAR, the default value is an empty sequence.

### Return value

None.

### Exceptions

None.



## setDataType(...)



This method sets the data type of a FieldOutput object.



### Required arguments

- *type*

  A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR, TENSOR_3D_FULL, TENSOR_3D_PLANAR, TENSOR_3D_SURFACE, TENSOR_2D_PLANAR, and TENSOR_2D_SURFACE.

### Return value

None.

### Exceptions

None.



## setValidInvariants(...)



This method sets the invariants valid for the FieldOutput object.



### Required arguments

- *validInvariants*

  A sequence of SymbolicConstants specifying which invariants should be calculated for this field. An empty sequence indicates that no invariants are valid for this field. Possible values are:

  - MAGNITUDE
  - MISES
  - TRESCA
  - PRESS
  - INV3
  - MAX_PRINCIPAL
  - MID_PRINCIPAL
  - MIN_PRINCIPAL
  - MAX_INPLANE_PRINCIPAL
  - MIN_INPLANE_PRINCIPAL
  - OUTOFPLANE_PRINCIPAL

  The default value is an empty sequence.

### Return value

None.

### Exceptions

None.



## Members

The FieldOutput object has members with the same names and descriptions as the arguments to the [FieldOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?ContextScope=all#simaker-fieldoutputfieldoutputpyc) method.

In addition, the FieldOutput object can have the following members:

- *dim*

  An Int specifying the dimension of vector or the first dimension (number of rows) of matrix.

- *dim2*

  An Int specifying the second dimension (number of columns) of matrix.

- *isComplex*

  A Boolean specifying whether the data are complex.

- *locations*

  A [FieldLocationArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldlocationpyc.htm?ContextScope=all) object.

- *values*

  A [FieldValueArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldvaluepyc.htm?ContextScope=all) object specifying the order of the objects in the array is determined by the Abaqus Scripting Interface; see the *data* argument to the addData method for a description of the order.