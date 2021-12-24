

class TableCollection:

    """A TableCollection is an object used to define the containers that encapsulate the 
    ParameterTable and PropertyTable objects. 

    Access
    ------
        - mdb.models[name].tableCollections[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - *TABLE COLLECTION

    """

    # A repository of the PropertyTable object. 
    propertyTables: str = ''

    # A repository of the ParameterTable object 
    parameterTables: str = ''

    def __init__(self, name: str):
        """This method creates a TableCollection object and places it in the tableCollections
        repository.

        Path
        ----
            - mdb.models[name].TableCollection

        Parameters
        ----------
        name
            A String specifying the repository key. 

        Returns
        -------
            A TableCollection object. 

        Exceptions
        ----------
            None. 
        """
        pass

