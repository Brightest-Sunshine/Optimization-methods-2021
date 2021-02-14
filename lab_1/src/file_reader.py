class reader_cond:
    num_vector = 1
    symb_vector = 0


class reader:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file_obj = open(self.file_name, "r")  # Opened the file that we are working with for reading
        return self.get_data()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()

    def get_data(self):
        matrix_A = []
        for line in self.file_obj:
            if line == "\n":
                break
            matrix_A.append([int(x) for x in line.split()])
        sign_of_matrix = self.read_data(reader_cond.symb_vector)
        vector_b = self.read_data(reader_cond.num_vector)
        vector_c = self.read_data(reader_cond.num_vector)
        sign_of_var = self.read_data(reader_cond.symb_vector)
        func = self.file_obj.readline().rstrip()
        for _ in range(len(vector_c) - len(sign_of_var)):
            sign_of_var.append("")
        data = [matrix_A, sign_of_matrix, vector_b, vector_c, sign_of_var, func]
        self.show_data(data)
        return data

    def read_data(self, type):
        for line in self.file_obj:
            if line == "\n":
                break
            if type:
                data = self.read_num_line(line)
            else:
                data = self.read_symb_line(line)
        return data

    @staticmethod
    def read_symb_line(line):
        return [x for x in line.split()]

    @staticmethod
    def read_num_line(line):
        return [int(x) for x in line.split()]

    @staticmethod
    def show_data(data):
        print("A = ", data[0])
        print("MatrixSigns = ", data[1])
        print("b = ", data[2])
        print("c = ", data[3])
        print("VariablesSigns = ", data[4])
        print("func = ", data[5])
