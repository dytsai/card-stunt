import os

def insert_color_code(color_array):
    modified_array = []
    for i in range(len(color_array)):
        if i > 0 and i % 20 == 0:
            modified_array.append('#FFFFFF')
        modified_array.append(color_array[i])
    return modified_array

directory = "C:\\Users\\Daniel Tsai\\Downloads\\tfg-stunt\\Pattenrs2"

for i in range(1, 36):
    file_name = f"{i}.txt"
    file_path = os.path.join(directory, file_name)

    with open(file_path, "r") as file:
        content = file.read()

    color_array = eval(content)

    modified_array = insert_color_code(color_array)

    modified_content = str(modified_array).replace("'", '"')

    with open(file_path, "w") as file:
        file.write(modified_content)

