from .ContactPropertyAssignment import ContactPropertyAssignment
from .Interaction import Interaction
from .MainSecondaryAssignment import MainSecondaryAssignment
from .RegionPairs import RegionPairs
from .SmoothingAssignment import SmoothingAssignment
from .SurfaceFeatureAssignment import SurfaceFeatureAssignment
from .SurfaceOffsetAssignment import SurfaceOffsetAssignment
from .SurfaceThicknessAssignment import SurfaceThicknessAssignment
from abaqusConstants import *
import typing

class ContactExp(Interaction):

    """The ContactExp object defines the contact domain and associated properties during 
    contact in an Abaqus/Explicit analysis. 
    The ContactExp object is derived from the Interaction object. 

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

    # A SurfaceFeatureAssignment object specifying the surface feature angle assignments in 
    # the contact domain. 
    surfaceFeatureAssignments: SurfaceFeatureAssignment = None

    # A SmoothingAssignment object specifying the surface smoothing assignments in the contact 
    # domain. 
    smoothingAssignments: SmoothingAssignment = None

    # A MainSecondaryAssignment object specifying the main-secondary assignments in the 
    # contact domain. 
    mainSecondaryAssignments: MainSecondaryAssignment = None

    # A PolarityAssignment object specifying the polarity assignments in the contact domain. 
    polarityAssignments: PolarityAssignment = None

    def __init__(self, name: str, createStepName: str, globalSmoothing: Boolean = ON, 
                 surfaceCrushTriggerAssignments: typing.Union[SymbolicConstant, float] = None, 
                 surfaceFrictionAssignments: typing.Union[SymbolicConstant, float] = None, 
                 useAllstar: Boolean = OFF, includedPairs: SymbolicConstant = None, 
                 excludedPairs: SymbolicConstant = None, 
                 contactPropertyAssignments: SymbolicConstant = None, 
                 surfaceThicknessAssignments: typing.Union[SymbolicConstant, float] = None, 
                 surfaceOffsetAssignments: typing.Union[SymbolicConstant, float] = None, 
                 surfaceFeatureAssignments: typing.Union[SymbolicConstant, float] = None, 
                 smoothingAssignments: SymbolicConstant = None, 
                 mainSecondaryAssignments: SymbolicConstant = None, 
                 polarityAssignments: SymbolicConstant = None):
        """This method creates a ContactExp object.

        Path
        ----
            - mdb.models[name].ContactExp

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which this contact interaction is created. 
        globalSmoothing
            A Boolean specifying whether surface smoothing (geometric correction) is automatically 
            applied to all eligible surfaces. The default value is ON. 
        surfaceCrushTriggerAssignments
            A sequence of tuples specifying the surface crush trigger assignments. Each tuple 
            contains four entries: 
            - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to 
            which the feature angle is assigned. 
            - A SymbolicConstant specifying the trigger option to be used for the surface. Possible 
            values of the SymbolicConstant are TRIGGER, NO_TRIGGER, or NO_CRUSH. 
            - A Float specifying the crush stress value to be used for the surface. 
            - A Float specifying the crush initiation angle value to be used for the surface. 
            - A Float specifying the crush continuation angle value to be used for the surface. 
        surfaceFrictionAssignments
            A sequence of tuples specifying the surface friction assignments. Each tuple contains 
            two entries: 
            - A region or a material object or the SymbolicConstant GLOBAL specifying the surface to 
            which the friction coefficient is assigned. 
            - A Float specifying the overriding friction coefficient to be used in the contact 
            definition. 
        useAllstar
            A Boolean specifying whether the contacting surface pair consists of all exterior faces, 
            shell edges, beam segments, analytical rigid surfaces, and, when applicable, Eulerian 
            material surfaces. 
        includedPairs
            A sequence of pairs of Region objects or SymbolicConstants that specifies the surface 
            pairs in contact. Possible values of the SymbolicConstants are ALLSTAR and SELF. This 
            argument is valid only when *useAllstar*=OFF. 
        excludedPairs
            A sequence of pairs of Region objects or SymbolicConstants that specify the surface 
            pairs excluded from contact. Possible values of the SymbolicConstants are ALLSTAR and 
            SELF. 
        contactPropertyAssignments
            A sequence of tuples specifying the properties assigned to each surface pair. Each tuple 
            contains three entries: 
            - A Region object or the SymbolicConstant GLOBAL. 
            - A Region object or the SymbolicConstant SELF. 
            - A String specifying an InteractionProperty object associated with this pair of 
            regions. 
        surfaceThicknessAssignments
            A sequence of tuples specifying the surface thickness assignments in the contact domain. 
            Each tuple contains three entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the 
            surface thickness is assigned. 
            - A Float or a SymbolicConstant specifying the overriding thickness value to be used in 
            the contact definition. Possible values of the SymbolicConstant are ORIGINAL or 
            THINNING. 
            - A Float specifying a scale factor that multiplies the thickness value specified in the 
            second entry. 
        surfaceOffsetAssignments
            A sequence of tuples specifying the surface offset fraction assignments in the contact 
            domain. Each tuple contains two entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the 
            surface offset fraction is assigned. 
            - A Float or a SymbolicConstant specifying the offset fraction value to be used in the 
            contact definition. Possible values of the SymbolicConstant are ORIGINAL, SPOS, or SNEG. 
        surfaceFeatureAssignments
            A sequence of tuples specifying the surface feature angle assignments in the contact 
            domain. Each tuple contains two entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the surface to which the 
            surface feature angle is assigned. 
            - A Float or a SymbolicConstant specifying the overriding feature angle value to be used 
            in the contact definition. Possible values of the SymbolicConstant are PERIMETER, ALL, 
            PICKED, or NONE. 
        smoothingAssignments
            A sequence of tuples specifying the surface smoothing assignments in the contact domain. 
            Each tuple contains two entries: 
            - A region object specifying the surface to which the smoothing option is assigned. 
            - A SymbolicConstant specifying the smoothing option to be used in the contact 
            definition. Possible values of the SymbolicConstant are NONE, REVOLUTION, SPHERICAL, or 
            TOROIDAL. 
        mainSecondaryAssignments
            A sequence of tuples specifying pure main-secondary assignments in the contact domain. 
            Each tuple contains three entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the first surface that 
            defines the main-secondary assignment. 
            - A region object specifying the second surface in the main-secondary assignment 
            definition. 
            - A SymbolicConstant specifying the status of the first surface. Possible values are 
            MAIN and SECONDARY. 
        polarityAssignments
            A sequence of tuples specifying polarity assignments in the contact domain. Each tuple 
            contains three entries: 
            - A region object or the SymbolicConstant GLOBAL specifying the first surface that 
            defines the polarity assignment. 
            - A region object specifying the second surface in the polarity assignment definition. 
            - A SymbolicConstant specifying the polarity of the second surface. Possible values are 
            SPOS, SNEG, and TWO_SIDED. 

        Returns
        -------
            A ContactExp object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

