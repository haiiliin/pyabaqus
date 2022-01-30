class OdbDataElementSet:
    """The OdbDataElementSet object stores element set data.

    Notes
    -----
        This object can be accessed by:
        - import visualization
        - session.odbData[name].elementSets[i]

    """

    # A String specifying the set name. This attribute is read-only. 
    name: str = ''

    # A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute 
    # is read-only. 
    elements: str = ''
