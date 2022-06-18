Change Log
==========

Change log from V2021 to V2022

Constraint
----------

- :py:class:`~abaqus.Constraint.Coupling.Coupling` and :py:meth:`ConstraintModel.Coupling() <abaqus.Constraint.ConstraintModel.ConstraintModel.Coupling>`: add **alpha** argument.
- :py:class:`~abaqus.Constraint.Tie.Tie` and :py:meth:`ConstraintModel.Tie() <abaqus.Constraint.ConstraintModel.ConstraintModel.Tie>`: arguments **master** and **slave** change to **main** and **secondary**.

Datum
-----

- Add :py:meth:`DatumCsys.globalToLocal() <abaqus.Datum.DatumCsys.DatumCsys.globalToLocal>` and :py:meth:`DatumCsys.localToGlobal() <abaqus.Datum.DatumCsys.DatumCsys.localToGlobal>`.

Field Report
------------

- :py:meth:`FieldReportOptions.setValues() <abaqus.FieldReport.FieldReportOptions.FieldReportOptions.setValues>`: add printLocalCSYS argument.

Interaction
-----------

- :py:class:`~abaqus.Interaction.ContactExp.ContactExp` and :py:meth:`InteractionModel.ContactExp() <abaqus.Interaction.InteractionModel.InteractionModel.ContactExp>`: argument **masterSlaveAssignments** renames to **mainSecondaryAssignments**.
- :py:class:`~abaqus.Interaction.ContactStd.ContactStd` and :py:meth:`InteractionModel.ContactStd() <abaqus.Interaction.InteractionModel.InteractionModel.ContactStd>`: argument **masterSlaveAssignments** renames to **mainSecondaryAssignments**.
- :py:class:`~abaqus.Interaction.CyclicSymmetry.CyclicSymmetry` and :py:meth:`InteractionModel.CyclicSymmetry() <abaqus.Interaction.InteractionModel.InteractionModel.CyclicSymmetry>`: arguments **master** and **slave** rename to **main** and **secondary**. 
- :py:class:`~abaqus.Interaction.ExpInitialization.ExpInitialization` and :py:meth:`InteractionModel.ExpInitialization() <abaqus.Interaction.InteractionModel.InteractionModel.ExpInitialization>`: argument **slaveNodesetName** renames to **secondaryNodesetName**.
- :py:class:`~abaqus.Interaction.GapHeatGeneration.GapHeatGeneration`: argument **slaveFraction** renames to **secondaryFraction**.
- :py:meth:`InitializationAssignment.appendInStep() <abaqus.Interaction.InitializationAssignment.InitializationAssignment.appendInStep>`: argument **assignments**'s docstring changes (slave -> secondary). 
- :py:class:`~abaqus.Interaction.MasterSlaveAssignment.MasterSlaveAssignment` change to :py:class:`~abaqus.Interaction.MainSecondaryAssignment.MainSecondaryAssignment`.
- :py:meth:`InteractionModel.contactDetection() <abaqus.Interaction.InteractionModel.InteractionModel.contactDetection>`: arguments **createUnionOfMasterSurfaces**, **createUnionOfSlaveSurfaces**, **createUnionOfMasterSlaveSurfaces** change to **createUnionOfMainSurfaces**, **createUnionOfSecondarySurfaces**, **createUnionOfMainSecondarySurfaces**.
- :py:meth:`PolarityAssignments.changeValuesInStep() <abaqus.Interaction.PolarityAssignments.PolarityAssignments.changeValuesInStep>`: argument **stepName**'s docstring changes (master-slave -> main-secondary).
- :py:class:`~abaqus.Interaction.PressurePenetration.PressurePenetration` and :py:meth:`InteractionModel.PressurePenetration() <abaqus.Interaction.InteractionModel.InteractionModel.PressurePenetration>`: arguments **masterPoints** and **slavePoints** rename to **mainPoints** and **secondaryPoints**.
- :py:class:`~abaqus.Interaction.Radiation.Radiation` and :py:meth:`InteractionModel.Radiation() <abaqus.Interaction.InteractionModel.InteractionModel.Radiation>`: arguments **masterEmissivity** and **slaveEmissivity** rename to **mainEmissivity** and **secondaryEmissivity**.
- :py:class:`~abaqus.Interaction.SelfContactStd.SelfContactStd` and :py:meth:`InteractionModel.SelfContactStd() <abaqus.Interaction.InteractionModel.InteractionModel.SelfContactStd>`: argument **smooth**'s docstring changes (master -> main).
- :py:class:`~abaqus.Interaction.StdContactControl.StdContactControl` and :py:meth:`InteractionModel.StdContactControl() <abaqus.Interaction.InteractionModel.InteractionModel.StdContactControl>`: argument **uerrmx**'s docstring changes (slave -> secondary).
- :py:class:`~abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp` and :py:meth:`InteractionModel.SurfaceToSurfaceContactExp() <abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactExp>`: arguments **master** and **slave** rename to **main** and **secondary**. 
- :py:meth:`SurfaceToSurfaceContactExp.swapSurfaces() <abaqus.Interaction.SurfaceToSurfaceContactExp.SurfaceToSurfaceContactExp.swapSurfaces>`: docstring changes (master -> main, slave -> secondary). 
- :py:class:`~abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd` and :py:meth:`InteractionModel.SurfaceToSurfaceContactStd() <abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactStd>`: arguments **master** and **slave** rename to **main** and **secondary**.  
- :py:meth:`SurfaceToSurfaceContactStd.swapSurfaces() <abaqus.Interaction.SurfaceToSurfaceContactStd.SurfaceToSurfaceContactStd.swapSurfaces>`: docstring changes (master -> main, slave -> secondary). 

Job
---

