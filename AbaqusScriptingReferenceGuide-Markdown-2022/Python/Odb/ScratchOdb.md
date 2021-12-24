# ScratchOdb object

A scratch output database is associated with an open output database and is used to store session-related, non-persistent objects, such as Step, Frame and [FieldOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?ContextScope=all) objects. Abaqus creates a scratch output database when needed for these non-persistent objects during an Abaqus/CAE session. Abaqus deletes the scratch output database when the associated output database is closed.

## Access

```
import odbAccess
session.scratchOdbs[name]
```

## ScratchOdb(...)



This method creates a new ScratchOdb object.



### Path

```
session.ScratchOdb
```

### Required arguments

- *odb*

  An [Odb](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?ContextScope=all) object specifying the output database with which to associate.

### Optional arguments

None.

### Return value

A ScratchOdb object.

### Exceptions

None.



## Members

The ScratchOdb object has no members.