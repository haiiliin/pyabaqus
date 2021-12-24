# ParameterTable object

A ParameterTable is an object that is used to define the containers that encapsulate ParameterColumn and DataTable objects. The data of DataTable is dependent on the contents of ParameterColumn. After DataTable is instantiated, making changes to ParameterColumn may lead to data corruption.

## Access

```
mdb.models[name].tableCollections[name].parameterTables[name]
```

## ParameterTable(...)

This method creates a ParameterTable object and places it in the parameterTables repository.

### Path

```
mdb.models[name]tableCollections[name].ParameterTable
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

None.

### Return value

A ParameterTable object.

### Exceptions

None.



## Members

The ParameterTable object has the following members:

- *columns*

  A [ParameterColumnArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-parameterColumnpyc.htm?ContextScope=all#simaker-c-parameterColumnpyc) specifying all the columns in the ParameterTable.

- *dataTables*

  A [DataTableArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-parameterDataTablepyc.htm?ContextScope=all#simaker-c-parameterDataTablepyc) specifying all the dataTables in the ParameterTable.



## Corresponding analysis keywords

- [*PARAMETER TABLE TYPE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-parametertabletype.htm?ContextScope=all#simakey-r-parametertabletype)
- [*PARAMETER TABLE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-parametertable.htm?ContextScope=all#simakey-r-parametertable)