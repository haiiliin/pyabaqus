

class PropertyTable:

    """A PropertyTable is an object that is used to define the container that encapsulates the 
    PropertyTableData object. 
    The data of the PropertyTableData object is dependent on the contents of the 
    PropertyTable object. 
    After PropertyTableDatais instantiated, making changes to PropertyTable may lead to data 
    corruption. 

    Access
    ------
        - mdb.models[name].tableCollections[name].propertyTables[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - PROPERTY TABLE TYPE
        - PROPERTY TABLE

    """

    # A repository of PropertyTableData. Specifies all the propertyTableData in PropertyTable 
    propertyTableDatas: str = ''

    def __init__(self, name: str, properties: str, variables: str = ''):
        """This method creates a PropertyTable object.

        Path
        ----
            - mdb.models[name].tableCollections[name].PropertyTable

        Parameters
        ----------
        name
            A String specifying the repository key. 
        properties
            A string array specifying the multiple properties to build the parameter table type. 
        variables
            A String array specifying multiple independent variables. The default value is an empty 
            array. 

        Returns
        -------
            A PropertyTable object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self, variables: str = ''):
        """This method modifies the PropertyTable object.

        Parameters
        ----------
        variables
            A String array specifying multiple independent variables. The default value is an empty 
            array. 

        Returns
        -------

        Exceptions
        ----------
            RangeError. 
        """
        pass

