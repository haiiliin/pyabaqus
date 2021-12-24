# TableCollection object

A TableCollection is an object used to define the containers that encapsulate the ParameterTable and PropertyTable objects.

## Access

```
mdb.models[name].tableCollections[name]
```

## TableCollection(...)

This method creates a TableCollection object and places it in the tableCollections repository.

### Path

```
mdb.models[name].TableCollection
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

None.

### Return value

A TableCollection object.

### Exceptions

None.



## Members

The TableCollection object has the following members:

- *propertyTables*

  A repository of the PropertyTable object.

- *parameterTables*

  A repository of the ParameterTable object



## Corresponding analysis keywords

- [*TABLE COLLECTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-tablecollection.htm?ContextScope=all#simakey-r-tablecollection)