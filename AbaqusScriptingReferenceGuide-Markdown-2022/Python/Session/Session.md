# Session object

The Session object has no constructor. Abaqus creates the *session* member when a session is started.

## Access

```
session
```

## setValues(...)



This method modifies the Session object.



### Required arguments

None.

### Optional arguments

- *kernelMemoryLimit*

  A Float specifying the memory limit value for the Abaqus/CAE kernel process in megabytes. If the limit is exceeded, Abaqus/CAE displays an error message.The default memory limit value for Windows 32-bit systems if not set is 1800 MB. Increasing the memory limit is not recommended unless you are using a Windows 32-bit system with the boot option /3GB /userva=SizeInMBytes to extend the amount of memory available for Abaqus/CAE. In this case the limit can be changed to 2800 MB.If the kernel memory size reaches the **abq_ker_memory** value or the virtual memory limit of the machine, the following message will be displayed:`Operation did not complete due to a memory allocation failure.`For optimal performance, the memory limit should be set to a value less than the physical amount of memory on the machine.The minimum setting allowed is 256 MB.

### Return value

None.

### Exceptions

None.



## enableCADConnection(...)



This method enables the Abaqus/CAE listening port for the specified *CAD* system.



### Required arguments

- *CADName*

  A String specifying the CAD system. Available options are Pro/ENGINEER, CATIA V5, CATIA V6, NX and SolidWorks.

### Optional arguments

- *portNum*

  An Integer specifying the port number to be used by the CAD system to communicate with Abaqus/CAE. If unspecified, attempts will be made to identify an open port. The default ports used are as follow:Pro/E : 49178CATIA V5 : 49179SolidWorks : 49180NX : 49181CATIA V6 : 49182

### Return value

The connection port number used for the CAD connection.

### Exceptions

None.



## isCADConnectionEnabled()



This method checks the status of CAD Connection.



### Arguments

None.

### Return value

A Boolean value of True if the CAD connection enabled and False if the CAD connection disabled.

### Exceptions

None.



## disableCADConnection(...)



This method disables an associative import CAD connection that was enabled.



### Required arguments

- *CADName*

  A String specifying the CAD system for which associative import will be disabled. Available options are Pro/ENGINEER, CATIA V5, and CATIA V6, NX and SolidWorks.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## enableParameterUpdate(...)



This method enables parameter updates for ProE and NX by establishing a connection with the listening port previously setup by the CAD application.



### Required arguments

- *CADName*

  A String specifying the CAD system for which parameter update will be enabled. Available options are Pro/ENGINEER and NX.

- *CADVersion*

  A String specifying the CAD system version. Allowable options take the form of the specific CAD system plus a version string. Examples for Pro/ENGINEER are "Wildfire5" and "Creo4." An NX example is "NX11."

### Optional arguments

- *CADPort*

  An Integer specifying the port number to be used by Abaqus/CAE to communicate with the CAD system. If unspecified, attempts will be made to identify an open port. This port number is not the same as the *portNum* used by the associative import interface. The default CAD listening ports are as follow:ProE : 3344NX : 3344

### Return value

None.

### Exceptions

None.



## setCADPortNumber(...)



This method enables parameter updates for CATIA V5 and CATIA V6 by establishing a connection with the listening port previously setup by the CAD application. This port number is used to send the parameter information to the CAD system.



### Required arguments

- *CADName*

  A String specifying the CAD system for which the port number will be saved. The available options are 'CATIA V5' and ' CATIA V6'.

- *Port*

  An integer specifying the port number to be used by Abaqus/CAE to send the modified parameters to the CAD system.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## updateCADParameters(...)



This method updates the parameters for the specified model using the specified parameter file.



### Required arguments

- *modelName*

  A String specifying the model name to update.

- *CADName*

  A String specifying the CAD system for which Abaqus updates the parameters. The available options are 'Pro/ENGINEER', 'CATIA V5' and 'CATIA V6'.

- *parameterFile*

  A parameter file containing the parameters that were exposed in the CAD system using the 'ABQ_' prefix.

- *CADPartFile*

  A file name specifying the CAD part file for which parameter update is triggered.For *CADName*='CATIA V5' or 'CATIA V6', you can specify either products or parts using this argument. If you specify a product, Abaqus updates all of the parts associated with that product.For *CADName*='Pro/ENGINEER', this argument is optional, and you can specify update for parts only. However, a single file can be associated with multiple parts in the case of family tables. In this case, Abaqus updates all listed parts.

