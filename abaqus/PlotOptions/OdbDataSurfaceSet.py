

class OdbDataSurfaceSet:

    """The OdbDataSurfaceSet object stores surface set data. 

    Access
    ------
        - import visualization
        - session.odbData[name].surfaceSets[i]

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

    # A String-to-tuple-of-Ints Dictionary specifying the facets corresponding to the 
    # *elements*. This attribute is read-only. 
    facets: str = ''

