

class EventSeriesType:

    """The EventSeriesType object is used to define a type of event in a process. 

    Access
    ------
        - mdb.models[name].eventSeriesTypes[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - EVENT SERIES TYPE
        - EVENT SERIES

    """

    def __init__(self, name: str, createStepName: str, fields: str = ''):
        """This method creates an EventSeriesType object.

        Path
        ----
            - mdb.models[name].EventSeriesType

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A string specifying the step name. 
        fields
            A String array specifying fields. The default value is an empty array. 

        Returns
        -------
            A EventSeriesType object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self, fields: str = ''):
        """This method modifies the EventSeriesType object.

        Parameters
        ----------
        fields
            A String array specifying fields. The default value is an empty array. 

        Returns
        -------

        Exceptions
        ----------
            RangeError. 
        """
        pass

