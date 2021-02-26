from TransportTask.code import data_structure as ds
from TransportTask.code.algorithms import north_west_method, calculate_function
from TransportTask.code import potential_method as pm

task = ds.TransportTask([[3, 11, 3, 10], [1, 9, 2, 8], [7, 4, 10, 5]], [3, 6, 5, 6], [7, 4, 9])
# print(task.matrix_cost)
# print(task.vector_importer)
# print(task.vector_exporter)
start_plan = north_west_method(task)
# print(task.matrix_cost)
print("start plan")
for line in start_plan:
    print(line)
print("cost matrix")
for line in task.matrix_cost:
    print(line)
print("vector importer ", task.vector_importer)
print("vector exporter", task.vector_exporter)
print(calculate_function(start_plan, task.matrix_cost))
res_plan = pm.run_potential_method(task, start_plan, task.matrix_cost)
print()
print("result of calculation: ", calculate_function(res_plan, task.matrix_cost))
