import typing

from abaqusConstants import *
from .ContactPropertyAssignment import ContactPropertyAssignment
from .InitializationAssignment import InitializationAssignment
from .Interaction import Interaction
from .MainSecondaryAssignment import MainSecondaryAssignment
from .RegionPairs import RegionPairs
from .SlidingFormulationAssignment import SlidingFormulationAssignment
from .SlidingTransitionAssignments import SlidingTransitionAssignments
from .SmoothingAssignment import SmoothingAssignment
from .StabilizationAssignment import StabilizationAssignment
from .SurfaceBeamSmoothingAssignment import SurfaceBeamSmoothingAssignment
from .SurfaceFeatureAssignment import SurfaceFeatureAssignment
from .SurfaceOffsetAssignment import SurfaceOffsetAssignment
from .SurfaceThicknessAssignment import SurfaceThicknessAssignment
from .SurfaceVertexCriteriaAssignment import SurfaceVertexCriteriaAssignment


class ContactStd(Interaction):

    """The ContactStd object defines the contact domain and associated properties during 
    contact in an Abaqus/Standard analysis. 
    The ContactStd object is derived from the Interaction object. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - CONTACT

    """

    # A String specifying the repository key. 
    name: str = ''

    # A Boolean specifying whether surface smoothing (geometric correction) is automatically 
    # applied to all eligible surfaces. The default value is ON. 
    globalSmoothing: Boolean = ON

    # A RegionPairs object specifying the domain pairs included in contact. 
    includedPairs: RegionPairs = None

    # A RegionPairs object specifying the domain pairs excluded from contact. 
    excludedPairs: RegionPairs = None

    # A ContactPropertyAssignment object specifying the contact property assignments in the 
    # contact domain. 
    contactPropertyAssignments: ContactPropertyAssignment = None

    # A SurfaceThicknessAssignment object specifying the surface thickness assignments in the 
    # contact domain. 
    surfaceThicknessAssignments: SurfaceThicknessAssignment = None

    # A SurfaceOffsetAssignment object specifying the surface offset fraction assignments in 
    # the contact domain. 
    surfaceOffsetAssignments: SurfaceOffsetAssignment = None

    # A MainSecondaryAssignment object specifying the main-secondary assignments in the 
    # contact domain. 
    mainSecondaryAssignments: MainSecondaryAssignment = None

    # An InitializationAssignment object specifying the contact initialization assignments in 
    # the contact domain. 
    initializationAssignments: InitializationAssignment = None

    # A StabilizationAssignment object specifying the contact stabilization assignments in the 
    # contact domain. 
    stabilizationAssignments: StabilizationAssignment = None

    # A SmoothingAssignment object specifying the surface smoothing assignments in the contact 
    # domain. 
    smoothingAssignments: SmoothingAssignment = None

    # A SurfaceFeatureAssignment object specifying the surface feature angle assignments in 
    # the contact domain. 
    surfaceFeatureAssignments: SurfaceFeatureAssignment = None

    # A SlidingTransitionAssignments object specifying the sliding transition assignments in 
    # the contact domain. 
    slidingTransitionAssignments: SlidingTransitionAssignments = None

    # A Boolean specifying whether to assign the edge-to-edge formulation. The default value 
    # is False. 
    assignEdgeToEdgeformulation: Boolean = False

    # A symbolic constant specifying edge-to-edge formulation. The default value is NO. 
    edgeToEdgeFormulation: str = NO

    @typing.overload
    def __init__(self, name: str, createStepName: str, useAllstar: Boolean = OFF, 
                 globalSmoothing: Boolean = ON, includedPairs: RegionPairs = None, 
                 excludedPairs: RegionPairs = None, 
                 contactPropertyAssignments: ContactPropertyAssignment = None, 
                 surfaceThicknessAssignments: SurfaceThicknessAssignment = None, 
                 surfaceOffsetAssignments: SurfaceOffsetAssignment = None, 
                 surfaceFeatureAssignments: SurfaceFeatureAssignment = None, 
                 surfaceBeamSmoothingAssignments: SurfaceBeamSmoothingAssignment = None, 
                 surfaceVertexCriteriaAssignments: SurfaceVertexCriteriaAssignment = None, 
                 mainSecondaryAssignments: MainSecondaryAssignment = None, 
                 initializationAssignments: InitializationAssignment = None, 
                 stabilizationAssignments: StabilizationAssignment = None, 
                 smoothingAssignments: SmoothingAssignment = None, 
                 slidingTransitionAssignments: SlidingTransitionAssignments = None, 
                 slidingFormulationAssignments: SlidingFormulationAssignment = None):
        """This method creates a ContactStd object.

        Path
        ----
            - mdb.models[name].ContactStd

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which this contact interaction is created. 
        useAllstar
            A Boolean specifying whether the contacting surface pairs consist of all exterior faces 
            in the model. 
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically 
            applied to all eligible surfaces. The default value is ON. 
        includedPairs
            A RegionPairs object specifying the domain pairs included in contact. 
        excludedPairs
            A RegionPairs object specifying the domain pairs excluded from contact. 
        contactPropertyAssignments
            A ContactPropertyAssignment object specifying the contact property assignments in the 
            contact domain. 
        surfaceThicknessAssignments
            A SurfaceThicknessAssignment object specifying the surface thickness assignments in the 
            contact domain. 
        surfaceOffsetAssignments
            A SurfaceOffsetAssignment object specifying the surface offset fraction assignments in 
            the contact domain. 
        surfaceFeatureAssignments
            A SurfaceFeatureAssignment object specifying the surface feature angle assignments in 
            the contact domain. 
        surfaceBeamSmoothingAssignments
            A SurfaceBeamSmoothingAssignment object specifying the surface beam smoothing 
            assignments in the contact domain. 
        surfaceVertexCriteriaAssignments
            A SurfaceVertexCriteriaAssignment object specifying the surface vertex criteria 
            assignments in the contact domain. 
        mainSecondaryAssignments
            A MainSecondaryAssignment object specifying the main-secondary assignments in the 
            contact domain. 
        initializationAssignments
            An InitializationAssignment object specifying the contact initialization assignments in 
            the contact domain. 
        stabilizationAssignments
            A StabilizationAssignment object specifying the contact stabilization assignments in the 
            contact domain. 
        smoothingAssignments
            A SmoothingAssignment object specifying the surface smoothing assignments in the contact 
            domain. 
        slidingTransitionAssignments
            A SlidingTransitionAssignments object specifying the sliding transition assignments in 
            the contact domain. 
        slidingFormulationAssignments
            A SlidingFormulationAssignment object specifying the sliding formulation assignments in 
            the contact domain. 

        Returns
        -------
            A ContactStd object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    @typing.overload
    def __init__(self, name: str, createStepName: str, globalSmoothing: Boolean = ON, 
                 surfaceBeamSmoothingAssignments: tuple = (), 
                 surfaceVertexCriteriaAssignments: typing.Union[SymbolicConstant,float] = None, 
                 slidingFormulationAssignments: SymbolicConstant = None, useAllstar: Boolean = OFF, 
                 includedPairs: SymbolicConstant = None, excludedPairs: SymbolicConstant = None, 
                 contactPropertyAssignments: SymbolicConstant = None, 
                 surfaceFeatureAssignments: typing.Union[SymbolicConstant,float] = None, 
                 surfaceThicknessAssignments: typing.Union[SymbolicConstant,float] = None, 
                 surfaceOffsetAssignments: typing.Union[SymbolicConstant,float] = None, 
                 mainSecondaryAssignments: SymbolicConstant = None, 
                 initializationAssignments: SymbolicConstant = None, 
                 stabilizationAssignments: SymbolicConstant = None, 
                 smoothingAssignments: SymbolicConstant = None, 
                 slidingTransitionAssignments: SymbolicConstant = None):
        """This method creates a ContactStd object.

        Path
        ----
            - mdb.models[name].ContactStd

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which this contact interaction is created. 
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically 
            applied to all eligible surfaces. The default value is ON. 
        surfaceBeamSmoothingAssignments
            A sequence of tuples specifying the surface beam smoothing assignments. Each tuple 
            contains two entries: 
            - A region object specifying the surface to which the smoothing is assigned. 
            - A Float specifying the surface smoothing value to be used for the surface. 
        surfaceVertexCriteriaAssignments
            A sequence of tuples specifying the surface vertex criteria assignments. Each tuple 
            contains two entries: 
            - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to 
            which the vertex criteria is assigned. 
            - A Float or a SymbolicConstant specifying the vertex criteria value to be used for the 
            surface. Possible values of the SymbolicConstant are ALL_VERTICES or NO_VERTICES. 
        slidingFormulationAssignments
            A sequence of tuples specifying the sliding formulation assignments. Each tuple contains 
            two entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the 
            sliding formulation attribute is assigned. 
            - A SymbolicConstant specifying the overriding the smoothness value to be used for the 
            first surface. Possible values of the SymbolicConstant are NONE and SMALL_SLIDING. 
        useAllstar
            A Boolean specifying whether the contacting surface pairs consist of all exterior faces 
            in the model. 
        includedPairs
            A sequence of pairs of Region objects or SymbolicConstants that specifies the surface 
            pairs in contact. Possible values of the SymbolicConstants are ALLSTAR and SELF. This 
            argument is valid only when *useAllstar*=OFF. 
        excludedPairs
            A sequence of pairs of Region objects or SymbolicConstants that specifies the surface 
            pairs excluded from contact. Possible values of the SymbolicConstants are ALLSTAR and 
            SELF. 
        contactPropertyAssignments
            A sequence of tuples specifying the properties assigned to each surface pair. Each tuple 
            contains three entries: 
            - A Region object or the SymbolicConstant GLOBAL. 
            - A Region object or the SymbolicConstant SELF. 
            - A String specifying an InteractionProperty object associated with this pair of 
            regions. 
        surfaceFeatureAssignments
            A sequence of tuples specifying the surface feature angle assignments in the contact 
            domain. Each tuple contains two entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the 
            surface feature angle is assigned. 
            - A Float or a SymbolicConstant specifying the overriding feature angle value to be used 
            in the contact definition. Possible values of the SymbolicConstant are PERIMETER or 
            NONE. 
        surfaceThicknessAssignments
            A sequence of tuples specifying the surface thickness assignments in the contact domain. 
            Each tuple contains three entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the 
            surface thickness is assigned. 
            - A Float or a SymbolicConstant specifying the overriding thickness value to be used in 
            the contact definition. The SymbolicConstant ORIGINAL may be specified instead of a 
            floating point value. 
            - A Float specifying a scale factor that multiplies the thickness value specified in the 
            second entry. 
        surfaceOffsetAssignments
            A sequence of tuples specifying the surface offset fraction assignments in the contact 
            domain. Each tuple contains two entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the 
            surface offset fraction is assigned. 
            - A Float or a SymbolicConstant specifying the offset fraction value to be used in the 
            contact definition. Possible values of the SymbolicConstant are ORIGINAL, SPOS, or SNEG. 
        mainSecondaryAssignments
            A sequence of tuples specifying main-secondary assignments in the contact domain. Each 
            tuple contains three entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the first surface that 
            defines the main-secondary assignment. 
            - A region object specifying the second surface in the main-secondary assignment 
            definition. 
            - A SymbolicConstant specifying the status of the first surface. Possible values are 
            MAIN, SECONDARY, and BALANCED. 
        initializationAssignments
            A sequence of tuples specifying the contact initialization data assigned to each surface 
            pair. Each tuple contains three entries: 
            - A Region object or the SymbolicConstant GLOBAL. 
            - A Region object or the SymbolicConstant SELF. 
            - A String specifying a StdStabilization object associated with this pair of regions. 
        stabilizationAssignments
            A sequence of tuples specifying the contact stabilization assigned to each surface pair. 
            Each tuple contains three entries: 
            - A Region object or the SymbolicConstant GLOBAL. 
            - A Region object or the SymbolicConstant SELF. 
            - A String specifying a StdStabilization object associated with this pair of regions. 
        smoothingAssignments
            A sequence of tuples specifying the surface smoothing assignments in the contact domain. 
            Each tuple contains two entries: 
            - A region object specifying the surface to which the smoothing option is assigned. 
            - A SymbolicConstant specifying the smoothing option to be used in the contact 
            definition. Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, or 
            TOROIDAL. 
        slidingTransitionAssignments
            A sequence of tuples specifying sliding transition assignments in the contact domain. 
            Each tuple contains three entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the first surface that 
            defines the sliding transition assignment. 
            - A region object specifying the second surface in the sliding transition assignment 
            definition. 
            - A SymbolicConstant specifying the smoothness value. Possible values are 
            ELEMENT_ORDER_SMOOTHING, LINEAR_SMOOTHING, and QUADRATIC_SMOOTHING. 

        Returns
        -------
            A ContactStd object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def __init__(self, *args, **kwargs):
        pass

