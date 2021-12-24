

class ParameterTable:

    """A ParameterTable is an object that is used to define the containers that encapsulate 
    ParameterColumn and DataTable objects. The data of DataTable is dependent on the 
    contents of ParameterColumn. After DataTable is instantiated, making changes to 
    ParameterColumn may lead to data corruption. 

    Access
    ------
        - mdb.models[name].tableCollections[name].parameterTables[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - *PARAMETER TABLE TYPE
        - *PARAMETER TABLE

    """

    # A ParameterColumnArray specifying all the columns in the ParameterTable. 
    columns: str = ''

    # A DataTableArray specifying all the dataTables in the ParameterTable. 
    dataTables: str = ''

    def __init__(self, name: str):
        """This method creates a ParameterTable object and places it in the parameterTables
        repository.

        Path
        ----
            - mdb.models[name]tableCollections[name].ParameterTable

        Parameters
        ----------
        name
            A String specifying the repository key. 

        Returns
        -------
            A ParameterTable object. 

        Exceptions
        ----------
            None. 
        """
        pass

