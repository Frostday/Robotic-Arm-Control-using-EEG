import pybullet as p
import pybullet_data
from time import sleep
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,0)

startPos = [0,0,0]
startOrientation = p.getQuaternionFromEuler([0,0,0])
simulationId = p.loadURDF("urdf-practice/basic_arm.urdf", startPos, startOrientation)
# boxId = p.loadURDF("r2d2.urdf",startPos, startOrientation)
for i in range (10000):
    # maxForce = 0
    # mode = p.VELOCITY_CONTROL
    # p.setJointMotorControl2(simulationId, 1, controlMode=mode, force=maxForce)
    p.stepSimulation()
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(simulationId)
print(cubePos,cubeOrn)
p.disconnect()

number_of_joints = p.getNumJoints(simulationId)
for joint_number in range(number_of_joints):
    info = p.getJointInfo(simulationId, joint_number)
    print(info)

sleep(20)
