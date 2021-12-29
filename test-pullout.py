from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import *

executeOnCaeStartup()

os.chdir('C:\\Users\\user\\OneDrive\\Documents\\GitHub\\PyAbaqusBase\\tests\\pullout')

# PART
mdb.models['Model-1'].ConstrainedSketchBase(name='SKETCH-NAIL', sheetSize=1.2)
mdb.models['Model-1'].sketches['SKETCH-NAIL'].ArcByCenterEnds(center=(0.0, 0.0), direction=CLOCKWISE, point1=(-0.05, 0.0), point2=(0.05, 0.0))
mdb.models['Model-1'].sketches['SKETCH-NAIL'].Line(point1=(0.05, 0.0), point2=(-0.05, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='PART-NAIL', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-NAIL'].BaseSolidExtrude(depth=1.2, sketch=mdb.models['Model-1'].sketches['SKETCH-NAIL'])
del mdb.models['Model-1'].sketches['SKETCH-NAIL']
mdb.models['Model-1'].ConstrainedSketchBase(name='SKETCH-SOIL', sheetSize=1.0)
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-0.05, 0.0), point2=(-0.05 * 2, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-0.05 * 2, 0.0), point2=(-0.8 + 0.4, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-0.8 + 0.4, 0.0), point2=(-0.8 + 0.4, 0.05 * 2))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-0.8 + 0.4, 0.05 * 2), point2=(-0.8 + 0.4, 0.3))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-0.8 + 0.4, 0.3), point2=(-0.05 * 2, 0.3))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(-0.05 * 2, 0.3), point2=(0.05 * 2, 0.3))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(0.05 * 2, 0.3), point2=(0.4, 0.3))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(0.4, 0.3), point2=(0.4, 0.05 * 2))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(0.4, 0.05 * 2), point2=(0.4, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(0.4, 0.0), point2=(0.05 * 2, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].Line(point1=(0.05 * 2, 0.0), point2=(0.05, 0.0))
mdb.models['Model-1'].sketches['SKETCH-SOIL'].ArcByCenterEnds(center=(0.0, 0.0), direction=CLOCKWISE, point1=(-0.05, 0.0), point2=(0.05, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='PART-SOIL', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-SOIL'].BaseSolidExtrude(depth=1.0, sketch=mdb.models['Model-1'].sketches['SKETCH-SOIL'])
del mdb.models['Model-1'].sketches['SKETCH-SOIL']
