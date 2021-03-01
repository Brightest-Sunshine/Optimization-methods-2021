class TransportTask:
    def __init__(self, cost_matrix, importer_vector, exporter_vector):
        self.matrix_cost = []
        for elem in cost_matrix:
            self.matrix_cost.append(elem.copy())
        self.vector_importer = importer_vector.copy()  # Покупатель/Потребитель
        self.vector_exporter = exporter_vector.copy()  # Продавец/Производитель
        self.make_closed()

    #
    # Как выглядит таблица? c00     c01      c02.... exporter0
    #                       c10     c11      c12 ....exporter1
    #                         ...
    #                       cn0     cn1      cn2 ... exportern
    #                      importer0 importer1 .....

    def make_closed(self):
        sum_import = 0
        sum_export = 0
        for elem in self.vector_importer:
            sum_import += elem
        for elem in self.vector_exporter:
            sum_export += elem
        if sum_import == sum_export:
            return
        elif sum_import > sum_export:
            self.make_fictive_exporter(sum_import - sum_export)
            return
        else:
            self.make_fictive_importer(sum_export - sum_import)
            return

    def make_fictive_exporter(self, diff):
        self.matrix_cost.append([0 for _ in self.vector_importer])  # Добавляем строчку 0
        self.vector_exporter.append(diff)  # Добавляем прозводство фиктивного
        return

    def make_fictive_importer(self, diff):
        for elem in self.matrix_cost:
            elem.append(0)
        self.vector_importer.append(diff)  # Фиктивный потребитель
        return


class OneLineEquation:
    def __init__(self, var_1, var_2, value):
        self.var_1 = var_1
        self.var_2 = var_2
        self.var_1_val = 0
        self.var_2_val = 0
        self.value = value
        self.solved = False

    def __str__(self):
        return self.var_1 + "+" + self.var_2 + "=" + str(self.value)

    def solve(self, var, value):
        self.solved = True
        if var == self.var_1:
            self.var_1_val = value
            #self.var_2_val = value - self.value #rod
            self.var_2_val = -value + self.value
            return self.var_2_val
        else:
            self.var_2_val = value
            #self.var_1_val = value + self.value #rod
            self.var_1_val = -value + self.value
            return self.var_1_val
