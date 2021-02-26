class reader:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file_obj = open(self.file_name, "r")  # Opened the file that we are working with for reading
        return self.get_data()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()

    def get_data(self):
        # Ожидаемый формат данных:
        # Строка в которой данные производителей
        # Enter
        # Строка в которой данные потребителей
        # Enter
        # Матрица в которой стоимости перевозок от iго производителя jому потребителю
        v_exporter, v_importer, m_cost = [], [], []
        for line in self.file_obj:
            if line == "\n":
                break
            v_exporter = [int(x) for x in line.split()]
        for line in self.file_obj:
            if line == "\n":
                break
            v_importer = [int(x) for x in line.split()]

        for line in self.file_obj:
            if line == "\n":
                break
            m_line = [int(x) for x in line.split()]
            m_cost.append(m_line)

        return m_cost, v_importer, v_exporter
