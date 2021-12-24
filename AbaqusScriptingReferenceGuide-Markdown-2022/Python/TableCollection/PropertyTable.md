# PropertyTable object

A PropertyTable is an object that is used to define the container that encapsulates the PropertyTableData object.

The data of the PropertyTableData object is dependent on the contents of the PropertyTable object.

After PropertyTableDatais instantiated, making changes to PropertyTable may lead to data corruption.

## Access

```
mdb.models[name].tableCollections[name].propertyTables[name]
```

## PropertyTable(...)



This method creates a PropertyTable object.



### Path

```
mdb.models[name].tableCollections[name].PropertyTable
```

### Required arguments

- *name*

  A String specifying the repository key.

- *properties*

  A string array specifying the multiple properties to build the parameter table type.

### Optional arguments

- *variables*

  A String array specifying multiple independent variables. The default value is an empty array.

### Return value

A PropertyTable object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the PropertyTable object.



### Optional arguments

The optional arguments to setValues are the same as the arguments to the [PropertyTable](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-propertytabletypepyc.htm?ContextScope=all#simaker-propertytabletypepropertytabletypepyc) method, except for the *name* argument.

### Exceptions

RangeError.



## Members

The PropertyTableType object has members with the same names and descriptions as the arguments to the [PropertyTable](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-propertytabletypepyc.htm?ContextScope=all#simaker-propertytabletypepropertytabletypepyc) method.

In addition, the PropertyTable object has following members:

- *propertyTableDatas*

  A repository of [PropertyTableData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-propertytabledatapyc.htm?ContextScope=all#simaker-c-propertytabledatapyc). Specifies all the propertyTableData in PropertyTable



## Corresponding analysis keywords

- [PROPERTY TABLE TYPE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-propertytabletype.htm?ContextScope=all#simakey-r-propertytabletype)
- [PROPERTY TABLE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-propertytable.htm?ContextScope=all#simakey-r-propertytable)