### Optional arguments

- *CADPartName*

  An String specifying the part name to update. This part name should match the part name in the originating CAD system.If you specify neither *CADPartFile* nor *CADPartName* during an update in which you specified *CADName*='Pro/ENGINEER', Abaqus updates all of the parts in the specified file.

### Return value

None.

### Exceptions

None.



## disableParameterUpdate(...)



This method disables an associative CAD connection using parameters.



### Required arguments

- *CADName*

  A String specifying the CAD system for which the parameter update will be disabled. Available option is Pro/ENGINEER.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## printToFile(...)



This method prints canvas objects to a file using the attributes stored in the [PrintOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-printoptionspyc.htm?ContextScope=all) object and the appropriate format options object.



### Required arguments

- *fileName*

  A String specifying the file to which the image is to be written. If no file extension is supplied, an extension is added based on the selected image format (.ps, .eps, .png, .tif, .svg, or .svgz).

### Optional arguments

- *format*

  A SymbolicConstant specifying the image format. Possible values are PNG, SVG, TIFF, PS, and EPS. The default value is PNG.

- *canvasObjects*

  A sequence of canvas objects (viewports, text strings, or arrows) to print. The default is to print all canvas objects.

- *compression*

  A Boolean specifying the format for an SVG file. It is only valid to use this argument when *format* is SVG. Possible values are False (Uncompressed) and True (Compressed).

### Return value

None.

### Exceptions

None.



## printToPrinter(...)



This method prints canvas objects to a Windows printer or to a PostScript printer. The attributes used for printing to a Windows printer are stored in the [PrintOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-printoptionspyc.htm?ContextScope=all) object and the [PageSetupOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pagesetupoptionspyc.htm?ContextScope=all) object; the attributes used for printing to a PostScript printer are stored in the [PrintOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-printoptionspyc.htm?ContextScope=all) object and the [PsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psoptionspyc.htm?ContextScope=all) object.



### Required arguments

None.

### Optional arguments

- *printCommand*

  A String specifying the operating system command or printer name to issue for printing to the printer. The default value is “lpr” or the value specified by the printOptions method. If you create a script to print directly to a Windows printer, the *printCommand* must take the following form:`session.printToPrinter.setValues(printCommand='PRINTER[                                 number of characters in name                                 ]:                                 printername                                 PROPERTIES[                                 number of characters in properties                                 ]:                                 document properties                                 ')                              `The `PROPERTIES` is a list of characters that represents the printing preferences for the selected Windows printer. The properties are not required in a script; the printed output will use the current settings for the selected printer. You can use `'PRINTER[7]: DEFAULT'` to specify the default Windows printer.

- *numCopies*

  An Int specifying the number of copies to print. Possible values are 1 ≤≤ *numCopies* ≤≤ 100. The default value is 1.

- *canvasObjects*

  A sequence of canvas objects (viewports, text strings, or arrows) to print. The default is to print all canvas objects.

### Return value

None.

### Exceptions

- If *printCommand* is invalid:

  SystemError: invalid print command

- If the print command fails:

  SystemError: print command failed

- If *numCopies* is out of range:

  RangeError: numCopies must be in the range 1 <= value <= 100

- If *compression* is specified when *format* is not SVG :

  TypeError: keyword error on compression



## saveOptions(...)



This method saves your customized display settings.



### Required arguments

- *directory*

  A SymbolicConstant specifying the directory in which Abaqus saves the file that will be used to restore your customized settings (abaqus_2021.gpr). Possible values are HOME and CURRENT.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## writeVrmlFile(...)



This method exports the current viewport objects to a file.



### Required arguments

- *fileName*

  A String specifying the file to which the graphics data is to be written. If no file extension is supplied, an extension is added based on the selected format (.wrl, .wrz).

### Optional arguments

- *format*

  A Boolean specifying the format. Possible values are False (Uncompressed) and True (Compressed).

- *canvasObjects*

  A sequence of canvas objects (viewports, text strings, or arrows) to export.

### Return value

None.

### Exceptions

None.



## write3DXMLFile(...)



This method exports the current viewport objects to a file.



### Required arguments

- *fileName*

  A String specifying the file to which the graphics data is to be written. If no file extension is supplied, (.3dxml) will be added.

