from .OdbSet import OdbSet
from .SectionPoint import SectionPoint
from abaqusConstants import *

class FieldOutput:

    """A FieldOutput object contains field data for a specific output variable. 

    Access
    ------
        - import
        - odbAccess
        - session.odbs[name].steps[name].frames[i].fieldOutputs[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the dimension of vector or the first dimension (number of rows) of 
    # matrix. 
    dim: int = None

    # An Int specifying the second dimension (number of columns) of matrix. 
    dim2: int = None

    # A Boolean specifying whether the data are complex. 
    isComplex: Boolean = OFF

    # A FieldLocationArray object. 
    locations: FieldLocationArray = None

    # A FieldValueArray object specifying the order of the objects in the array is determined 
    # by the Abaqus Scripting Interface; see the *data* argument to the addData method for a 
    # description of the order. 
    values: int = None

    def __init__(self, field: 'FieldOutput', name: str = '', description: str = ''):
        """This method creates a FieldOutput object from an existing FieldOutput object of the same
        output database.

        Path
        ----
            - session.odbs[name].steps[name].frames[i].FieldOutput

        Parameters
        ----------
        field
            A FieldOutput object. 
        name
            A String specifying the name of the FieldOutput object. 
        description
            A String specifying the output variable. Colon (:) should not be used as a part of the 
            field output description. 

        Returns
        -------
            A FieldOutput object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def addData(self, position: SymbolicConstant, set: OdbSet, data: tuple, sectionPoint: SectionPoint = None, 
                conjugateData: float = None):
        """This method adds data to a FieldOutput object.

        Parameters
        ----------
        position
            A SymbolicConstant specifying the position of the output. Possible values are:NODAL, 
            specifying the values calculated at the nodes.INTEGRATION_POINT, specifying the values 
            calculated at the integration points.ELEMENT_NODAL, specifying the values obtained by 
            extrapolating results calculated at the integration points.CENTROID, specifying the 
            value at the centroid obtained by extrapolating results calculated at the integration 
            points.ELEMENT_FACE_INTEGRATION_POINT, specifying the values calculated at the element 
            face integration points.SURFACE_INTEGRATION_POINT, specifying the values calculated at 
            the surface integration points. Selecting this value prompts the Visualization module to 
            calculate the sum of the values at the ELEMENT_FACE_INTEGRATION_POINT position from 
            multiple surfaces. 
        set
            An OdbSet object specifying the instance-level set defining the region for addData. The 
            set must be defined in the same output database as the output database into which the 
            new field output data is being written. For better performance, the node or element 
            labels in the set are preferred to be sorted in ascending order and must be specified in 
            the same order as the values provided for the *data* argument. 
        data
            A sequence of sequences of Floats specifying the data values for the specified position 
            and labels in the set. Each row of data provides the value at one unique position. The 
            width of each row should match the number of required components for the data. The 
            values must be given in the order that matches the ordering of labels in the set.The 
            order of the element nodal data, integration point data, and section point data for 
            beams and shells follows the conventions defined in the Abaqus Elements Guide. 
        sectionPoint
            A SectionPoint object specifying the location in the section. Although*sectionPoint* is 
            an optional argument to theaddData method, omitting the argument does have consequences 
            for visualization. If you omit the argument when you are writing field output data for a 
            shell or a beam, you cannot subsequently select the section point to display when you 
            are displaying the field output data using the Visualization module. 
        conjugateData
            An odb_SequenceSequenceFloat object specifying the imaginary data values for the 
            specified position, instance, and labels. You must provide this data when you add 
            complex fields to the output database. The order of the values follows the conventions 
            defined in the Abaqus Elements Guide. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            - If you specify an odbSet containing entities from multiple instances: 
              odbException: Entities from multiple instances present in set. 
            - The addData method throws many exceptions of type odbException. For example, if the 
            local coordinate system is specified for scalar data: 
              odbException: Transformation not allowed for scalar data. 
        """
        pass

    def getScalarField(self, componentLabel: str):
        """This method generates a scalar field containing the extracted component or calculated
        invariant values. The new field will hold values for the same nodes or elements as the
        parent field. Abaqus will perform this operation on only the real part of the
        FieldOutput object. The operation is not performed on the conjugate data (the imaginary
        portion of a complex result).

        Parameters
        ----------
        componentLabel
            A String specifying the component label, such as “S11”. 

        Returns
        -------
            A FieldOutput object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getSubset(self, elementType: str = ''):
        """A FieldOutput object with a subset of the field values.

        Parameters
        ----------
        elementType
            A String specifying the element type for which to extract values. The string must 
            correspond to a valid Abaqus element type. 

        Returns
        -------
            A FieldOutput object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getTransformedField(self, datumCsys: str, deformationField: 'FieldOutput' = None, 
                            rotationField: 'FieldOutput' = None, projected22Axis: int = None, 
                            projectionTol: str = ''):
        """This method generates a new vector or tensor field containing the transformed component
        values of the parent field. The new field will hold values for the same nodes or
        elements as the parent field. Results will be transformed based on the orientations
        specified by the input DatumCsys object. Abaqus will perform this operation on only the
        real part of the FieldOutput object. The operation is not performed on the conjugate
        data (the imaginary portion of a complex result).

        Parameters
        ----------
        datumCsys
            A valid DatumCsys object designating the coordinate system. Valid systems can be fixed 
            or positioned with respect to nodes on the model and can be cartesian, cylindrical, or 
            spherical. 
        deformationField
            A FieldOutput object specifying the nodal displacement vectors required by moving 
            coordinate systems to determine instantaneous configurations. 
        rotationField
            A FieldOutput object specifying the nodal rotational displacement vectors required by 
            moving coordinate systems that follow a 6-dof node, to determine instantaneous 
            configurations. 
        projected22Axis
            An Int specifying which axis of the coordinate system will be projected as the second 
            component for local result orientations. Valid values are 1, 2, or 3; the default value 
            is 2. 
        projectionTol
            A Double specifying the minimum allowable angle (radians) between the specified 
            projection axis and the element normal. The next axis will be used for projection if 
            this tolerance test fails. 

        Returns
        -------
            A FieldOutput object. 

        Exceptions
        ----------
            - The getTransformedField method throws an exception if the field contains any assembly 
            level nodes. 
              odbException: Cannot apply transformation to field containing assembly level nodes. 
        """
        pass

    def getConnectorFieldXformedToNodeA(self, deformationField: 'FieldOutput' = None):
        """This method generates a new vector field containing the transformed component values of
        the parent connector field to the node A coordinate system. The new field will hold
        values for the same connector elements as the parent field. Some connection types such
        as Axial, Link, Slip Ring, and Radial Thrust require that the deformationField be
        specified.

        Parameters
        ----------
        deformationField
            A FieldOutput object specifying the nodal displacement vectors required by moving 
            coordinate systems to determine instantaneous configurations. 

        Returns
        -------
            A FieldOutput object. 

        Exceptions
        ----------
            - The getConnectorFieldXformedToNodeA method throws an exception if the field requires a 
            deformationField and the argument is not supplied. 
              odbException: Deformation field is required for transforming this connector field. 
        """
        pass

    def setComponentLabels(self, componentLabels: tuple):
        """This method sets the component labels for the FieldOutput object.

        Parameters
        ----------
        componentLabels
            A sequence of Strings specifying the labels for each component of the value. The length 
            of the sequence must match the type. If *type*=TENSOR, the default value is *name* with 
            the suffixes ('11', '22', '33', '12', '13', '23'). If *type*=VECTOR, the default value 
            is *name* with the suffixes ('1', '2', '3'). If *type*=SCALAR, the default value is an 
            empty sequence. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setDataType(self, type: SymbolicConstant):
        """This method sets the data type of a FieldOutput object.

        Parameters
        ----------
        type
            A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR, 
            TENSOR_3D_FULL, TENSOR_3D_PLANAR, TENSOR_3D_SURFACE, TENSOR_2D_PLANAR, and 
            TENSOR_2D_SURFACE. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValidInvariants(self, validInvariants: SymbolicConstant):
        """This method sets the invariants valid for the FieldOutput object.

        Parameters
        ----------
        validInvariants
            A sequence of SymbolicConstants specifying which invariants should be calculated for 
            this field. An empty sequence indicates that no invariants are valid for this field. 
            Possible values are: 
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

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

