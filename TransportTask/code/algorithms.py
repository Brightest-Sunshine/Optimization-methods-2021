from TransportTask.code.data_structure import TransportTask


def north_west_method(get_task: TransportTask):  # Создаем начальный план
    task = copy_task(get_task)
    point = [0, 0]  # Наше местоположение в таблице, первый элемент строка, второй столбец
    while point[0] <= len(task.vector_exporter) - 1 and point[1] <= len(task.vector_importer) - 1:
        possible_max = min(task.vector_exporter[point[0]], task.vector_importer[point[1]])
        if task.vector_exporter[point[0]] == task.vector_importer[point[1]]:
            # Если мы полностью закрыли импортера и экспортера
            # close_line_and_column(task, point[1], point[0], possible_max)
            # Нельзя закрыть сразу оба, можно закрыть только одного, второму нужно оставить 0.
            if point[1] < len(task.vector_importer) - 1: #Есть место справа
                close_column(task, point[1], point[0], possible_max)
                close_line(task, point[1]+1,point[0], 0)
            elif point[0] < len(task.vector_exporter) - 1:  # Если есть место снизу.
                close_line(task, point[1], point[0], possible_max)
                close_column(task, point[1],point[0]+1, 0)

            else: # Видимо мы в правом нижнем углу?
                close_line_and_column(task, point[1], point[0], possible_max)
            point[1] += 1
            point[0] += 1

        elif possible_max == task.vector_importer[point[1]]:  # Заполнили импортера
            close_column(task, point[1], point[0], possible_max)
            point[1] += 1
            task.vector_exporter[point[0]] -= possible_max

        else:
            close_line(task, point[1], point[0], possible_max)
            point[0] += 1
            task.vector_importer[point[1]] -= possible_max

    return task.matrix_cost.copy()


def close_line_and_column(task: TransportTask, x, y, new_cost):
    close_line(task, x, y, new_cost)
    close_column(task, x, y, new_cost)
    return


def close_line(task: TransportTask, x, y, new_cost):
    for i in range(x + 1, len(task.vector_importer)):
        task.matrix_cost[y][i] = '*'
    task.matrix_cost[y][x] = new_cost
    return


def close_column(task: TransportTask, x, y, new_cost):
    for i in range(y + 1, len(task.vector_exporter)):
        task.matrix_cost[i][x] = '*'
    task.matrix_cost[y][x] = new_cost
    return


def copy_task(get_task):
    return TransportTask(get_task.matrix_cost, get_task.vector_importer, get_task.vector_exporter)


def calculate_function(x, cost):
    result = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] != '*':
                result += x[i][j] * cost[i][j]
    return result
