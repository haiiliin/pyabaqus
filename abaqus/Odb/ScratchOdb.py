from .Odb import Odb


class ScratchOdb:
    """A scratch output database is associated with an open output database and is used to
    store session-related, non-persistent objects, such as Step, Frame and FieldOutput 
    objects. Abaqus creates a scratch output database when needed for these non-persistent 
    objects during an Abaqus/CAE session. Abaqus deletes the scratch output database when 
    the associated output database is closed. 

    Access
    ------
        - import odbAccess
        - session.scratchOdbs[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def __init__(self, odb: Odb):
        """This method creates a new ScratchOdb object.

        Path
        ----
            - session.ScratchOdb

        Parameters
        ----------
        odb
            An Odb object specifying the output database with which to associate. 

        Returns
        -------
            A ScratchOdb object. 

        Exceptions
        ----------
            None. 
        """
        pass
