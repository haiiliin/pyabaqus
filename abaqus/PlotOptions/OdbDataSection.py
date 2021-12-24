

class OdbDataSection:

    """The OdbDataSection object stores section data. 

    Access
    ------
        - import visualization
        - session.odbData[name].sections[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the set name. This attribute is read-only. 
    name: str = ''

    # A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute 
    # is read-only. 
    elements: str = ''

