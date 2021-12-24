# InputFile object

The InputFile object is used to store the definitions in an Abaqus input file. InputFile objects can be created using the methods described in this section.

## Access

```
import inpParser
```

## InputFile(...)



This method creates an InputFile object by reading an Abaqus input file.



### Path

inpParser.InputFile

### Required arguments

- *file*

  A String specifying the path to the input file.

### Optional arguments

- *directory*

  A String specifying the path to the directory containing the input file.

### Return value

An InputFile object.

### Exceptions

None.



## parse(...)



This method parses the input file associated with the InputFile object.



### Optional arguments

- *organize*

  A Boolean specifying whether keywords should be organized into suboptions. The default is False.

- *verbose*

  A Boolean specifying whether verbose output is to be printed. If *verbose* is True, information about fatal errors is printed. If no fatal errors occur, there is no output. The default is False.

- *bulk*

  A Boolean specifying whether the input file includes bulk data that should be parsed. The default is True.

- *usePyArray*

  A Boolean specifying that parse method can return an AbaqusNDarray object for a keyword data value. In cases where large amounts of numerical data (i.e., large node arrays) are expected, it is recommended that you use the option usePyArray=True. The default is False.

### Return value

A KeywordSequence object.

### Exceptions

If you parse an input file more than once, a ValueError is raised for each subsequent parsing.



## Members

The InputFile object has the following members:

- *file*

  A String specifying the source file name of the Abaqus input file.

- *directory*

  A String specifying the directory where the input file is located.

- *includes*

  A sequence of Strings specifying any additional input files included in the specified input file.

- *missingIncludes*

  A sequence of Strings for input files included in the specified input file that could not be located.