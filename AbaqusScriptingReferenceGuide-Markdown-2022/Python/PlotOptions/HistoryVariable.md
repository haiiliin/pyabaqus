# HistoryVariable object

The HistoryVariable object stores history data.

## Access

```
import visualization
session.odbData[name].historyVariables[i]
```

## Members

The HistoryVariable object has the following members:

- *name*

  A String specifying the history request label. This String is read-only.

- *legendLabel*

  A String specifying the legend text. This String is read-only.

- *steps*

  A tuple of (String, Int, SymbolicConstant) tuples specifying the steps. This sequence is read-only. Each inner sequence contains the following elements:*stepLabel*: A String specifying the step label.*stepNumber*: An Int specifying the step number.*procedureDomain*: A SymbolicConstant specifying the analysis type of the step, which can have these values: “TIME,” “FREQUENCY,” or “MODAL.”