# Mdb object

The Mdb object is the high-level Abaqus model database. A model database stores models and analysis controls.

## Access

```
mdb
```

## Mdb(...)



This constructor creates an empty Mdb object.



### Path

```
Mdb
```

### Required arguments

None.

### Optional arguments

- *pathName*

  A String specifying the path to be used when the model database is saved to a file. If you do not provide a file extension, .cae is appended automatically to the path. The default value is an empty string.

### Return value

A Mdb object.

### Exceptions

None.



## importDxf(...)



This method creates a [ConstrainedSketch](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?ContextScope=all) object from a file containing dxf-format (AutoCAD) geometry. Only a limited number of entities are supported. This format should be used only if no other formats are available.



### Path

```
importDxf
```

### Required arguments

- *fileName*

  A String specifying the path to the dxf file to open.

### Optional arguments

None.

### Return value

A Mdb object.

### Exceptions

None.



## openMdb(...)



This method opens an existing model database file.



### Path

```
openMdb
```

### Required arguments

- *pathName*

  A String specifying the path to the model database file to open. If you do not provide a file extension, Abaqus/CAE attempts to open the file with .cae appended to the path.

### Optional arguments

None.

### Return value

An Mdb object.

### Exceptions

- If the file is an invalid model database:

  MdbError: invalid model database.

- If the file contains a model database from an Abaqus release other than the Abaqus release you are currently running:

  MdbError: incompatible release number, expected *<Abaqus release>*, got *<earlier or later Abaqus release>*

- If the model database file is already opened in write mode:

  MdbError: cannot open file: May be in use by another CAE session

- If the command fails to open the model database file for reasons not mentioned above:

  MdbError: cannot open file...



## openAcis(...)



