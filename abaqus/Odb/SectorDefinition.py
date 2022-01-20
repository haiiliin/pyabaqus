class SectorDefinition:
    """The SectorDefinition object describes the number of symmetry sectors and axis of
    symmetry for a cyclic symmetry model. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].sectorDefinition

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # An Int specifying the number of sectors in the cyclic symmetry model. 
    numSectors: int = None

    # A tuple of tuples of Floats specifying the coordinates of two points on the axis of 
    # symmetry. 
    symmetryAxis: float = None