- :py:class:`~abaqus.Job.JobFromInputFile.JobFromInputFile` and :py:meth:`JobMdb.JobFromInputFile() <abaqus.Job.JobMdb.JobMdb.JobFromInputFile>`: add argument **licenseType**.
- :py:meth:`JobMdb.Job() <abaqus.Job.JobMdb.JobMdb.Job>`: add argument **licenseType**.
- Add :py:class:`~abaqus.Job.Coexecution.Coexecution` to attributes of :py:class:`~abaqus.Mdb.Mdb.Mdb`. 

Material
--------

- Add classes :py:class:`~abaqus.Material.Plastic.CrushStress.CrushStress.CrushStress` and :py:class:`~abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor.CrushStressVelocityFactor`, add method :py:meth:`Material.CrushStress() <abaqus.Material.Material.Material.CrushStress>`. 
- :py:class:`~abaqus.Material.Elastic.Linear.Elastic.Elastic` and :py:meth:`Material.Elastic() <abaqus.Material.Material.Material.Elastic>`: argument **type** add **BILAMINA**.
- :py:class:`~abaqus.Material.Elastic.HyperElastic.Hyperelastic.Hyperelastic` and :py:meth:`Material.Hyperelastic() <abaqus.Material.Material.Material.Hyperelastic>`: argument **type** add **VALANIS_LANDEL**.
- :py:class:`~abaqus.Material.Plastic.Plastic.Plastic` and :py:meth:`Material.Plastic() <abaqus.Material.Material.Material.Plastic>`: add argument **extrapolation**.

Mesh
----

- :py:class:`~abaqus.Mesh.ElemType.ElemType`: add arguments **linearKinematicCtrl** and **initialGapOpening**.
- :py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray`:  argument **faces** changes to **elemFaces**.
- :py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray`:  argument **edges** changes to **elemEdges**.

Odb
---

- Add :py:meth:`OdbDatumCsys.globalToLocal() <abaqus.Odb.OdbDatumCsys.OdbDatumCsys.globalToLocal>` and :py:meth:`OdbDatumCsys.localToGlobal() <abaqus.Odb.OdbDatumCsys.OdbDatumCsys.localToGlobal>`.

Optimization
------------

- :py:class:`~abaqus.Optimization.BeadTask.BeadTask` and :py:meth:`OptimizationTaskModel.BeadTask() <abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask>`: add argument **groupOperator**.
- :py:class:`~abaqus.Optimization.DesignDirection.DesignDirection` and and :py:meth:`OptimizationTask.DesignDirection() <abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection>`: arguments **masterPoint** and **masterDetermination** change to **mainPoint** and **mainPointDetermination**.
- :py:class:`~abaqus.Optimization.DrillControl.DrillControl` and and :py:meth:`OptimizationTask.DrillControl() <abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl>`: arguments **masterPoint** and **masterDetermination** change to **mainPoint** and **mainPointDetermination**.
- :py:class:`~abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl` and and :py:meth:`OptimizationTask.ShapeDemoldControl() <abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl>`: argument **masterDetermination** changes to **mainPointDetermination**.
- :py:class:`~abaqus.Optimization.ShapeMemberSize.ShapeMemberSize` and and :py:meth:`OptimizationTask.ShapeMemberSize() <abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize>`: add arguments **assignNodeGroupRegion** and **nodeGroupRegion**.
- :py:class:`~abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry` and and :py:meth:`OptimizationTask.ShapePointSymmetry() <abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry>`: argument **masterDetermination** changes to **mainPointDetermination**.
- :py:class:`~abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry` and and :py:meth:`OptimizationTask.ShapeRotationalSymmetry() <abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry>`: arguments **masterPoint** and **masterDetermination** change to **mainPoint** and **mainPointDetermination**.
- :py:class:`~abaqus.Optimization.ShapeTask.ShapeTask` and :py:meth:`OptimizationTaskModel.ShapeTask() <abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask>`: add argument **groupOperator**.
- :py:class:`~abaqus.Optimization.SizingTask.SizingTask` and :py:meth:`OptimizationTaskModel.SizingTask() <abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask>`: add argument **groupOperator**.
- :py:class:`~abaqus.Optimization.StampControl.StampControl` and and :py:meth:`OptimizationTask.StampControl() <abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl>`: arguments **masterPoint** and **masterDetermination** change to **mainPoint** and **mainPointDetermination**.
- :py:class:`~abaqus.Optimization.TopologyTask.TopologyTask` and :py:meth:`OptimizationTaskModel.TopologyTask() <abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask>`: add argument **groupOperator**.
- Add :py:class:`~abaqus.Optimization.TopologyMillingControl.TopologyMillingControl` and :py:meth:`OptimizationTask.TopologyMillingControl() <abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl>`.
- :py:class:`~abaqus.Optimization.TurnControl.TurnControl` and and :py:meth:`OptimizationTask.TurnControl() <abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl>`: arguments **masterPoint** and **masterDetermination** change to **mainPoint** and **mainPointDetermination**.

Part
----

- :py:meth:`PartBase.getCoordinates() <abaqus.Part.PartBase.PartBase.getCoordinates>` add argument **csys**.

Session
-------

- :py:meth:`Session.printToFile() <abaqus.Session.Session.Session.printToFile>`: argument **compression**'s docstring changes.

Step Output
-----------

- :py:meth:`FieldOutputRequest.setValuesInStep() <abaqus.StepOutput.FieldOutputRequest.FieldOutputRequest.setValuesInStep>`: argument **timePoints** changes to **timePoint**.

XY
---

- :py:meth:`XYData.xyDataListFromField() <abaqus.XY.XYData.XYData.xyDataListFromField>` add argument **operator**.
