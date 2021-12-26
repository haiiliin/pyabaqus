import typing

from abaqusConstants import *
from .FieldOutput import FieldOutput
from .OdbLoadCase import OdbLoadCase
from ..UtilityAndView.Repository import Repository


class OdbFrame:

    """The domain of the OdbFrame object is taken from the parent step. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].steps[name].frames[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the cyclic mode number associated with the data stored on this frame. 
    # Only frequency analyses of cyclic symmetry models possess cyclic mode numbers. 
    cyclicModeNumber: int = None

    # A SymbolicConstant specifying the domain of the step of which the frame is a member. 
    # Possible values are TIME, FREQUENCY, and MODAL. 
    domain: SymbolicConstant = None

    # A Float specifying the frequency. This member is valid only if *domain*=FREQUENCY or if 
    # the *procedureType* member of the Step object=FREQUENCY. The default value is 0.0. 
    frequency: float = 0

    # An Int specifying the eigenmode. This member is valid only if *domain*=MODAL. 
    mode: int = None

    # An OdbFrame object specifying the real or imaginary portion of the data corresponding to 
    # this cyclic symmetry mode. 
    associatedFrame: 'OdbFrame' = None

    # A repository of FieldOutput objects specifying the key to the *fieldOutputs*repository 
    # is a String representing an output variable. 
    fieldOutputs: Repository[str, FieldOutput] = Repository[str, FieldOutput]()

    # An OdbLoadCase object specifying the load case for the frame. 
    loadCase: OdbLoadCase = OdbLoadCase()

    @typing.overload
    def Frame(self, incrementNumber: int, frameValue: float, description: str = ''):
        """This method creates an OdbFrame object and appends it to the frame sequence.

        Path
        ----
            - session.odbs[name].steps[name].Frame

        Parameters
        ----------
        incrementNumber
            An Int specifying the frame increment number within the step. The base frame has 
            normally increment number 0, and the results run from 1. In case of multiple load cases, 
            the same increment number is duplicated for each loadcase. 
        frameValue
            A Float specifying the value in units determined by the *domain* member of the Step 
            object. The equivalent in the time domain is *stepTime*; in the frequency domain the 
            equivalent is *frequency*; and in the modal domain the equivalent is *mode*. 
        description
            A String specifying the contents of the frame. The default value is an empty string. 

        Returns
        -------
            An OdbFrame object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def Frame(self, mode: int, frequency: float, description: str = ''):
        """This constructor creates an OdbFrame object in the frequency domain and appends it to
        the frame sequence. The arguments to the constructor are valid only when
        *domain*=FREQUENCY or *domain*=MODAL.

        Path
        ----
            - session.odbs[name].steps[name].Frame

        Parameters
        ----------
        mode
            An Int specifying the eigenmode. This member is valid only if *domain*=MODAL. 
        frequency
            A Float specifying the frequency. This member is valid only if *domain*=FREQUENCY or if 
            the *procedureType* member of the Step object=FREQUENCY. The default value is 0.0. 
        description
            A String specifying the contents of the frame. The default value is an empty string. 

        Returns
        -------
            An OdbFrame object. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def Frame(self, loadCase: OdbLoadCase, description: str = '', frequency: float = 0):
        """This constructor creates an OdbFrame object for a specific load case and appends it to
        the frame sequence.

        Path
        ----
            - session.odbs[name].steps[name].Frame

        Parameters
        ----------
        loadCase
            An OdbLoadCase object specifying the load case for the frame. 
        description
            A String specifying the contents of the frame. The default value is an empty string. 
        frequency
            A Float specifying the frequency. This member is valid only if *domain*=FREQUENCY or if 
            the *procedureType* member of the Step object=FREQUENCY. The default value is 0.0. 

        Returns
        -------
            An OdbFrame object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def Frame(self, *args, **kwargs):
        pass

