class MdbDataInstance:
    """The MdbDataInstance object instance data. It corresponds to same named part instance
    with a mesh in the cae model. 

    Access
    ------
        - import visualization
        - session.mdbData[name].instances[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the instance name. This attribute is read-only. 
    name: str = ''
