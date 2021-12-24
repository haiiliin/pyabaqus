

class RigidBodyConstraint:

    """The RigidBodyConstraint object. 

    Access
    ------
        - import visualization
        - session.odbData[name].rigidbodies[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the rigidbody constraint name. This attribute is read-only. 
    name: str = ''

    def constraintData(self):
        """This method returns constraint data if any are associated with the object.

        Parameters
        ----------

        Returns
        -------
            A String Value: NONE in the absence of constraint data. 

        Exceptions
        ----------
            None. 
        """
        pass

