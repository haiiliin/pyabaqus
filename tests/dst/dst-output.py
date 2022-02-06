from abaqus import *
from abaqusConstants import *
from driverUtils import executeOnCaeStartup
import numpy as np

executeOnCaeStartup()

# OPEN OUTPUT DATABASE FILE
odb = session.openOdb(name='Job-1.odb')

# TODO CONTACT SHEAR1
session.xyDataListFromField(odb=odb, outputPosition=ELEMENT_NODAL, variable=(('CSHEAR1', ELEMENT_NODAL),),
                            elementSets=("INSTANCE-SOIL.SET-SOIL-Z0",))

# TODO U1_RP
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', NODAL, ((COMPONENT, 'U1'),)),),
                            nodeSets=("INSTANCE-SOLID.SET-RP",))

# TODO RF1_RP
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF', NODAL, ((COMPONENT, 'RF1'),)),),
                            nodeSets=("INSTANCE-SOLID.SET-RP",))

# TODO CSLIP1
session.xyDataListFromField(odb=odb, outputPosition=ELEMENT_NODAL, variable=(('CSLIP1', ELEMENT_NODAL),),
                            elementSets=("INSTANCE-SOIL.SET-SOIL-Z0",))

# TODO U3_TOP
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                            nodeSets=("INSTANCE-SOIL.SET-SOIL-Z1",))

CSHEAR1, GAMMA_NORM, U1_RP, RF1_RP, CSLIP1, EPSN_FRIC, U3 = [], [], [], [], [], [], []
for key, xyDataObject in session.xyDataObjects.items():
    if key.startswith('CSHEAR1'):
        CSHEAR1.append(xyDataObject)
    elif key.startswith('U:U1'):
        U1_RP.append(xyDataObject)
    elif key.startswith('RF:RF1'):
        RF1_RP.append(xyDataObject)
    elif key.startswith('CSLIP1'):
        CSLIP1.append(xyDataObject)
    elif key.startswith('U:U3'):
        U3.append(xyDataObject)
        
if not os.path.exists('DATA'):
    os.mkdir('DATA')

TIME = np.mean(np.array(CSHEAR1), axis=0)[:, 0]
CSHEAR1_AVG = np.mean(np.array(CSHEAR1), axis=0)[:, 1]
U1_RP_AVG = np.mean(np.array(U1_RP), axis=0)[:, 1]
RF1_RP_AVG = np.mean(np.array(RF1_RP), axis=0)[:, 1]
CSLIP1_AVG = np.mean(np.array(CSLIP1), axis=0)[:, 1]
U3_AVG = np.mean(np.array(U3), axis=0)[:, 1]

DATA = [TIME, CSHEAR1_AVG, U1_RP_AVG, RF1_RP_AVG, CSLIP1_AVG, U3_AVG]
DATA = np.array(DATA).T
np.savetxt('data.csv', DATA, header='TIME,CSHEAR1,U1_RP,RF1_RP,CSLIP1,U3_TOP', delimiter=',', comments='')
