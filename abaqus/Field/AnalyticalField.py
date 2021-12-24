from .Field import Field

class AnalyticalField(Field):

    """The AnalyticalField object is the abstract base type for other AnalyticalField objects. 
    The AnalyticalField object has no explicit constructor. The methods and members of the 
    AnalyticalField object are common to all objects derived from the AnalyticalField. 
    The AnalyticalField object is derived from the Field object. 

    Access
    ------
        - import fields
        - mdb.models[name].analyticalFields[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. 
    name: str = ''

    # None or a DatumCsys object specifying the local coordinate system of the field. If 
    # *localCsys*=None, the field is defined in the global coordinate system. The default 
    # value is None. 
    localCsys: str = None

    # A String specifying the description of the field. The default value is an empty string. 
    description: str = ''

