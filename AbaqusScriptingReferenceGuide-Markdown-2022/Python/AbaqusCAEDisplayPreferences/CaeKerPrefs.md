# CaeKerPrefs object

The CaeKerPrefs object contains the details of the sessionOptions.

## Access

```
import caePrefsAccess
caePrefsAccess.openSessionOptions(...)
```

## save(...)



This method saves the sessionOptions in the current *fileName*.



### Required arguments

None.

### Optional arguments

- *backupFile*

  A Boolean specifying whether save a numbered backup copy of the preferences file, *fileName*. Default is True.

### Return value

None.

### Exceptions

None.



## saveAs(...)



This method saves the sessionOptions to the specified location.



### Required arguments

- *fileName*

  A String specifying the path to the preferences file.

- *directory*

  A SymbolicConstant specifying the location of the preferences file. Possible values are:CURRENT to open the preferences file in the current directory (caePrefsAccess.CURRENT)HOME to open the preferences file in your home directory (caePrefsAccess.HOME)The default value is HOME. Either *fileName* or *directory* must be supplied. The *fileName* or *directory* arguments are mutually exclusive.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The CaeKerPrefs object has the following member:

- *fileName*

  A String specifying the path to the preferences file that the CaeKerPrefs object represents.