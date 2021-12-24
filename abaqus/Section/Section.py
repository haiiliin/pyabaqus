

class Section:

    """The Section object defines the properties of a section. The Section object is the 
    abstract base type for other Section objects. The Section object has no explicit 
    constructor. The methods and members of the Section object are common to all objects 
    derived from the Section. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name]
        - import odbSection
        - session.odbs[name].sections[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. 
    name: str = ''

    def sectionsFromOdb(self, fileName: str):
        """This method creates Section objects by reading an output database. The new sections are
        placed in the sections repository.

        Path
        ----
            - mdb.models[*name*].sectionsFromOdb

        Parameters
        ----------
        fileName
            A String specifying the name of the output database file (including the .odb extension) 
            to be read. This String can also be the full path to the output database file if it is 
            located in another directory. 

        Returns
        -------
            A list of Section objects. 

        Exceptions
        ----------
            None. 
        """
        pass

