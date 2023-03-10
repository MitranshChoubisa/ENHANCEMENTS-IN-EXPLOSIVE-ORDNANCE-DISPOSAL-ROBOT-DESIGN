import pybullet as p
cin = p.connect(p.SHARED_MEMORY)
if (cin < 0):
    cin = p.connect(p.GUI)
objects = [p.loadURDF("plane.urdf", 0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,1.000000)]
objects = [p.loadURDF("quadruped/minitaur_v1.urdf", 1.013874,-1.000196,0.166346,-0.001119,0.001254,0.199664,0.979863)]
ob = objects[0]
jointPositions=[ 0.000000, 1.569829, 0.000000, -2.182699, 1.569978, 0.000000, -2.190614, 1.569734, 0.000000, -2.183725, 1.570131, 0.000000, -2.187749, 0.000000, -1.570451, 0.000000, 2.182866, -1.569392, 0.000000, 2.200592, -1.568860, 0.000000, 2.182572, -1.569346, 0.000000, 2.201720 ]
for jointIndex in range (p.getNumJoints(ob)):
	p.resetJointState(ob,jointIndex,jointPositions[jointIndex])

cid0 = p.createConstraint(1,19,1,16,p.JOINT_POINT2POINT,[0.000000,0.000000,0.000000],[0.000000,0.005000,0.100000],[0.000000,0.010000,0.100000],[0.000000,0.000000,0.000000,1.000000],[0.000000,0.000000,0.000000,1.000000])
p.changeConstraint(cid0,maxForce=1000.000000)
cid1 = p.createConstraint(1,3,1,6,p.JOINT_POINT2POINT,[0.000000,0.000000,0.000000],[0.000000,0.005000,0.100000],[0.000000,0.010000,0.100000],[0.000000,0.000000,0.000000,1.000000],[0.000000,0.000000,0.000000,1.000000])
p.changeConstraint(cid1,maxForce=1000.000000)
cid2 = p.createConstraint(1,25,1,22,p.JOINT_POINT2POINT,[0.000000,0.000000,0.000000],[0.000000,0.005000,0.100000],[0.000000,0.010000,0.100000],[0.000000,0.000000,0.000000,1.000000],[0.000000,0.000000,0.000000,1.000000])
p.changeConstraint(cid2,maxForce=1000.000000)
cid3 = p.createConstraint(1,9,1,12,p.JOINT_POINT2POINT,[0.000000,0.000000,0.000000],[0.000000,0.005000,0.100000],[0.000000,0.010000,0.100000],[0.000000,0.000000,0.000000,1.000000],[0.000000,0.000000,0.000000,1.000000])
p.changeConstraint(cid3,maxForce=1000.000000)
p.setGravity(0.000000,0.000000,-10.000000)
p.stepSimulation()
p.disconnect()