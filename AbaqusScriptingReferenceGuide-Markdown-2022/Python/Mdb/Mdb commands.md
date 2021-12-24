# Mdb commands

The following command upgrades a model database (.cae) to the current release and writes the upgraded model database to a new file.

## upgradeMdb



This method upgrades an existing Mdb object to the current release and writes the upgraded version of the Mdb object to a file. In addition, Abaqus/CAE writes information about the status of the upgrade to the log file ( *upgradedMdbPath*.log ).



### Path

upgradeMdb

### Required arguments

- *existingMdbPath*

  A String specifying the path to the file containing the model database to be upgraded.

- *upgradedMdbPath*

  A String specifying the path to the file that will contain the upgraded model database.

### Optional arguments

None.

### Return value

None.

### Exceptions

- If the model database upgrade fails:

  MdbError: cannot convert file



## CombineOptResults



This method combines the results from existing ODB files for each optimization cycle and writes a merged ODB file.



### Path

CombineOptResults

### Required arguments

- *optResultLocation*

  A String specifying the path to the folder in which optimization results are present.

### Optional arguments

- *optIter*

  A Symbolic Constant to specify the optimization cycles from which the results should be merged. The possible values are INITIAL_AND_LAST, NONE, ALL, LAST, EVERY_NCYCLES, SPECIFY.The default value is INITIAL_AND_LAST.

- *nValues*

  An Int or a tuple of Ints specifying the optimization cycles from which the results should be merged. This argument is used only when EVERY_NCYCLES or SPECIFY is selected for *optIter*.The default value is ALL.

- *models*

  A tuple of strings specifying the list of *models* for which the merging of results is performed.The default value is ALL.

- *steps*

  A tuple of strings specifying the list of steps from the selected *models* to be included in the odb merge.The default value is ALL.

- *analysisFieldVariables*

  A tuple of strings specifying the list of *analysisFieldVariables* to be included in the odb merge.The default value is ALL.

- *includeResultsFrom*

  A Symbolic Constant to specify the target odb to which the results will be merged. The possible values are ORIGINAL_MODEL, FIRST or LAST.The default value is FIRST.

- *originalModel*

  A String to specify the path of target odb if *includeResultsFrom* is set to ORIGINAL_MODEL.