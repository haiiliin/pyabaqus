from os import environ
from abaqus import *
from driverUtils import *
from abaqusConstants import *

executeOnCaeStartup()

environ['ABAQUS_BAT_PATH'] = 'C:\\SIMULIA\\Commands\\abaqus'
environ['ABAQUS_BAT_SETTING'] = 'noGUI'

sketch = mdb.models['Model-1'].ConstrainedSketch(name='SKETCH-SOIL', sheetSize=0.1)
sketch.rectangle(point1=(0.0, 0.0), point2=(0.025, 0.025))
mdb.models['Model-1'].Part(name='PART-SOIL', dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-SOIL'].BaseSolidExtrude(sketch=sketch, depth=0.025)
del mdb.models['Model-1'].sketches['SKETCH-SOIL']

mdb.saveAs(r'C:\Users\user\OneDrive\Documents\GitHub\PyAbaqusBase\dst.cae')
