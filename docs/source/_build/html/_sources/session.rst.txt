=======
Session
=======

Session commands are used to create objects that are not stored with the model; for example, viewports and display groups. Abaqus/CAE retains Session objects only for the duration of the session; they are not saved when the model database is saved.

.. toctree::
   :maxdepth: 2
   :caption: Objects of Session

   session/animation
   session/canvas
   session/display_options
   session/display
   session/field_report
   session/odb_display
   session/path
   session/plot_options
   session/print
   session/xy


Attributes
----------

- **session.attachedToGui**: A Boolean specifying whether an Abaqus interactive session is running.
- **session.replayInProgress**: A Boolean specifying whether Abaqus is executing a replay file.
- **session.kernelMemoryFootprint**: A Float specifying the memory usage value for the Abaqus/CAE kernel process in megabytes.
- **session.kernelMemoryMaxFootprint**: A Float specifying the maximum value for the memory usage for the Abaqus/CAE kernel process in megabytes.
- **session.kernelMemoryLimit**: A Float specifying the limit for the memory use for the Abaqus/CAE kernel process in megabytes.
- **session.colors**: A repository of :py:class:`abaqus.Session.Color.Color` objects.
- **session.journalOptions**: A :py:class:`abaqus.Session.JournalOptions.JournalOptions` object specifying how to record selection of geometry in the journal and replay files.
- **session.memoryReductionOptions**: A :py:class:`abaqus.Session.MemoryReductionOptions.MemoryReductionOptions` object specifying options for running in reduced memory mode.
- **session.nodeQuery**: A :py:class:`abaqus.PathAndProbe.NodeQuery.NodeQuery` object specifying nodes and their coordinates in a path.
- **session.sketcherOptions**: A :py:class:`abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions` object specifying common options for all sketches.
- **session.viewerOptions**: A :py:class:`abaqus.OdbDisplay.ViewerOptions.ViewerOptions` object.
- **session.animationOptions**: An :py:class:`abaqus.Animation.AnimationOptions.AnimationOptions` object.
- **session.aviOptions**: An :py:class:`abaqus.Animation.AVIOptions.AVIOptions` object.
- **session.imageAnimationOptions**: An :py:class:`abaqus.Animation.ImageAnimationOptions.ImageAnimationOptions` object.
- **session.imageAnimation**: An :py:class:`abaqus.Animation.ImageAnimation.ImageAnimation` object.
- **session.quickTimeOptions**: A :py:class:`abaqus.Animation.QuickTimeOptions.QuickTimeOptions` object.
- **session.viewports**: A repository of :py:class:`abaqus.Canvas.Viewport.Viewport` objects.
- **session.customData**: A :py:class:`abaqus.CustomKernel.RepositorySupport.RepositorySupport` object.
- **session.defaultFieldReportOptions**: A :py:class:`abaqus.FieldReport.FieldReportOptions.FieldReportOptions` object.
- **session.defaultFreeBodyReportOptions**: A :py:class:`abaqus.FieldReport.FreeBodyReportOptions.FreeBodyReportOptions` object.
- **session.fieldReportOptions**: A :py:class:`abaqus.FieldReport.FieldReportOptions.FieldReportOptions` object.
- **session.freeBodyReportOptions**: A :py:class:`abaqus.FieldReport.FreeBodyReportOptions.FreeBodyReportOptions` object.
- **session.odbs**: A repository of :py:class:`abaqus.Odb.Odb.Odb` objects.
- **session.scratchOdbs**: A repository of :py:class:`abaqus.Odb.ScratchOdb.ScratchOdb` objects.
- **session.defaultOdbDisplay**: A :py:class:`abaqus.OdbDisplay.DefaultOdbDisplay.DefaultOdbDisplay` object.
- **session.defaultPlot**: A :py:class:`abaqus.XY.DefaultPlot.DefaultPlot` object.
- **session.defaultChartOptions**: A :py:class:`abaqus.XY.DefaultChartOptions.DefaultChartOptions` object.
- **session.odbData**: A repository of :py:class:`abaqus.PlotOptions.OdbData.OdbData` objects.
- **session.mdbData**: A repository of :py:class:`abaqus.PlotOptions.MdbData.MdbData` objects.
- **session.paths**: A repository of :py:class:`abaqus.PathAndProbe.Path.Path` objects.
- **session.freeBodies**: A repository of :py:class:`abaqus.PathAndProbe.FreeBody.FreeBody` objects.
- **session.streams**: A repository of :py:class:`abaqus.PathAndProbe.Stream.Stream` objects.
- **session.spectrums**: A repository of :py:class:`abaqus.PathAndProbe.Spectrum.Spectrum` objects.
- **session.currentProbeValues**: A :py:class:`abaqus.PathAndProbe.CurrentProbeValues.CurrentProbeValues` object.
- **session.defaultProbeOptions**: A :py:class:`abaqus.PathAndProbe.ProbeOptions.ProbeOptions` object.
- **session.probeOptions**: A :py:class:`abaqus.PathAndProbe.ProbeOptions.ProbeOptions` object.
- **session.probeReport**: A :py:class:`abaqus.PathAndProbe.ProbeReport.ProbeReport` object.
- **session.defaultProbeReport**: A :py:class:`abaqus.PathAndProbe.ProbeReport.ProbeReport` object.
- **session.selectedProbeValues**: A :py:class:`abaqus.PathAndProbe.SelectedProbeValues.SelectedProbeValues` object.
- **session.printOptions**: A :py:class:`abaqus.Print.PrintOptions.PrintOptions` object.
- **session.epsOptions**: An :py:class:`abaqus.Print.EpsOptions.EpsOptions` object.
- **session.pageSetupOptions**: A :py:class:`abaqus.Print.PageSetupOptions.PageSetupOptions` object.
- **session.pngOptions**: A :py:class:`abaqus.Print.PngOptions.PngOptions` object.
- **session.psOptions**: A :py:class:`abaqus.Print.PsOptions.PsOptions` object.
- **session.svgOptions**: A :py:class:`abaqus.Print.SvgOptions.SvgOptions` object.
- **session.tiffOptions**: A :py:class:`abaqus.PredefinedField.TiffOptions.TiffOptions` object.
- **session.autoColors**: An :py:class:`abaqus.Session.AutoColors.AutoColors` object specifying the color palette to be used for color coding.
- **session.xyColors**: An :py:class:`abaqus.Session.AutoColors.AutoColors` object specifying the color palette to be used forXYCurve objects.
- **session.xyDataObjects**: A repository of :py:class:`abaqus.XY.XYData.XYData` objects.
- **session.curves**: A repository of :py:class:`abaqus.XY.XYCurve.XYCurve` objects.
- **session.xyPlots**: A repository of :py:class:`abaqus.XY.XYPlot.XYPlot` objects.
- **session.charts**: A repository of :py:class:`abaqus.XY.Chart.Chart` objects.
- **session.defaultXYReportOptions**: An :py:class:`abaqus.XY.XYReportOptions.XYReportOptions` object.
- **session.xyReportOptions**: An :py:class:`abaqus.XY.XYReportOptions.XYReportOptions` object.
- **session.views**: A repository of :py:class:`abaqus.UtilityAndView.View.View` objects.
- **session.networkDatabaseConnectors**: A repository of :py:class:`abaqus.Session.NetworkDatabaseConnector.NetworkDatabaseConnector` objects.
- **session.displayGroups**: A repository of :py:class:`abaqus.DisplayGroup.DisplayGroup.DisplayGroup` objects.
- **session.graphicsInfo**: A :py:class:`abaqus.DisplayOptions.GraphicsInfo.GraphicsInfo` object.
- **session.defaultGraphicsOptions**: A :py:class:`abaqus.DisplayOptions.GraphicsOptions.GraphicsOptions` object.
- **session.graphicsOptions**: A :py:class:`abaqus.DisplayOptions.GraphicsOptions.GraphicsOptions` object.
- **session.defaultViewportAnnotationOptions**: A :py:class:`abaqus.DisplayOptions.ViewportAnnotationOptions.ViewportAnnotationOptions` object.
- **session.queues**: A repository of :py:class:`abaqus.Job.Queue.Queue` objects.
- **session.currentViewportName**: A String specifying the name of the current viewport.
- **session.sessionState**: A Dictionary object specifying the viewports and their associated models. The Dictionary key specifies the viewport name. The Dictionary value is a Dictionary specifying the model name.
- **session.images**: A repository of :py:class:`abaqus.Session.Image.Image` objects.
- **session.movies**: A repository of :py:class:`abaqus.Animation.Movie.Movie` objects.
- **session.defaultLightOptions**: A :py:class:`abaqus.DisplayOptions.LightOptions.LightOptions` object.
- **session.drawingArea**: A :py:class:`abaqus.Canvas.DrawingArea.DrawingArea` object.
- **session.defaultMesherOptions**: A :py:class:`abaqus.Mesh.MesherOptions.MesherOptions` object specifying how to control default settings in the Mesh module.
- **session.drawings**: A repository of :py:class:`abaqus.Session.Drawing.Drawing` objects.



