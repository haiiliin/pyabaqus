from abaqusConstants import *


class ConstrainedSketchVertexArray:
    """The ConstrainedSketchVertexArray is a sequence of ConstrainedSketchVertex objects.

    Access
    ------
        - import sketch
        - mdb.models[name].sketches[name].vertices[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def findAt(self, coordinates: tuple, printWarning: Boolean = True):
        """This method returns the ConstrainedSketchVertex located at the given coordinates.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the *X*- and *Y*-coordinates of the object to find. 
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found 
            at the specified location. The default value is True. 

        Returns
        -------
            A ConstrainedSketchVertex object. 

        Exceptions
        ----------
            None. 
        """
        pass
