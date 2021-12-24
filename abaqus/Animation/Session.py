from ..Session.Session import Session as BaseSession
from abaqusConstants import *

class Session(BaseSession):
    """The following commands operate on Session objects. For more information about the 
    Session object, see Session object. 

    Access
    ------
        - import animation

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def writeImageAnimation(self, fileName: str, format: SymbolicConstant, canvasObjects: tuple = ()):
        """This method writes the animations present in the list of canvas objects to a file. It
        generates an animation file using the given file name and file format and uses the
        values in the appropriate options object.

        Parameters
        ----------
        fileName
            A String specifying the name of the animation file to generate. 
        format
            A SymbolicConstant specifying the format of the generated file. Possible values are AVI, 
            QUICKTIME, VRML, and COMPRESSED_VRML. 
        canvasObjects
            A sequence specifying the canvas objects to capture. The default behavior is to capture 
            all canvas objects. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

