from abaqusConstants import *


class FreeBody:
    """The FreeBody object defines a section across which resultant forces and moments are
    computed. 

    Access
    ------
        - import visualization
        - session.freeBodies[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def FreeBodyFromEdges(self, name: str, edges: str, summationLoc: SymbolicConstant = CENTROID,
                          summationPoint: tuple = (), componentResolution: SymbolicConstant = NORMAL_TANGENTIAL,
                          csysName: str = ''):
        """This method creates a FreeBody object and places it in the freeBodies repository.

        Path
        ----
            - session.FreeBodyFromEdges

        Parameters
        ----------
        name
            A string name for the free body. 
        edges
            A DisplayGroup leaf object that specifies the physical constituents of the free body. 
        summationLoc
            A SymbolicConstant specifying the location of the summation point. Possible values are 
            CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID. 
        summationPoint
            A tuple of 3 floats specifying the summation point. 
        componentResolution
            A SymbolicConstant specifying the component resolution. Possible values are 
            NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL. 
        csysName
            A string specifying the name of the coordinate system. 

        Returns
        -------
            A FreeBody object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def FreeBodyFromFaces(self, name: str, faces: str, summationLoc: SymbolicConstant = CENTROID,
                          summationPoint: tuple = (), componentResolution: SymbolicConstant = NORMAL_TANGENTIAL,
                          csysName: str = ''):
        """This method creates a FreeBody object and places it in the freeBodies repository.

        Path
        ----
            - session.FreeBodyFromFaces

        Parameters
        ----------
        name
            A string name for the free body. 
        faces
            A DisplayGroup leaf object that specifies the physical constituents of the free body. 
        summationLoc
            A SymbolicConstant specifying the location of the summation point. Possible values are 
            CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID. 
        summationPoint
            A tuple of 3 floats specifying the summation point. 
        componentResolution
            A SymbolicConstant specifying the component resolution. Possible values are 
            NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL. 
        csysName
            A string specifying the name of the coordinate system. 

        Returns
        -------
            A FreeBody object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def FreeBodyFromNodesElements(self, name: str, elements: str, nodes: str, summationLoc: SymbolicConstant = CENTROID,
                                  summationPoint: tuple = (), componentResolution: SymbolicConstant = NORMAL_TANGENTIAL,
                                  csysName: str = ''):
        """This method creates a FreeBody object and places it in the freeBodies repository.

        Path
        ----
            - session.FreeBodyFromNodesElements

        Parameters
        ----------
        name
            A string name for the free body. 
        elements
            A DisplayGroup leaf object that specifies the physical constituents of the free body. 
        nodes
            A DisplayGroup leaf object that specifies the physical constituents of the free body. 
        summationLoc
            A SymbolicConstant specifying the location of the summation point. Possible values are 
            CENTROID, NODAL_AVERAGE and SPECIFY. The default value is CENTROID. 
        summationPoint
            A tuple of 3 floats specifying the summation point. 
        componentResolution
            A SymbolicConstant specifying the component resolution. Possible values are 
            NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL. 
        csysName
            A string specifying the name of the coordinate system. 

        Returns
        -------
            A FreeBody object. 

        Exceptions
        ----------
            None. 
        """
        pass
