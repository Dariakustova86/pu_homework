from modeller import * 
from modeller.automodel import * 
log.verbose() 
env = environ() 

env.io.atom_files_directory = ['.', '../atom_files']
a = automodel(env,
    alnfile = 'sge.ali', 
    knowns = '3brx', 
    sequence = 'sge',
    assess_methods = assess.normalized_dope) 
a.starting_model= 1 
a.ending_model = 10 
 
a.make() 