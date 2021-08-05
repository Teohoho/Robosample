from robosample import *
import glob

SysIn = "demo/ADK/receptor"

prmtop = AmberPrmtopFile(SysIn + '.prmtop')
inpcrd = AmberInpcrdFile(SysIn + '.rst7')

print("Simulating", prmtop.topologyFNs, inpcrd.positionsFNs)
	
# Hardware platform
platform = Platform.getPlatformByName('GPU')
properties={'nofThreads': 1}

# Create a Robosample system by calling createSystem on prmtop
system = prmtop.createSystem(createDirs = True,
        nonbondedMethod = "CutoffPeriodic",
        nonbondedCutoff = 1.44*nanometer,
        constraints = None,
        rigidWater = True,
        implicitSolvent = True,
        soluteDielectric = 1.0,
        solventDielectric = 78.5,
        removeCMMotion = False
)

integrator = HMCIntegrator(300*kelvin,   # Temperature of head bath
	                           0.006*picoseconds) # Time step
	
simulation = Simulation(prmtop.topology, system, integrator, platform, properties, addDefaultWorld=True)
simulation.context.setPositions(inpcrd.positions)
simulation.reporters.append(PDBReporter('robots/', 10))

simulation.addWorld(regionType='premade', region=[[1,2]],  rootMobility='Weld', timestep=0.005, mdsteps=1, argJointType='Pin', subsets=['rama', 'side'], samples=1) #Premade doesn't generate any flexfile, assumes you have a premade one

simulation.NMAStep(simulation.context.mdtrajTraj, 6000, 100, "/home/teo/Laurentiu/RobosampleDev/NMA/RS_NMA/iMod/iMOD_v1.04_Linux/bin/imode_gcc", 5)
