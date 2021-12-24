

class DataTable:

    """The DataTable object is used to specify the parameter table of the respective parameter 
    table type. 
    The data type of the values in each column in the DataTable object corresponds to the 
    data type mentioned for the respective ParameterColumn object. The DataTable object 
    should be created when all the required ParameterColumn objects are created for the 
    current ParameterTable. 

    Access
    ------
        - mdb.models[name].tableCollections[name].parameterTables[name].dataTables[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - *PARAMETER TABLE

    """

    # A String specifying the label of the data table. 
    label: str = ''

    # A DataColumnArray specifying all the dataColumns in the DataTable object. 
    columns: str = ''

    def __init__(self, label: str):
        """This method creates a DataTable object and places it in the dataTables array.

        Path
        ----
            - mdb.models[name].tableCollections[name].parameterTables[name].DataTable

        Parameters
        ----------
        label
            A String specifying a unique label name for the current ParameterTable object. 

        Returns
        -------
            A DataTable object. 

        Exceptions
        ----------
            AbaqusException. 
        """
        pass

