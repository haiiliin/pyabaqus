class OdbDataInstance:
    """The OdbDataInstance object instance data.

    Notes
    -----
        This object can be accessed by:
        - import visualization
        - session.odbData[name].instances[i]

    """

    # A String specifying the instance name. This attribute is read-only. 
    name: str = ''
