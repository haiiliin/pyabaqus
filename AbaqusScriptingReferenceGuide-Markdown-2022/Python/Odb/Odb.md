# Odb object

The Odb object is the in-memory representation of an output database (ODB) file.

## Access

```
import odbAccess
session.odbs[name]
```

## Odb(...)



This method creates a new Odb object.



### Path

```
session.Odb
```

### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *analysisTitle*

  A String specifying the title of the output database. The default value is an empty string.

- *description*

  A String specifying the description of the output database. The default value is an empty string.

- *path*

  A String specifying the path to the file where the new output database (.odb ) file will be written. The default value is an empty string.

### Return value

An Odb object.

### Exceptions

None.



## close()



This method closes an output database.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## getFrame(...)



This method returns the frame at the specified time, frequency, or mode. It will not interpolate values between frames. The method is not applicable to an Odb object containing steps with different domains or to an Odb object containing a step with load case specific data.



### Required arguments

- *frameValue*

  A Double specifying the value at which the frame is required. *frameValue* can be the total time or frequency.

### Optional arguments

- *match*

  A SymbolicConstant specifying which frame to return if there is no frame at the exact frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is CLOSEST.When *match*=CLOSEST, Abaqus returns the closest frame. If the frame value requested is exactly halfway between two frames, Abaqus returns the frame after the value.When *match*=EXACT, Abaqus raises an exception if the exact frame value does not exist.

### Return value

An [OdbFrame](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?ContextScope=all) object.

### Exceptions

- If the exact frame is not found:

  OdbError: Frame not found.



## save()



This method saves output to an output database (.odb ) file.



### Arguments

None.

### Return value

None.

### Exceptions

- OdbError

  Database save failed. The database was opened as read-only. Modification of data is not permitted.



## update()



This method is used to update an Odb object in memory while an Abaqus analysis writes data to the associated output database. update checks if additional steps have been written to the output database since it was opened or last updated. If additional steps have been written to the output database, update adds them to the Odb object.



### Arguments

None.

### Return value

A Boolean specifying whether additional steps or frames were added to the Odb object.

### Exceptions

None.



## Members

The Odb object has members with the same names and descriptions as the arguments to the [Odb ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?ContextScope=all#simaker-odbodbpyc)method.

In addition, the Odb object can have the following members:

- *isReadOnly*

  A Boolean specifying whether the output database was opened with read-only access.

- *amplitudes*

  A repository of [Amplitude](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?ContextScope=all) objects.

- *filters*

  A repository of [Filter](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filterpyc.htm?ContextScope=all) objects.

- *rootAssembly*

  An [OdbAssembly](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbassemblypyc.htm?ContextScope=all) object.

- *jobData*

  A [JobData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobdatapyc.htm?ContextScope=all) object.

- *parts*

  A repository of [OdbPart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpartpyc.htm?ContextScope=all) objects.

- *materials*

  A repository of [Material](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialpyc.htm?ContextScope=all) objects.

- *steps*

  A repository of [OdbStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsteppyc.htm?ContextScope=all) objects.

- *sections*

  A repository of [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) objects.

- *sectionCategories*

  A repository of [SectionCategory](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectioncategorypyc.htm?ContextScope=all) objects.

- *sectorDefinition*

  A [SectorDefinition](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectordefinitionpyc.htm?ContextScope=all) object.

- *userData*

  A [UserData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-userdatapyc.htm?ContextScope=all) object.

- *customData*

  A [RepositorySupport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-repositorysupportpyc.htm?ContextScope=all) object.

- *profiles*

  A repository of [Profile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-profilepyc.htm?ContextScope=all) objects.