This method creates an [AcisFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object from a file containing ACIS-format geometry. This object is subsequently used by the PartFromGeometryFile method.



### Path

```
openAcis
```

### Required arguments

- *fileName*

  A String specifying the path to the ACIS file to open.

### Optional arguments

- *scaleFromFile*

  A Boolean specifying whether to scale, rotate, and translate the part using the transform read from the ACIS file. The default value is OFF.

### Return value

An AcisFile object.

### Exceptions

- File is from a newer version of ACIS than the CAE kernel.

  Texterror: ACIS File version exceeds Kernel.

- The data in the ACIS file are corrupted.

  Texterror: Failed to read ACIS file.



## openCatia(...)



This method creates an [AcisFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object from a file containing CATIA V5–format geometry. This object is subsequently used by the PartFromGeometryFile method.



### Path

```
openCatia
```

### Required arguments

- *fileName*

  A String specifying the path to the CATIA file to open.

### Optional arguments

- *topology*

  A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid. If *topology*=SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid entity. The default value is SOLID.

- *convertUnits*

  A SymbolicConstant specifying whether the original units should be retained. Possible values are ON and OFF. The default value is OFF.

- *combineBodies*

  A Boolean specifying whether to combine the bodies in the CATPart file. If the bodies to be combined touch or overlap, invalid entities would result. For CATProduct files, this option will be ignored.

### Return value

An AcisFile object.

### Exceptions

None.



## openEnf(...)



This method creates an[AcisFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object from a file containing Elysium Neutral File-format geometry that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object is subsequently used by the PartFromGeometryFile method.



### Path

```
openEnf
```

### Required arguments

- *fileName*

  A String specifying the path to the Elysium Neutral File that was created by I-DEAS, Pro/ENGINEER, or CATIA V5.

- *fileType*

  A String specifying the type of CAD system that created the file. Possible values are “ideas”, “proe”, or “catiav5”.

### Optional arguments

- *topology*

  A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid. If *topology*=SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid entity. The default value is SOLID.

- *convertUnits*

  A Boolean specifying if the dimensions of the part should be converted to millimeters. The default value is OFF.

### Return value

An AcisFile object.

### Exceptions

None.



## openIges(...)



This method creates an [AcisFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object from a file containing IGES-format geometry. This object is subsequently used by the PartFromGeometryFile method.



### Path

```
openIges
```

### Required arguments

- *fileName*

  A String specifying the path to the IGES file to open.

### Optional arguments

- *trimCurve*

  A SymbolicConstant specifying the method used to define the trim curves that bound parametric surfaces. Possible values are:DEFAULT, use either of the following as specified by the contents of the IGES file.PARAMETRIC_DATA, use the parameter space of the surface being trimmed.THREED_DATA, use real space—the coordinate system of the part along with an indication that the trim curve lies on the parametric surface.The default value is DEFAULT.

- *scaleFromFile*

  A SymbolicConstant specifying whether the imported geometry needs to be scaled using the units information available in the IGES file. Possible values are ON and OFF. The default value is OFF. When the argument is set to ON, the geometry is scaled to millimeters with respect to the unit system specified in the IGES file.

- *msbo*

  A Boolean specifying if the IGES file contains MSBO (Manifold Solid B-Rep Object) entities. The default value is False.

- *includedLayers*

  A sequence of Ints specifying the levels or layers of entities that will be translated from the IGES file to build the part. The default is to include all the layers.

- *topology*

  A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid. If *topology*=SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid entity. The default value is SOLID.

- *uniteWires*

  A SymbolicConstant specifying whether the imported wires need to be united or not. Possible values are ON andOFF. The default value is ON. When importing a sketch, this value is set to OFF.

### Return value

An AcisFile object.

### Exceptions

- The data in the IGES file are corrupted.

  Texterror: Failed to read IGES file.



## openParasolid(...)



This method creates an[AcisFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object from a file containing Parasolid-format geometry. This object is subsequently used by the PartFromGeometryFile method.



### Path

```
openParasolid
```

### Required arguments

- *fileName*

  A String specifying the path to the Parasolid file to open.

### Optional arguments

- *topology*

  A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid. If *topology*=SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid entity. The default value is SOLID.

### Return value

An AcisFile object.

### Exceptions

None.



## openStep(...)



This method creates an [AcisFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object from a file containing STEP-format geometry. This object is subsequently used by the PartFromGeometryFile method.



### Path

```
openStep
```

### Required arguments

- *fileName*

  A String specifying the path to the STEP file to open.

### Optional arguments

- *scale*

  A Float specifying the scaling factor to apply to the imported geometric entities. The default value is 1.0.

### Return value

An AcisFile object.

### Exceptions

- The data in the STEP file are corrupted.

  Texterror: Failed to read STEP file.



## openVda(...)



This method creates an [AcisFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object from a file containing VDA-FS-format geometry. This object is subsequently used by the PartFromGeometryFile method.



### Path

```
openVda
```

### Required arguments

- *fileName*

  A String specifying the path to the VDA-FS file to open.

### Optional arguments

None.

### Return value

An AcisFile object.

### Exceptions

- The data in the VDA-FS file are corrupted.

  Texterror: Failed to read VDA file.



## openSolidworks(...)



This method creates an [AcisFile](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?ContextScope=all) object from a file containing Solidworks format geometry. This object is subsequently used by the PartFromGeometryFile method.



### Path

```
openSolidworks
```

### Required arguments

- *fileName*

  A String specifying the path to the Solidworks file to open.

### Optional arguments

- *topology*

  A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created. Possible values are SOLID, SHELL, and WIRE. If *topology*=SOLID, Abaqus/CAE attempts to attach cells to create a solid entity. If *topology*=SHELL, Abaqus/CAE builds the body as a shell entity, not as a solid entity. The default value is SOLID.

### Return value

An AcisFile object.

### Exceptions

- The data in the Solidworks file are corrupted.

  Texterror: Failed to read Solidworks file.



## close()



This method closes an open Mdb object but does not save the Mdb object to disk. After closing the Mdb object, this method creates a new unnamed empty Mdb object.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## save()



This method saves an Mdb object to disk at the location specified by *pathName* (*pathName* is a member of the Mdb object).



### Arguments

None.

### Return value

None.

### Exceptions

- If *pathName* is empty:

  MdbError: cannot save file: pathname member is empty

- If *pathName* is abaqus.cae:

  MdbError: “abaqus.cae” is an invalid CAE filename.

- If the command fails to save the Mdb object to disk for reasons not mentioned above:

  MdbError: cannot save file...



## saveAs(...)



This method saves an Mdb object to disk at the specified location.



### Required arguments

- *pathName*

  A String specifying the path to be used when the model database is saved to a file. If you do not provide a file extension, .cae is appended automatically to the path.

### Optional arguments

None.

### Return value

None.

### Exceptions

- If *pathName* is abaqus.cae:

  MdbError: “abaqus.cae” is an invalid CAE filename.

- If the command fails to save the Mdb object to disk for reasons not mentioned above:

  MdbError: cannot save file...



## openAuxMdb(...)



This method opens an auxiliary Mdb object on the disk at the specified location. This enables models from the auxiliary Mdb object to be copied into the current Mdb.



### Required arguments

- *pathName*

  A String specifying the path to the auxiliary Mdb which is to be opened. If you do not provide a file extension, .cae is appended automatically to the path.

### Optional arguments

None.

### Return value

None.

### Exceptions

- If the file is an invalid model database:

  MdbError: invalid model database.

- If the file contains a model database from an Abaqus release other than the Abaqus release you are currently running:

  MdbError: incompatible release number, expected *<Abaqus release>*, got *<earlier or later Abaqus release>*.

- If the command fails to open the model database file for reasons not mentioned above:

  MdbError: cannot open file...



## closeAuxMdb()



This method closes the auxiliary Mdb which had been opened earlier using the openAuxMdb command.



### Arguments

None.

### Return value

None.

### Exceptions

- If the auxiliary Mdb was not opened earlier.

  MdbError: The auxiliary Mdb was not opened..



## getAuxMdbModelNames()



This method returns a list of model names present in the auxiliary Mdb which had been opened earlier using the openAuxMdb command.



### Arguments

None.

### Return value

A list of model names present in the auxiliaryMdb

### Exceptions

- If the auxiliary Mdb was not opened earlier.

  MdbError: The auxiliary Mdb was not opened..



## copyAuxMdbModel(...)



This method copies a specified model from the auxiliary Mdb which had been opened earlier using the openAuxMdb command.



### Required arguments

- *fromName*

  A String specifying the model name in the auxiliary Mdb which is to be copied.

### Optional arguments

- *toName*

  A String specifying the name to be given to the model after it is copied into the Mdb. If this argument is not specified *toName* is assumed to be the same as *fromName*. If a model with name *toName* already exists in Mdb, it is overwritten.

### Return value

None.

### Exceptions

- If the auxiliary Mdb was not opened earlier.

  MdbError: The auxiliary Mdb was not opened.

- If the model fromName does not exist in the auxiliary Mdb.

  KeyError: fromName does not exist.



## Members

The Mdb object has members with the same names and descriptions as the arguments to the [Mdb](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?ContextScope=all#simaker-mdbmdbpyc) method.

In addition, the Mdb object can have the following members:

- *version*

  An Int specifying the release number of the Mdb object in memory.

- *lastChangedCount*

  A Float specifying the value of a counter associated with the Mdb object. The counter indicates when the Mdb object was last changed.

- *jobs*

  A repository of [Job](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobpyc.htm?ContextScope=all) objects.

- *adaptivityProcesses*

  A repository of [AdaptivityProcess](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-adaptivityprocesspyc.htm?ContextScope=all) objects.

- *coexecutions*

  A repository of [Coexecution](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coexecutionpyc.htm?ContextScope=all) objects.

- *optimizationProcesses*

  A repository of [OptimizationProcess](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationprocesspyc.htm?ContextScope=all) objects.

- *meshEditOptions*

  A [MeshEditOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mesheditoptionspyc.htm?ContextScope=all) object specifying the undo/redo behavior when editing meshes on parts or part instances.

- *models*

  A repository of [Model](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?ContextScope=all) objects.

- *customData*

  A [RepositorySupport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-repositorysupportpyc.htm?ContextScope=all) object.

- *annotations*

  A repository of [Annotation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-annotationpyc.htm?ContextScope=all) objects.