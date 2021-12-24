from ..Model.Model import Model as BaseModel
from ..Odb.Odb import Odb

class Model(BaseModel):
    """The following commands operate on Model objects. For more information about the Model 
    object, see Model object. 

    Access
    ------
        - import mesh

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def adaptiveRemesh(self, odb: Odb):
        """This method remeshes the model using the active remesh rules in the model and the error
        indicator results from a previous analysis.

        Parameters
        ----------
        odb
            An Odb object containing error output field results. 

        Returns
        -------
            An AdaptivityIteration Object. 

        Exceptions
        ----------
            None. 
        """
        pass