Object features
---------------

Basic features of the Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Session.SessionBase.SessionBase
    :members:

Animation features of the Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Animation.AnimationSession.AnimationSession
    :members:

Display Group features of the Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.DisplayGroup.DisplayGroupSession.DisplayGroupSession
    :members:

Field Report features of the Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.FieldReport.FieldReportSession.FieldReportSession
    :members:

Job features of the Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Job.JobSession.JobSession
    :members:

Odb features of the Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Odb.OdbSession.OdbSession
    :members:

Path features of the Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.PathAndProbe.PathSession.PathSession
    :members:

XY features of the Session
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.XY.XYSession.XYSession
    :members:


AutoColors
~~~~~~~~~~

.. autoclass:: abaqus.Session.AutoColors.AutoColors
    :members:

Color
~~~~~

.. autoclass:: abaqus.Session.Color.Color
    :members:

Drawing
~~~~~~~

.. autoclass:: abaqus.Session.Drawing.Drawing
    :members:

Image
~~~~~

.. autoclass:: abaqus.Session.Image.Image
    :members:

JournalOptions
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Session.JournalOptions.JournalOptions
    :members:

MemoryReductionOptions
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Session.MemoryReductionOptions.MemoryReductionOptions
    :members:

NetworkDatabaseConnector
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Session.NetworkDatabaseConnector.NetworkDatabaseConnector
    :members:

NumberFormat
~~~~~~~~~~~~

.. autoclass:: abaqus.Session.NumberFormat.NumberFormat
    :members:

