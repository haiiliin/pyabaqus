# PropertyTableData object

A PropertyTableData is an object that is used to specify the property table of the respective property table type.

The values in each column in the PropertyTableData object corresponds to the properties and variables mentioned in the PropertyTable object.

## Access

```
mdb.models[name].tableCollections[name].propertyTables[name].propertyTableDatas[name]
```

## PropertyTableData(...)



This method creates a PropertyTableData object.



### Path

```
mdb.models[name].tableCollections[name].propertyTables[name].PropertTableData
```

### Optional arguments

- *label*

  A String specifying a unique label name for the current PropertyTable object.

- *regularize*

  A SymbolicConstant specifying the type of regularize to the user-defined property data.

- *extrapolate*

  A SymbolicConstant specifying the type of extrapolation of dependent variables outside the specified range of the independent variables.

- *isTemp*

  A Boolean specifying the dependency of properties on temperature.

- *fieldNums*

  An Int specifying the field variables on which properties are dependent.

- *regularizeTolerance*

  A Double specifying the tolerance to be used to regularize the property table data.

- *data*

  An Array of doubles specifying the values of the properties, the variables mentioned in PropertyTable, and the field variables mentioned in PropertyTableData.

### Return value

A PropertyTableData object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the PropertyTableData object.



### Exceptions

RangeError.



## Members

The PropertyTableData object has members with the same names and descriptions as the arguments to the [PropertyTableData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-propertytabledatapyc.htm?ContextScope=all#simaker-propertytabledatapropertytabledatapyc) method.



## Corresponding analysis keywords

- [PROPERTY TABLE TYPE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-propertytabletype.htm?ContextScope=all#simakey-r-propertytabletype)
- [PROPERTY TABLE](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-propertytable.htm?ContextScope=all#simakey-r-propertytable)