# MullinsEffect object

The MullinsEffect specifies properties for mullins data.

## Access

```
import material
mdb.models[name].materials[name].mullinsEffect
import odbMaterial
session.odbs[name].materials[name].mullinsEffect
```

## Members

The MullinsEffect object can have the following members:

- *definition*

  A SymbolicConstant specifying the method of specifying the data. Possible values are USER, CONSTANTS, and TEST_DATA. The default value is CONSTANTS.

- *temperatureDependency*

  A Boolean specifying whether the data depend on temperature. The default value is OFF.

- *dependencies*

  An Int specifying the number of field variable dependencies. The default value is 0.

- *properties*

  An Int specifying the number of property values needed as data for the user-defined hyperelastic material. The default value is 0.

- *table*

  A tuple of tuples of Floats specifying the items described below. The default value is an empty sequence.

- *uniaxialTests*

  A [UniaxialTestDataArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-uniaxialtestdatapyc.htm?ContextScope=all) object.

- *biaxialTests*

  A [BiaxialTestDataArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-biaxialtestdatapyc.htm?ContextScope=all) object.

- *planarTests*

  A [PlanarTestDataArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-planartestdatapyc.htm?ContextScope=all) object.