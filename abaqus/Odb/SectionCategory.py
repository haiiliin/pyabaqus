from .SectionPointArray import SectionPointArray

class SectionCategory:

    """The SectionCategory object is used to group regions of the model with like sections. 
    Section definitions that contain the same number of section points or integration points 
    are grouped together. 
    To access data for a particular section definition, use the individual Section objects 
    in the output database. For more information, see Beam Section profile commands and 
    Section commands. 

    Access
    ------
        - import
        - odbAccess
        - session.odbs[name].parts[name].elements[i].sectionCategory
        - session.odbs[name].parts[name].elementSets[name].elements[i].sectionCategory
        - session.odbs[name].parts[name].nodeSets[name].elements[i].sectionCategory
        - session.odbs[name].parts[name].surfaces[name].elements[i].sectionCategory
        - session.odbs[name].rootAssembly.elements[i].sectionCategory
        - session.odbs[name].rootAssembly.elementSets[name].elements[i].sectionCategory
        - session.odbs[name].rootAssembly.instances[name].elements[i].sectionCategory
        - session.odbs[name].rootAssembly.instances[name].elementSets[name].elements[i].sectionCategory
        - session.odbs[name].rootAssembly.instances[name].nodeSets[name].elements[i].sectionCategory
        - session.odbs[name].rootAssembly.instances[name].surfaces[name].elements[i].sectionCategory
        - session.odbs[name].rootAssembly.nodeSets[name].elements[i].sectionCategory
        - session.odbs[name].rootAssembly.surfaces[name].elements[i].sectionCategory
        - session.odbs[name].sectionCategories[name]
        - session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elements[i].sectionCategory
        - session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name].elements[i].sectionCategory
        - session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].elements[i].sectionCategory
        - session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].elements[i].sectionCategory

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SectionPointArray object. 
    sectionPoints: SectionPointArray = None

    def __init__(self, name: str, description: str):
        """This method creates a SectionCategory object.

        Path
        ----
            - session.odbs[*name*].SectionCategory

        Parameters
        ----------
        name
            A String specifying the name of the category. 
        description
            A String specifying the description of the category. 

        Returns
        -------
            A SectionCategory object. 

        Exceptions
        ----------
            None. 
        """
        pass

