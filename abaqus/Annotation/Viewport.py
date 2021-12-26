from .Annotation import Annotation
from ..Canvas.Viewport import Viewport as BaseViewport


class Viewport(BaseViewport):
    """The following commands operate on Viewport objects. For more information about the 
    Viewport object, see Viewport object. 

    Access
    ------
        - import annotationToolset

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def plotAnnotation(self, annotation: Annotation, index: str = 0.0):
        """This method plots an Annotation object in aViewport.

        Parameters
        ----------
        annotation
            An Annotation object to plot. 
        index
            An Int specifying the index of the Annotation object in the sequence of annotations to 
            plot. The default value is zero. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

