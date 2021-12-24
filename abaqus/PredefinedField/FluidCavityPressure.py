from ..Region.Region import Region
from .PredefinedField import PredefinedField

class FluidCavityPressure(PredefinedField):

    """The FluidCavityPressure object stores the data for initial fluid cavity pressures. The 
    base class*region* argument can not be specifed with this object. 
    The FluidCavityPressure object is derived from the PredefinedField object. 

    Access
    ------
        - import load
        - mdb.models[name].predefinedFields[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - INITIAL CONDITIONS

    """

    # A Region object on which the *fluidCavity* interaction is specified. 
    region: Region = None

    def __init__(self, name: str, fluidCavity: str, fluidPressure: float):
        """This method creates a FluidCavityPressure object.

        Path
        ----
            - mdb.models[name].FluidCavityPressure

        Parameters
        ----------
        name
            A String specifying the repository key. 
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction. 
        fluidPressure
            A Float specifying the initial fluid pressure. 

        Returns
        -------
            A FluidCavityPressure object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the FluidCavityPressure object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

