from .NumberFormat import NumberFormat
from abaqusConstants import *

class JournalOptions:

    """A JournalOptions object specifies how to record selection of geometry in the journal and 
    replay files. *journalOptions* can also be used to set the numeric formatting options 
    for field report output, geometry commands output, and a default format for other 
    numeric output. The JournalOptions object has no constructor. Abaqus creates the 
    *journalOptions* member when a session is started. 

    Access
    ------
        - session.journalOptions

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def setValues(self, replayGeometry: SymbolicConstant = COMPRESSEDINDEX, 
                  recoverGeometry: SymbolicConstant = COMPRESSEDINDEX, defaultFormat: NumberFormat = None, 
                  fieldReportFormat: NumberFormat = None, geometryFormat: NumberFormat = None):
        """This method modifies the JournalOptions object.

        Parameters
        ----------
        replayGeometry
            A SymbolicConstant specifying the format of the geometry in the replay file. Possible 
            values are COORDINATE, INDEX, and COMPRESSEDINDEX. The default value is COMPRESSEDINDEX. 
        recoverGeometry
            A SymbolicConstant specifying the format of the geometry in the recovery file. Possible 
            values are COORDINATE, INDEX, and COMPRESSEDINDEX. The default value is COMPRESSEDINDEX. 
        defaultFormat
            A NumberFormat object specifying the default format for numeric output. The default 
            values are the same as the default values for the NumberFormat object. 
        fieldReportFormat
            A NumberFormat object specifying the default format for numbers in a field report 
            output. The default values are the same as the default values for the NumberFormat 
            object. 
        geometryFormat
            A NumberFormat object specifying the default format for numbers in geometry commands 
            output. The default values are the same as the default values for the NumberFormat 
            object. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

