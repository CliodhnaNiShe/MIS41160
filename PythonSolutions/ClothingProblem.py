import xpress as xp

xp.init('C:/xpressmp/bin/xpauth.xpr')


#Implementation of the Pottery problem: two decision variables, two constraints

problem = xp.problem(name="Clothing Problem") # Create and name the Problem

#Step 1: declare the decision variables
x_1 = xp.var(name = 'coat_quantity', lb = 0, vartype = xp.continuous)
x_2 = xp.var(name = 'jacket_quantity', lb = 0, vartype = xp.continuous)


#############################LP Model#######################
Profit = 50*x_1 + 40*x_2  #Objective function
wool_constraint = 3*x_1 + 5*x_2 <= 150 # Wool sq m availability
labour_constraint = 10*x_1 + 4*x_2 <= 200 # hours of labour availability
###################################################################


problem.addVariable(x_1) # Add the bowl variable to the problem
problem.addVariable(x_2) # Add the mug variable to the problem
problem.addConstraint(labour_constraint) # Add the labour constraint to the problem
problem.addConstraint(wool_constraint) # Add the wool constraint to the problem
problem.setObjective(Profit, sense=xp.maximize) # Add the objective function to the problem


problem.solve()  # Solve the problem

solution = problem.getSolution()  # Get the solution values
objective_value = problem.getObjVal()

print("\n")
print("Make {} coat(s)".format(solution[0]))
print("Make {} jacket(s)".format(solution[1]))
print("Best profit is €{} ".format(objective_value))