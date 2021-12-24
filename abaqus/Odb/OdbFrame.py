from ..UtilityAndView.Repository import Repository
from .FieldOutput import FieldOutput
from .OdbLoadCase import OdbLoadCase
from abaqusConstants import *

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
    fieldOutputs: Repository[str, FieldOutput] = None

    # An OdbLoadCase object specifying the load case for the frame. 
    loadCase: OdbLoadCase = None

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

