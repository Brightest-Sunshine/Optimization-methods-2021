from TransportTask.code.data_structure import TransportTask, OneLineEquation
from TransportTask.code.algorithms import north_west_method, calculate_function

LINE = 0
COL = 1
directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]  # up right left  down


def check_filled_value(x):
    count = 0
    for line in x:
        for elem in line:
            if elem != '*':
                count += 1
    return count


def check_optimal(v_export, v_import, plan, m_coast):
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == '*':
                if v_import[j] + v_export[i] > m_coast[i][j]:
                    # if v_import[j] - v_export[i] > m_coast[i][j]:  # rod
                    return False

    return True


def find_new_working_point(v_export, v_import, plan, matrix_cost):
    maximum = 0
    point = [0, 0]
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == '*':
                if (v_import[j] + v_export[i] - matrix_cost[i][j]) > maximum:
                    # if abs(v_import[j] - v_export[i] - matrix_cost[i][j]) > maximum:  # rod
                    # maximum = abs(v_import[j] - v_export[i] - matrix_cost[i][j])  # rod
                    maximum = abs(v_import[j] + v_export[i] - matrix_cost[i][j])
                    point = [i, j]
    return point


def update_system(result, solved, system):
    for eq in system:
        if not eq.solved:
            if eq.var_1 in result:
                result[eq.var_2] = eq.solve(eq.var_1, result[eq.var_1])
                solved = False
                continue
            if eq.var_2 in result:
                result[eq.var_1] = eq.solve(eq.var_2, result[eq.var_2])
                solved = False
                continue
    return solved


def convert_to_vectors(result: dict):
    keys, values = list(result.keys()), list(result.values())
    importers, exporters = [], []
    for i in range(len(keys)):
        if keys[i][0] == 'u':
            exporters.append([int(keys[i].split('_')[1]), values[i]])
        else:
            importers.append([int(keys[i].split('_')[1]), values[i]])
    exporters.sort(key=lambda x: x[0])
    importers.sort(key=lambda x: x[0])
    vector_export = [elem[1] for elem in exporters]
    vector_import = [elem[1] for elem in importers]
    return vector_export, vector_import


def solve_linear_system(task: TransportTask, start_plan):
    system = []
    for i in range(len(start_plan)):
        for j in range(len(start_plan[0])):
            if start_plan[i][j] != '*':
                new_eq = OneLineEquation("v_" + str(j), "u_" + str(i), task.matrix_cost[i][j])
                system.append(new_eq)
    for elem in system:
        print(elem)
    # Поскольку у нас n+m переменных и ВСЕГДА только n+m-1 уравнений, одну переменную можно выбрать любой
    result = {'u_0': 0}
    solved = False
    while not solved:
        solved = True
        solved = update_system(result, solved, system)

    print(result)
    return convert_to_vectors(result)


def find_way(starting_point, plan):
    for direction in directions:  # Путь существует и единственнен
        next_point = step(starting_point, direction)
        find, path = walk(next_point, direction, plan, starting_point, set(), starting_point)
        if find:
            return path
    return


def step(point, direction):
    return [point[LINE] + direction[LINE], point[COL] + direction[COL]]


def point_num(point, hor_size):
    return point[LINE] * hor_size + point[COL]


def equal_point(point, point_2):
    return point[LINE] == point_2[LINE] and point[COL] == point_2[COL]


def walk(point, current_direction, plan, starting_point, visited, prev_point):
    point_id = point_num(point, len(plan[0]))
    if point[LINE] < 0 or point[COL] < 0 or point[LINE] >= len(plan) or point[COL] >= len(
            plan[0]) or (point_id in visited):  # Вышли за границу
        return False, []
    nul = plan[point[LINE]][point[COL]] != '*'  # Проверяем, в рабочей ли мы клетке
    visited.add(point_id)
    if not nul:  # Если точка оказалась нерабочей, то просто идем дальше
        if point[LINE] == starting_point[LINE] and point[COL] == starting_point[COL]:  # Вернулись в исходную позицию
            # print("find")
            return True, []
        next_point = step(point, current_direction)
        find, path = walk(next_point, current_direction, plan, starting_point, visited, point)
        if find:
            return find, path
        visited.remove(point_id)
    else:
        for direction in directions:
            next_point = step(point, direction)
            if equal_point(next_point, prev_point):
                continue
            find, path = walk(next_point, direction, plan, starting_point, visited, point)
            # print(point)
            # print("find=", find)
            # print(path)
            if not equal_point(direction, current_direction):  # Можем применить к направлениям, тк по сути это точки
                path.append(point)
            if find:
                return find, path
        visited.remove(point_id)

    return False, []


def find_min(way, plan):
    print(way[0])
    min_elem = plan[way[0][LINE]][way[0][COL]]
    point = [way[0][LINE], way[0][COL]]
    for elem in way:
        if elem[2] == '-':
            if plan[elem[LINE]][elem[COL]] < min_elem:
                point = [elem[LINE], elem[COL]]
                # print("point changed",point)
                min_elem = plan[elem[LINE]][elem[COL]]
    return min_elem, point


def change_plan(plan, start_point):
    way = find_way(start_point, plan)
    # print(way)
    minus = True
    for i in range(len(way)):
        if minus:
            way[i].append("-")
        else:
            way[i].append("+")
        minus = not minus
    print("Ломаная пути", way)
    minimum, min_point = find_min(way, plan)
    plan[start_point[LINE]][start_point[COL]] = minimum
    for elem in way:
        if elem[2] == '-' and elem[LINE] == min_point[LINE] and elem[COL] == min_point[COL]:
            plan[elem[LINE]][elem[COL]] = '*'
        # print(elem)
        elif elem[2] == "-":
            plan[elem[LINE]][elem[COL]] -= minimum

        else:
            plan[elem[LINE]][elem[COL]] += minimum
    return plan


def run_potential_method(task: TransportTask, start_plan, matrix_cost):
    plan = start_plan
    checking_var = len(task.vector_exporter) + len(task.vector_importer) - 1
    while True:

        # for i in range(5):
        if checking_var == check_filled_value(plan):
            print("Заполнение верное")
            export_potential, import_potential = solve_linear_system(task, plan)
            print("Производители ", export_potential)
            print("Потребители ", import_potential)
            optimal = check_optimal(export_potential, import_potential, plan, task.matrix_cost)
            if optimal:
                print("END")
                break
            else:
                print("CONTINUE")
                print(calculate_function(plan, matrix_cost))

            working_point = find_new_working_point(export_potential, import_potential, plan, task.matrix_cost)
            print("Новая изменяемая точка", working_point)

            plan = change_plan(plan, working_point)
            print("new plan")
            for line in plan:
                print(line)
    print("final plan")
    for line in plan:
        print(line)
    return plan
