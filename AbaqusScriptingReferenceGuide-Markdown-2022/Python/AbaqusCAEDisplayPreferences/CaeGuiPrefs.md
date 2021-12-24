# CaeGuiPrefs object

The CaeGuiPrefs object contains the details of the graphical preferences in a guiPreferences section of the abaqus_2021.gpr file.

## Access

```
import caePrefsAccess
caePrefsAccess.openGuiPreferences(...)
```

## save(...)



This method saves the guiPreferences section specified in the current *fileName*.



### Required arguments

None.

### Optional arguments

- *backupFile*

  A Boolean specifying whether Abaqus should save a numbered backup copy of the preferences file, *fileName*. Default is True.

### Return value

None.

### Exceptions

None.



## saveAs(...)



This method saves the guiPreferences settings to the specified location.



### Required arguments

- *fileName*

  A String specifying the path to the preferences file.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The CaeGuiPrefs object has the following member:

- *fileName*

  A String specifying the path to the preferences file.