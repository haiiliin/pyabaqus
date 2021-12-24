# Keyword object

The Keyword object is used to store a keyword definition from an Abaqus input file.

Keyword objects are returned via the InputFile.parse() method.

## Access

```
import inpParser
```

## Members

The InputFile object has the following members:

- *name*

  A String specifying the name of the keyword.

- *parameter*

  A Dictionary of Strings specifying the keyword parameters.

- *data*

  A sequence of sequences or an AbaqusNDarray object specifying the keyword data. The type of the leaf objects depends on the keyword. The AbaqusNDarray object is returned only if the data is suitable and if the InputFile.parse() method was called with the option usePyArray=True. In cases where large amounts of numerical data (i.e., large node arrays) are expected, it is recommended that you use the option usePyArray=True.

- *suboptions*

  A KeywordSequence specifying the suboptions of the keyword.

- *comments*

  A sequence of Strings specifying the comments.