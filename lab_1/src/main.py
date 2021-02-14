from src import file_reader, canon
from src import simplex_method, dual_form

with file_reader.reader("problem.txt") as data:  # Читаем условие задачи из файла
    matrix_A, sign_of_matrix, vector_b, vector_c, sign_of_var, func = data
    canon_system = canon.convert_to_canon(data)
NpCanonForm = simplex_method.NpCanonicalForm(canon_system)
x = simplex_method.starting_vector(NpCanonForm)
print("--- simplex algorithm: primal problem ---")
print(simplex_method.simplex_method(NpCanonForm, x).x)

# creating dualproblem
dual_form.check_signs(matrix_A, vector_b, sign_of_matrix)  # only >= sign allowed in finding min problem
TransA = dual_form.transpose_matrix(matrix_A)  # transposing matrix A
Newb = dual_form.new_vector(vector_c)  # finding dual vector b
Newc = dual_form.new_coeff(vector_b)  # finding coefficients of dual goal function
NewMatrixSigns = dual_form.new_mtrx_signs(sign_of_var)  # finding signs of dual matrix
NewVariableSigns = dual_form.new_var_signs(sign_of_matrix)  # finding signs of dual variables
Newfunc = dual_form.new_function(func)  # finding dual problem type

# canon dual system
DualCanonSys = canon.convert_to_canon([TransA, NewMatrixSigns, Newb, Newc, NewVariableSigns, Newfunc])

NpCanonForm = simplex_method.NpCanonicalForm(DualCanonSys)
x = simplex_method.starting_vector(NpCanonForm)
print("--- simplex algorithm: dual problem ---")
print(simplex_method.simplex_method(NpCanonForm, x).x)

x = input()
