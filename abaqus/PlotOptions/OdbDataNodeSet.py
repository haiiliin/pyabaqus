class OdbDataNodeSet:
    """The OdbDataNodeSet object stores node set data.

    Access
    ------
        - import visualization
        - session.odbData[name].nodeSets[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the set name. This attribute is read-only. 
    name: str = ''

    # A String-to-tuple-of-Ints Dictionary specifying the nodes in the set. This attribute is 
    # read-only. 
    nodes: str = ''
