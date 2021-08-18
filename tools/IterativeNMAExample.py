from robosample import *
import glob

SysIn = "./demo/ADK/receptor"
iMod_Exec = ""		##You'll have to fill this one up yourself :)

prmtop = AmberPrmtopFile(SysIn + ".prmtop")
inpcrd = AmberInpcrdFile(SysIn + ".rst7")

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
	
simulation = Simulation(prmtop.topology, system, integrator, platform, properties, addDefaultWorld=False)
simulation.context.setPositions(inpcrd.positions)
simulation.reporters.append(PDBReporter('robots/', 10))

simulation.addWorld(regionType='all', rootMobility='Weld', timestep=0.0006, mdsteps=5, argJointType='Pin', samples=1)
simulation.addWorld(regionType='premade',  rootMobility='Weld', timestep=0.002, mdsteps=25, argJointType='Pin', samples=1) #Premade doesn't generate any flexfile, assumes you have a premade one. You add this type of world last if you want to use NMAStep.

simulation.NMAStep(simulation.context.mdtrajTraj, 10000, 1000, iMod_Exec, 1)
