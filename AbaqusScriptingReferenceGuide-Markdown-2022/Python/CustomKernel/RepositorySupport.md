# RepositorySupport object

The RepositorySupport is a base class from which you can derive your own classes that are designed to contain custom repositories. Instances of this class can be queried from the GUI and are capable of notifying the GUI when the contents of the instance change.

The RepositorySupport object is derived from the [CommandRegister](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-commandregisterpyc.htm?ContextScope=all) object.

## Access

```
import customKernel
mdb.customData
session.customData
session.odbs[name].customData
```

## RepositorySupport()



This method creates a RepositorySupport object.



### Path

customKernel.RepositorySupport

### Arguments

None.

### Return value

A RepositorySupport object.

### Exceptions

None.



## Repository(...)



This method installs a repository on the class. The repository is an instance of a RegisteredDictionary class. Refer to [RegisteredDictionary](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-registereddictionarypyc.htm?ContextScope=all) for details on its methods.

The objects stored in the repository are assumed to have an attribute called *name* that stores the key used to access the object in the repository. The name attribute will be modified by the changeKey method.



### Required arguments

- *name*

  A String specifying the name of the repository.

- *constructors*

  A constructor or sequence of constructors specifying which classes will store their instances in the repository.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The RepositorySupport object has no members.