### Optional arguments

- *format*

  A Boolean specifying the format. Possible values are False (Uncompressed) and True (Compressed).

- *canvasObjects*

  A sequence of canvas objects to export.

### Return value

None.

### Exceptions

None.



## writeOBJFile(...)



This method exports the current viewport objects to a file.



### Required arguments

- *fileName*

  A String specifying the file to which the graphics data is to be written. If no file extension is supplied, (.obj) will be added.

### Optional arguments

- *canvasObjects*

  A sequence of canvas objects to export.

### Return value

None.

### Exceptions

None.



## Members

The Session object can have the following members:

- *attachedToGui*

  A Boolean specifying whether an Abaqus interactive session is running.

- *replayInProgress*

  A Boolean specifying whether Abaqus is executing a replay file.

- *kernelMemoryFootprint*

  A Float specifying the memory usage value for the Abaqus/CAE kernel process in megabytes.

- *kernelMemoryMaxFootprint*

  A Float specifying the maximum value for the memory usage for the Abaqus/CAE kernel process in megabytes.

- *kernelMemoryLimit*

  A Float specifying the limit for the memory use for the Abaqus/CAE kernel process in megabytes.

- *colors*

  A repository of [Color](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-colorpyc.htm?ContextScope=all) objects.

- *journalOptions*

  A [JournalOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-journaloptionspyc.htm?ContextScope=all) object specifying how to record selection of geometry in the journal and replay files.

- *memoryReductionOptions*

  A [MemoryReductionOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-memoryreductionoptionspyc.htm?ContextScope=all) object specifying options for running in reduced memory mode.

- *nodeQuery*

  A [NodeQuery](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nodequerypyc.htm?ContextScope=all) object specifying nodes and their coordinates in a path.

- *sketcherOptions*

  A [ConstrainedSketcherOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketcheroptionspyc.htm?ContextScope=all) object specifying common options for all sketches.

- *viewerOptions*

  A [ViewerOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-vieweroptionspyc.htm?ContextScope=all) object.

- *animationOptions*

  An [AnimationOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-animationoptionspyc.htm?ContextScope=all) object.

- *aviOptions*

  An [AVIOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-avioptionspyc.htm?ContextScope=all) object.

- *imageAnimationOptions*

  An [ImageAnimationOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-imageanimationoptionspyc.htm?ContextScope=all) object.

- *imageAnimation*

  An [ImageAnimation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-imageanimationpyc.htm?ContextScope=all) object.

- *quickTimeOptions*

  A [QuickTimeOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-quicktimeoptionspyc.htm?ContextScope=all) object.

- *viewports*

  A repository of [Viewport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewportpyc.htm?ContextScope=all) objects.

- *customData*

  A [RepositorySupport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-repositorysupportpyc.htm?ContextScope=all) object.

- *defaultFieldReportOptions*

  A [FieldReportOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldreportoptionspyc.htm?ContextScope=all) object.

- *defaultFreeBodyReportOptions*

  A [FreeBodyReportOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-freebodyreportoptionspyc.htm?ContextScope=all) object.

- *fieldReportOptions*

  A [FieldReportOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldreportoptionspyc.htm?ContextScope=all) object.

- *freeBodyReportOptions*

  A [FreeBodyReportOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-freebodyreportoptionspyc.htm?ContextScope=all) object.

- *odbs*

  A repository of [Odb](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?ContextScope=all) objects.

- *scratchOdbs*

  A repository of [ScratchOdb](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-scratchodbpyc.htm?ContextScope=all) objects.

- *defaultOdbDisplay*

  A [DefaultOdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-defaultodbdisplaypyc.htm?ContextScope=all) object.

- *defaultPlot*

  A [DefaultPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-defaultplotpyc.htm?ContextScope=all) object.

- *defaultChartOptions*

  A [DefaultChartOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-defaultchartoptionspyc.htm?ContextScope=all) object.

- *odbData*

  A repository of [OdbData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatapyc.htm?ContextScope=all) objects.

- *mdbData*

  A repository of [MdbData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbdatapyc.htm?ContextScope=all) objects.

- *paths*

  A repository of [Path](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pathpyc.htm?ContextScope=all) objects.

- *freeBodies*

  A repository of [FreeBody](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-freebodypyc.htm?ContextScope=all) objects.

- *streams*

  A repository of [Stream](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-streampyc.htm?ContextScope=all) objects.

