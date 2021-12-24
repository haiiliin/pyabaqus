# OdbNumericalProblemSummary object

The OdbNumericalProblemSummary object stores the numerical problem summary of a job.

## Access

```
        import visualization
        session.odbData[name].diagnosticData.numericalProblemSummary
      
```

## Members

The OdbNumericalProblemSummary object has the following members:

- *convergedNegativeEigenValues*

  A boolean specifying whether negative eigenvalues converged during the analysis. This attribute is read-only.

- *convergedNumericalSingularities*

  A boolean specifying whether numerical singularities converged during the analysis. This attribute is read-only.

- *convergedZeroPivots*

  A boolean specifying whether pivot points converged during the analysis. This attribute is read-only.

- *numberOfZeroPivots*

  An int specifying the number of zero pivots. This attribute is read-only.

- *numberOfNumericalSingularities*

  An int specifying the number of numerical singularities. This attribute is read-only.

- *numberOfNegativeEigenValues*

  An int specifying the number of negative eigenvalues. This attribute is read-only.