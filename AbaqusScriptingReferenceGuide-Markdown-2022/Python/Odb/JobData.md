# JobData object

The JobData object describes the context in which the analysis was run.

## Access

```
import odbAccess
session.odbs[name].jobData
```

## Members

The JobData object has the following members:

- *name*

  A String specifying the name of the job.

- *analysisCode*

  A SymbolicConstant specifying the analysis code. Possible values are ABAQUS_STANDARD, ABAQUS_EXPLICIT, and UNKNOWN_ANALYSIS_CODE.

- *precision*

  A SymbolicConstant specifying the precision. Only SINGLE_PRECISION is currently supported. Possible values are DOUBLE_PRECISION and SINGLE_PRECISION.

- *version*

  A String specifying the release of the analysis code.

- *creationTime*

  A String specifying the date and time at which the analysis was run.

- *modificationTime*

  A String specifying the date and time at which the database was last modified.

- *machineName*

  A String specifying the name of the machine on which the analysis was run.

- *productAddOns*

  A String specifying an odb_Sequence of productAddOns. Possible values are: Possible values are AQUA, DESIGN, BIORID, CEL, SOLITER, and CAVPARALLEL.