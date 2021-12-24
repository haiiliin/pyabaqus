# DataTable object

The DataTable object is used to specify the parameter table of the respective parameter table type.

The data type of the values in each column in the DataTable object corresponds to the data type mentioned for the respective [ParameterColumn](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-parameterColumnpyc.htm?ContextScope=all#simaker-c-parameterColumnpyc) object. The DataTable object should be created when all the required ParameterColumn objects are created for the current ParameterTable.

## Access

```
mdb.models[name].tableCollections[name].parameterTables[name].dataTables[i]
```

## DataTable(...)

This method creates a DataTable object and places it in the dataTables array.

### Path

```
mdb.models[name].tableCollections[name].parameterTables[name].DataTable
```

### Required arguments

- *label*

  A String specifying a unique label name for the current ParameterTable object.

### Optional arguments

None.

### Return value

A DataTable object.

### Exceptions

AbaqusException.



## Members

The DataTable object has the following members.

- *label*

  A String specifying the label of the data table.

- *columns*

  A DataColumnArray specifying all the dataColumns in the DataTable object.



## Corresponding analysis keywords

- [*PARAMETER TABLE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-parametertable.htm?ContextScope=all#simakey-r-parametertable)