# CombinedTermDesignResponse object

The CombinedTermDesignResponse object defines a combined-term design response.

The CombinedTermDesignResponse object is derived from the [DesignResponse](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designresponsepyc.htm?ContextScope=all) object.

## Access

```
        import optimization
        mdb.models[name].optimizationTasks[name].designResponses[name]
      
```

## CombinedTermDesignResponse(...)



This method creates a CombinedTermDesignResponse object.



### Path

```
          mdb.models[name].optimizationTasks[name].CombinedTermDesignResponse
        
```

### Required arguments

- *name*

  A String specifying the design response repository key.

- *terms*

  A sequence of Strings specifying the names of the design responses to combine.

### Optional arguments

- *filterMaxRadius*

  None or a sequence of Floats specifying the maximum radius of influence used when *method* is FILTER. The default value is None.

- *filterExponent*

  A Float specifying the exponent used when *method* is FILTER. The default value is 1.0.

- *filterRadiusReduction*

  A Float specifying the reduction of the radius depending on surface bending, used when *method* is FILTER. The default value is 0.2.

- *highCutOff*

  None or a sequence of Floats specifying the upper bound of the vector value used when *method* is CUT_OFF. All values greater than the *highCutOff* are set to the *highCutOff* value. The default value is None.

- *lowCutOff*

  A Float specifying the lower bound of the vector value used when *method* is CUT_OFF. All values less than the *lowCutOff* are treated as 0. The default value is 0.0.

- *method*

  A SymbolicConstant specifying the method used to combine selected design responses. Possible values are:

  - ABSOLUTE_DIFFERENCE
  - ABSOLUTE_VALUE
  - ADD
  - COSINE
  - CUT_OFF
  - DELTA_OVER_1_ITERATION
  - DELTA_OVER_2_ITERATIONS
  - DELTA_OVER_3_ITERATIONS
  - DELTA_OVER_4_ITERATIONS
  - DELTA_OVER_5_ITERATIONS
  - DELTA_OVER_6_ITERATIONS
  - DIVIDE
  - EXPONENTIAL
  - FILTER
  - INTEGER
  - LOG
  - MAXIMUM
  - MINIMUM
  - MULTIPLY
  - NATURAL_LOG
  - NEAREST_INTEGER
  - NORM
  - NORM_FIRST
  - NTH_POWER
  - NTH_ROOT
  - SIGN
  - SINE
  - SQUARE_ROOT
  - SUBTRACT
  - TANGENT
  - WEIGHTED_ADD

  The default value is ADD.

- *weights*

  A sequence of Floats specifying the weights to apply to the list of design responses used when *method* is WEIGHTED_ADD. The default value is an empty sequence.

### Return value

A CombinedTermDesignResponse object.

### Exceptions

None.



## setValues(...)



This method modifies the CombinedTermDesignResponse object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [CombinedTermDesignResponse ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-combinedtermdesignresponsepyc.htm?ContextScope=all#simaker-combinedtermdesignresponsecombinedtermdesignresponspyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The CombinedTermDesignResponse object has members with the same names and descriptions as the arguments to the [CombinedTermDesignResponse ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-combinedtermdesignresponsepyc.htm?ContextScope=all#simaker-combinedtermdesignresponsecombinedtermdesignresponspyc)method.