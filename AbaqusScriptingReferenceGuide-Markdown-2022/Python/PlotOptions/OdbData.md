# OdbData object

The OdbData object stores non persistent values and attributes associated with an open odb for the given session. The OdbData object has no constructor. Abaqus creates the *odbData* repository when you import the Visualization module. Abaqus creates a OdbData object when an odb is opened.

## Access

```
import visualization
session.odbData[name]
```

## setValues(...)



This method modifies the OdbData object.



### Required arguments

None.

### Optional arguments

- *activeFrames*

  A sequence specifying the active frames, or the SymbolicConstant ALL. Each item in the sequence is a tuple defining the stepName followed by a sequence of expressions specifying frame numbers. The expression can be any of the following:An Int specifying a single frame number; for example, `1`.A String specifying a single frame number ; for example, `'7'`.A String specifying a sequence of frame numbers; for example, `'3:5'` and `'3:15:3'`.For these expressions a negative number will indicate reverse numbering: -1 is the last frame of the step, -2 is the one before the last frame. Frame numbering starts at 0.

- *stepPeriods*

  A sequence of (String, Float) sequences specifying the stepName and the stepPeriod. Alternatively, this member may take the value ODB_VALUES.

### Return value

None.

### Exceptions

None.



## Members

The OdbData object can have the following members:

- *activeFrames*

  A tuple specifying the active frames, or the SymbolicConstant ALL. Each item in the sequence is a tuple defining the stepName followed by a sequence of expressions specifying frame numbers. The expression can be any of the following:

  - An Int specifying a single frame number; for example, `1`.
  - A String specifying a single frame number ; for example, `'7'`.
  - A String specifying a sequence of frame numbers; for example, `'3:5'` and `'3:15:3'`.

  For these expressions a negative number will indicate reverse numbering: -1 is the last frame of the step, -2 is the one before the last frame. Frame numbering starts at 0.

- *stepPeriods*

  A tuple of (String, Float) tuples specifying the stepName and the stepPeriod. Alternatively, this member may take the value ODB_VALUES.

- *historyVariables*

  A repository of [HistoryVariable](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyvariablepyc.htm?ContextScope=all) objects specifying the history request label. The repository is read-only.

- *steps*

  A repository of [OdbDataStep](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatasteppyc.htm?ContextScope=all) objects specifying the list of steps. The repository is read-only.

- *instances*

  A repository of [OdbDataInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatainstancepyc.htm?ContextScope=all) objects specifying the list of instances. The repository is read-only.

- *materials*

  A repository of [OdbDataMaterial](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatamaterialpyc.htm?ContextScope=all) objects specifying the list of materials. The repository is read-only.

- *sections*

  A repository of [OdbDataSection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatasectionpyc.htm?ContextScope=all) objects specifying the list of sections. The repository is read-only.

- *elementSets*

  A repository of [OdbDataElementSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdataelementsetpyc.htm?ContextScope=all) objects specifying the list of element sets. The repository is read-only.

- *nodeSets*

  A repository of [OdbDataNodeSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatanodesetpyc.htm?ContextScope=all) objects specifying the list of node sets. The repository is read-only.

- *surfaceSets*

  A repository of [OdbDataSurfaceSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatasurfacesetpyc.htm?ContextScope=all) objects specifying the list of surface sets. The repository is read-only.

- *datumCsyses*

  A repository of [OdbDataDatumCsys](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatadatumcsyspyc.htm?ContextScope=all) objects specifying the list of coordinate systems defined in the model. The repository is read-only.

- *kinematicCouplings*

  A repository of [CouplingConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-couplingconstraintpyc.htm?ContextScope=all) objects specifying the list of kinematic couplings. The repository is read-only.

- *distributingCouplings*

  A repository of [CouplingConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-couplingconstraintpyc.htm?ContextScope=all) objects specifying the list of distributing couplings. The repository is read-only.

- *shellSolidCouplings*

  A repository of [CouplingConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-couplingconstraintpyc.htm?ContextScope=all) objects specifying the list of shellsolid couplings. The repository is read-only.

- *rigidbodies*

  A repository of [RigidBodyConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rigidbodyconstraintpyc.htm?ContextScope=all) objects specifying the list of rigid body constraints. The repository is read-only.

- *multiPointConstraints*

  A repository of [MpcConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mpcconstraintpyc.htm?ContextScope=all) objects specifying the list of multipoint constraints. The repository is read-only.

- *ties*

  A repository of [TieConstraint](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tieconstraintpyc.htm?ContextScope=all) objects specifying the list of Tie constraints. The repository is read-only.

- *diagnosticData*

  An [OdbDiagnosticData](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdiagnosticdatapyc.htm?ContextScope=all) object.