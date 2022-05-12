import typing

from abaqusConstants import *
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region

from __init__ import *
from __future__ import annotations


class ConnAccelerationBC(BoundaryCondition):
    """The ConnAccelerationBC object stores the data for a connector acceleration boundary
    condition. 
    The ConnAccelerationBC object is derived from the BoundaryCondition object. 

    Attributes
    ----------
    name: str
        A String specifying the boundary condition repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
    fastenerName: str
        A String specifying the name of the assembled fastener to which the boundary condition
        will be applied. This argument is not valid when **region** is specified. When this
        argument is specified, **fastenerSetName** must also be specified. The default value is an
        empty string.
    fastenerSetName: str
        A String specifying the assembled fastener template model set to which the boundary
        condition will be applied. This argument is not valid when **region** is specified. When
        this argument is specified, **fastenerName** must also be specified. The default value is
        an empty string.
    category: SymbolicConstant
        A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.
    region: Region
        A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
    localCsys: str
        None or a :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the boundary
        condition's degrees of freedom. If **localCsys=None**, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].boundaryConditions[name]

    """

    # A String specifying the boundary condition repository key.
    name: str = ''

    # A SymbolicConstant specifying how the boundary condition is distributed spatially.
    # Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM.
    distributionType: SymbolicConstant = UNIFORM

    # A String specifying the name of the assembled fastener to which the boundary condition
    # will be applied. This argument is not valid when *region* is specified. When this
    # argument is specified, *fastenerSetName* must also be specified. The default value is an
    # empty string.
    fastenerName: str = ''

    # A String specifying the assembled fastener template model set to which the boundary
    # condition will be applied. This argument is not valid when *region* is specified. When
    # this argument is specified, *fastenerName* must also be specified. The default value is
    # an empty string.
    fastenerSetName: str = ''

    # A SymbolicConstant specifying the category of the boundary condition. Possible values
    # are MECHANICAL and THERMAL.
    category: SymbolicConstant = None

    # A Region object specifying the region to which the boundary condition is applied.
    region: Region = Region()

    # None or a DatumCsys object specifying the local coordinate system of the boundary
    # condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined
    # in the global coordinate system. The default value is None.
    localCsys: str = None

    def __init__(self,
                 name: str,
                 createStepName: str,
                 region: str = '',
                 fastenerName: str = '',
                 fastenerSetName: str = '',
                 a1: typing.Union[SymbolicConstant, float] = UNSET,
                 a2: typing.Union[SymbolicConstant, float] = UNSET,
                 a3: typing.Union[SymbolicConstant, float] = UNSET,
                 ar1: typing.Union[SymbolicConstant, float] = UNSET,
                 ar2: typing.Union[SymbolicConstant, float] = UNSET,
                 ar3: typing.Union[SymbolicConstant, float] = UNSET,
                 amplitude: str = UNSET,
                 distributionType: SymbolicConstant = UNIFORM):
        """This method creates an ConnAccelerationBC object on a wire region. Alternatively, the
        boundary condition may also be applied to a wire set referenced from an assembled
        fastener template model.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ConnAccelerationBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            The wire region to which the boundary condition is applied. This argument is not valid 
            when *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition 
            will be applied. This argument is not valid when *region* is specified. When this 
            argument is specified, *fastenerSetName* must also be specified. The default value is an 
            empty string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary 
            condition will be applied. This argument is not valid when *region* is specified. When 
            this argument is specified, *fastenerName* must also be specified. The default value is 
            an empty string. 
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET.Note:Although *a1*, *a2*, *a3*, *ar1*, *ar2*, and *ar3* are 
            optional arguments, at least one of them must be specified. 
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET. 
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET. 
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 

        Returns
        -------
            A ConnAccelerationBC object.
        """
        super().__init__()
        pass

    def setValues(self,
                  region: str = '',
                  fastenerName: str = '',
                  fastenerSetName: str = '',
                  a1: typing.Union[SymbolicConstant, float] = UNSET,
                  a2: typing.Union[SymbolicConstant, float] = UNSET,
                  a3: typing.Union[SymbolicConstant, float] = UNSET,
                  ar1: typing.Union[SymbolicConstant, float] = UNSET,
                  ar2: typing.Union[SymbolicConstant, float] = UNSET,
                  ar3: typing.Union[SymbolicConstant, float] = UNSET,
                  amplitude: str = UNSET,
                  distributionType: SymbolicConstant = UNIFORM):
        """This method modifies the data for an existing ConnAccelerationBC object in the step
        where it is created.
        
        Parameters
        ----------
        region
            The wire region to which the boundary condition is applied. This argument is not valid 
            when *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the boundary condition 
            will be applied. This argument is not valid when *region* is specified. When this 
            argument is specified, *fastenerSetName* must also be specified. The default value is an 
            empty string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the boundary 
            condition will be applied. This argument is not valid when *region* is specified. When 
            this argument is specified, *fastenerName* must also be specified. The default value is 
            an empty string. 
        a1
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET.Note:Although *a1*, *a2*, *a3*, *ar1*, *ar2*, and *ar3* are 
            optional arguments, at least one of them must be specified. 
        a2
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET. 
        a3
            A Float or a SymbolicConstant specifying the acceleration component in the connector's 
            local 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The 
            default value is UNSET. 
        ar1
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 4-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ar2
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 5-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        ar3
            A Float or a SymbolicConstant specifying the rotational acceleration component in the 
            connector's local 6-direction. Possible values for the SymbolicConstant are UNSET and 
            SET. The default value is UNSET. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the boundary condition has no amplitude reference. The default 
            value is UNSET. You should provide the *amplitude* argument only if it is valid for the 
            specified step. 
        distributionType
            A SymbolicConstant specifying how the boundary condition is distributed spatially. 
            Possible values are UNIFORM and USER_DEFINED. The default value is UNIFORM. 
        """
        pass

    def setValuesInStep(self,
                        stepName: str,
                        a1: typing.Union[SymbolicConstant, float] = SET,
                        a2: typing.Union[SymbolicConstant, float] = SET,
                        a3: typing.Union[SymbolicConstant, float] = SET,
                        ar1: typing.Union[SymbolicConstant, float] = SET,
                        ar2: typing.Union[SymbolicConstant, float] = SET,
                        ar3: typing.Union[SymbolicConstant, float] = SET,
                        amplitude: str = ''):
        """This method modifies the propagating data for an existing ConnAccelerationBC object in
        the specified step.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified. 
        a1
            A Float or a SymbolicConstant specifying the connector acceleration component in the 
            connector's local 1-direction. Possible values for the SymbolicConstant are SET, 
            UNCHANGED, and FREED. 
        a2
            A Float or a SymbolicConstant specifying the connector acceleration component in the 
            connector's local 2-direction. Possible values for the SymbolicConstant are SET, 
            UNCHANGED, and FREED. 
        a3
            A Float or a SymbolicConstant specifying the connector acceleration component in the 
            connector's local 3-direction. Possible values for the SymbolicConstant are SET, 
            UNCHANGED, and FREED. 
        ar1
            A Float or a SymbolicConstant specifying the connector acceleration component in the 
            connector's local 4-direction. Possible values for the SymbolicConstant are SET, 
            UNCHANGED, and FREED. 
        ar2
            A Float or a SymbolicConstant specifying the connector acceleration component in the 
            connector's local 5-direction. Possible values for the SymbolicConstant are SET, 
            UNCHANGED, and FREED. 
        ar3
            A Float or a SymbolicConstant specifying the connector acceleration component in the 
            connector's local 6-direction. Possible values for the SymbolicConstant are SET, 
            UNCHANGED, and FREED. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous analysis step. FREED should be used if the 
            boundary condition is changed to have no amplitude reference. You should provide the 
            *amplitude* argument only if it is valid for the specified step. 
        """
        pass
