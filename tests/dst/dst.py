from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import *

executeOnCaeStartup()

# PART
sketch = mdb.models['Model-1'].ConstrainedSketch(name='SKETCH-SOIL', sheetSize=0.1)
sketch.rectangle(point1=(0.0, 0.0), point2=(0.025, 0.025))
mdb.models['Model-1'].Part(name='PART-SOIL', dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-SOIL'].BaseSolidExtrude(sketch=sketch, depth=0.025)
del mdb.models['Model-1'].sketches['SKETCH-SOIL']

sketch = mdb.models['Model-1'].ConstrainedSketch(name='SKETCH-SOLID', sheetSize=0.1)
sketch.rectangle(point1=(0.0, 0.0), point2=(0.05, 0.05))
mdb.models['Model-1'].Part(name='PART-SOLID', dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['PART-SOLID'].BaseSolidExtrude(sketch=sketch, depth=0.05)
del mdb.models['Model-1'].sketches['SKETCH-SOLID']

# ASSEMBLY
assembly = mdb.models['Model-1'].rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
assembly.Instance(name='INSTANCE-SOIL', part=mdb.models['Model-1'].parts['PART-SOIL'], dependent=ON)
assembly.Instance(name='INSTANCE-SOLID', part=mdb.models['Model-1'].parts['PART-SOLID'], dependent=ON)
assembly.translate(instanceList=('INSTANCE-SOIL',), vector=((0.05 - 0.025) / 2, (0.05 - 0.025) / 2, 0.05))

# SETS
part = mdb.models['Model-1'].parts['PART-SOIL']
part.Surface(side1Faces=part.faces.findAt(((0.025 / 2, 0.025 / 2, 0),), ), name='SURFACE-SOIL-Z0')
part.Surface(side1Faces=part.faces.findAt(((0.025 / 2, 0.025 / 2, 0.025),), ), name='SURFACE-SOIL-Z1')
part.Set(cells=part.cells.findAt(((0.025 / 2, 0.025 / 2, 0.025 / 2),), ), name='SET-SOIL')
part.Set(faces=part.faces.findAt(((0, 0.025 / 2, 0.025 / 2),), ), name='SET-SOIL-X0')
part.Set(faces=part.faces.findAt(((0.025 / 2, 0, 0.025 / 2),), ), name='SET-SOIL-Y0')
part.Set(faces=part.faces.findAt(((0.025 / 2, 0.025 / 2, 0),), ), name='SET-SOIL-Z0')
part.Set(faces=part.faces.findAt(((0.025, 0.025 / 2, 0.025 / 2),), ), name='SET-SOIL-X1')
part.Set(faces=part.faces.findAt(((0.025 / 2, 0.025, 0.025 / 2),), ), name='SET-SOIL-Y1')
part.Set(faces=part.faces.findAt(((0.025 / 2, 0.025 / 2, 0.025),), ), name='SET-SOIL-Z1')
part = mdb.models['Model-1'].parts['PART-SOLID']
part.Surface(side1Faces=part.faces.findAt(((0.05 / 2, 0.05 / 2, 0),), ), name='SURFACE-SOLID-Z0')
part.Surface(side1Faces=part.faces.findAt(((0.05 / 2, 0.05 / 2, 0.05),), ), name='SURFACE-SOLID-Z1')
part.Set(cells=part.cells.findAt(((0.05 / 2, 0.05 / 2, 0.05 / 2),), ), name='SET-SOLID')
part.Set(faces=part.faces.findAt(((0, 0.05 / 2, 0.05 / 2),), ), name='SET-SOLID-X0')
part.Set(faces=part.faces.findAt(((0.05 / 2, 0, 0.05 / 2),), ), name='SET-SOLID-Y0')
part.Set(faces=part.faces.findAt(((0.05 / 2, 0.05 / 2, 0),), ), name='SET-SOLID-Z0')
part.Set(faces=part.faces.findAt(((0.05, 0.05 / 2, 0.05 / 2),), ), name='SET-SOLID-X1')
part.Set(faces=part.faces.findAt(((0.05 / 2, 0.05, 0.05 / 2),), ), name='SET-SOLID-Y1')
part.Set(faces=part.faces.findAt(((0.05 / 2, 0.05 / 2, 0.05),), ), name='SET-SOLID-Z1')

# Materials
mdb.models['Model-1'].Material(name='MATERIAL-SOIL')
mdb.models['Model-1'].materials['MATERIAL-SOIL'].Elastic(table=((4e4, 0.0),))
mdb.models['Model-1'].materials['MATERIAL-SOIL'].Density(table=((1700,),))

mdb.models['Model-1'].Material(name='MATERIAL-SOLID')
mdb.models['Model-1'].materials['MATERIAL-SOLID'].Elastic(table=((2e8, 0.0),))
mdb.models['Model-1'].materials['MATERIAL-SOLID'].Density(table=((2000,),))

# SECTIONS
mdb.models['Model-1'].HomogeneousSolidSection(name='SECTION-SOIL', material='MATERIAL-SOIL', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='SECTION-SOLID', material='MATERIAL-SOLID', thickness=None)
# Sections assignment
part = mdb.models['Model-1'].parts['PART-SOIL']
part.SectionAssignment(region=part.sets['SET-SOIL'], sectionName='SECTION-SOIL', offset=0.0,
                       offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
part = mdb.models['Model-1'].parts['PART-SOLID']
part.SectionAssignment(region=part.sets['SET-SOLID'], sectionName='SECTION-SOLID', offset=0.0,
                       offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

# STEP
mdb.models['Model-1'].StaticStep(name='INITIAL-STRESS', previous='Initial', maxNumInc=1000, initialInc=0.001, minInc=1e-5,
                                 maxInc=1, matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC)
mdb.models['Model-1'].StaticStep(name='SHEAR', previous='INITIAL-STRESS', maxNumInc=1000, initialInc=0.001, minInc=1e-5,
                                 maxInc=1, matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC)

# INTERACTION
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=ON,
                                                                        constraintEnforcementMethod=DEFAULT)
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, pressureDependency=OFF,
    temperatureDependency=OFF, dependencies=0, table=((0.1, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION,
    fraction=0.005, elasticSlipStiffness=None)

assembly = mdb.models['Model-1'].rootAssembly
solid = assembly.instances['INSTANCE-SOLID'].surfaces['SURFACE-SOLID-Z1']
soil = assembly.instances['INSTANCE-SOIL'].surfaces['SURFACE-SOIL-Z0']
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', createStepName='Initial', master=solid, slave=soil,
                                                 sliding=FINITE, thickness=ON, interactionProperty='IntProp-1',
                                                 adjustMethod=NONE, initialClearance=OMIT, datumAxis=None,
                                                 clearanceRegion=None)
# LOAD
# VERTICAL PRESSURE
region = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOIL'].surfaces['SURFACE-SOIL-Z1']
mdb.models['Model-1'].Pressure(name='SOIL-VERTICAL-PRESSURE', createStepName='INITIAL-STRESS', region=region,
                               distributionType=UNIFORM, field='', magnitude=310, amplitude=UNSET)
# PREDEFINED STRESS
region = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOIL'].sets['SET-SOIL']
mdb.models['Model-1'].Stress(name='SOIL-PREDEFINED-STRESS', region=region, distributionType=UNIFORM,
                             sigma11=-310, sigma22=-310, sigma33=-310, sigma12=0, sigma13=0, sigma23=0)
# RIGID BOGY
feature = mdb.models['Model-1'].parts['PART-SOLID'].ReferencePoint(point=(0.0, 0.0, 0.0))
RP = mdb.models['Model-1'].parts['PART-SOLID'].referencePoints[feature.id]
mdb.models['Model-1'].parts['PART-SOLID'].Set(referencePoints=(RP,), name='SET-RP')
region1 = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOLID'].sets['SET-RP']
region2 = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOLID'].sets['SET-SOLID']
mdb.models['Model-1'].RigidBody(name='RIGID-BODY-SOLID', refPointRegion=region1, bodyRegion=region2)

# BOUNDARY CONDITION
RP = mdb.models['Model-1'].rootAssembly.instances['INSTANCE-SOLID'].sets['SET-RP']
displacementBC = mdb.models['Model-1'].DisplacementBC(name='BC-RP', createStepName='Initial', region=RP,
                                                      u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, amplitude=UNSET,
                                                      distributionType=UNIFORM, fieldName='', localCsys=None)
displacementBC.setValuesInStep(stepName='SHEAR', u1=0.006, u2=0, u3=0, ur1=0, ur2=0, ur3=0)
# CONFINING BOUNDARY CONDITION
X0 = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-X0']
mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-X0', createStepName='Initial', region=X0,
                                     u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET,
                                     fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
X1 = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-X1']
mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-X1', createStepName='Initial', region=X1,
                                     u1=0.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET,
                                     fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
Y0 = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-Y0']
mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-Y0', createStepName='Initial', region=Y0,
                                     u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET,
                                     fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
Y1 = assembly.instances['INSTANCE-SOIL'].sets['SET-SOIL-Y1']
mdb.models['Model-1'].DisplacementBC(name='BC-SOIL-Y1', createStepName='Initial', region=Y1,
                                     u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET,
                                     fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)

# MESH
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN,
                          secondOrderAccuracy=OFF, hourglassControl=ENHANCED, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part = mdb.models['Model-1'].parts['PART-SOIL']
cells = part.cells.findAt(((0.025 / 2, 0.025 / 2, 0.025 / 2),), )
part.setElementType(regions=(cells,), elemTypes=(elemType1, elemType2, elemType3))
part.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
part.generateMesh()
part = mdb.models['Model-1'].parts['PART-SOLID']
cells = part.cells.findAt(((0.05 / 2, 0.05 / 2, 0.05 / 2),), )
part.setElementType(regions=(cells,), elemTypes=(elemType1, elemType2, elemType3))
part.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
part.generateMesh()

# OUTPUT REQUESTS
mdb.models['Model-1'].FieldOutputRequest(
    name='F-Output-1', createStepName='SHEAR', timeInterval=0.01,
    variables=('S', 'E', 'LE', 'U', 'RF', 'RT', 'RM', 'P', 'CSTRESS', 'CDISP', 'CFORCE', 'CNAREA', 'CSTATUS'))
region = mdb.models['Model-1'].rootAssembly.allInstances['INSTANCE-SOLID'].sets['SET-RP']
mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-1', createStepName='SHEAR', variables=('U1', 'RF1'),
                                           region=region, sectionPoints=DEFAULT, rebar=EXCLUDE)

# JOB
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0,
        queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=DOUBLE,
        nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
        userSubroutine='', scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].writeInput()
# mdb.jobs['Job-1'].submit()
# mdb.jobs['Job-1'].waitForCompletion()

mdb.saveAs('dst.cae')