- *spectrums*

  A repository of [Spectrum](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-spectrumpyc.htm?ContextScope=all) objects.

- *currentProbeValues*

  A [CurrentProbeValues](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-currentprobevaluespyc.htm?ContextScope=all) object.

- *defaultProbeOptions*

  A [ProbeOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-probeoptionspyc.htm?ContextScope=all) object.

- *probeOptions*

  A [ProbeOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-probeoptionspyc.htm?ContextScope=all) object.

- *probeReport*

  A [ProbeReport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-probereportpyc.htm?ContextScope=all) object.

- *defaultProbeReport*

  A [ProbeReport](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-probereportpyc.htm?ContextScope=all) object.

- *selectedProbeValues*

  A [SelectedProbeValues](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-selectedprobevaluespyc.htm?ContextScope=all) object.

- *printOptions*

  A [PrintOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-printoptionspyc.htm?ContextScope=all) object.

- *epsOptions*

  An [EpsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-epsoptionspyc.htm?ContextScope=all) object.

- *pageSetupOptions*

  A [PageSetupOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pagesetupoptionspyc.htm?ContextScope=all) object.

- *pngOptions*

  A [PngOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pngoptionspyc.htm?ContextScope=all) object.

- *psOptions*

  A [PsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psoptionspyc.htm?ContextScope=all) object.

- *svgOptions*

  A [SvgOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-svgoptionspyc.htm?ContextScope=all) object.

- *tiffOptions*

  A [TiffOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tiffoptionspyc.htm?ContextScope=all) object.

- *autoColors*

  An [AutoColors](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-autocolorspyc.htm?ContextScope=all) object specifying the color palette to be used for color coding.

- *xyColors*

  An [AutoColors](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-autocolorspyc.htm?ContextScope=all) object specifying the color palette to be used for[XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects.

- *xyDataObjects*

  A repository of [XYData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?ContextScope=all) objects.

- *curves*

  A repository of [XYCurve](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xycurvepyc.htm?ContextScope=all) objects.

- *xyPlots*

  A repository of [XYPlot](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyplotpyc.htm?ContextScope=all) objects.

- *charts*

  A repository of [Chart](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chartpyc.htm?ContextScope=all) objects.

- *defaultXYReportOptions*

  An [XYReportOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyreportoptionspyc.htm?ContextScope=all) object.

- *xyReportOptions*

  An [XYReportOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xyreportoptionspyc.htm?ContextScope=all) object.

- *views*

  A repository of [View](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewpyc.htm?ContextScope=all) objects.

- *networkDatabaseConnectors*

  A repository of [NetworkDatabaseConnector](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-networkdatabaseconnectorpyc.htm?ContextScope=all) objects.

- *displayGroups*

  A repository of [DisplayGroup](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygrouppyc.htm?ContextScope=all) objects.

- *graphicsInfo*

  A [GraphicsInfo](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-graphicsinfopyc.htm?ContextScope=all) object.

- *defaultGraphicsOptions*

  A [GraphicsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-graphicsoptionspyc.htm?ContextScope=all) object.

- *graphicsOptions*

  A [GraphicsOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-graphicsoptionspyc.htm?ContextScope=all) object.

- *defaultViewportAnnotationOptions*

  A [ViewportAnnotationOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-viewportannotationoptionspyc.htm?ContextScope=all) object.

- *queues*

  A repository of [Queue](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-queuepyc.htm?ContextScope=all) objects.

- *currentViewportName*

  A String specifying the name of the current viewport.

- *sessionState*

  A Dictionary object specifying the viewports and their associated models. The Dictionary key specifies the viewport name. The Dictionary value is a Dictionary specifying the model name.

- *images*

  A repository of [Image](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-imagepyc.htm?ContextScope=all) objects.

- *movies*

  A repository of [Movie](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-moviepyc.htm?ContextScope=all) objects.

- *defaultLightOptions*

  A [LightOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lightoptionspyc.htm?ContextScope=all) object.

- *drawingArea*

  A [DrawingArea](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-drawingareapyc.htm?ContextScope=all) object.

- *defaultMesherOptions*

  A [MesherOptions](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mesheroptionspyc.htm?ContextScope=all) object specifying how to control default settings in the Mesh module.

- *drawings*

  A repository of [Drawing](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-drawingpyc.htm?ContextScope=all) objects.