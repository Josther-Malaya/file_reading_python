import logging
logging.basicConfig(level=logging.INFO)
class SquareCubeSeparator:
    def __init__(self):
        self.file_path = "C:\\python_projects\\file_reading_python_coding\\file_reading_python\\p4_square_and_cube_separator\\"
        self.square = []
        self.cube = []

    def create_file(self, file_name, data):
        try:
            with open(self.file_path + file_name, "w") as file:
                file.write(" ".join(str(i) for i in data))
            logging.info("Successfully created a file")
        except Exception as e:
            logging.warning(e)

    def get_data(self):
        numbers = []
        with open(self.file_path + "Numbers.txt", "r") as file:
            try:
                for line in file:
                    numbers.append(float(line.strip()))
                logging.info("Success reading the file")
                return numbers
            except Exception as e:
                logging.warning(e)

    def separate_square_and_cube_integer_and_save(self):
        numbers = self.get_data()
        for i in numbers:
            if i % 2 == 0:
                self.square.append(i * i)
                continue
            self.cube.append(i * i * i)

        self.create_file("square_numbers.txt", self.square)
        self.create_file("cube_numbers.txt", self.cube)


if __name__ == "__main__":
    SquareCubeSeparator().separate_square_and_cube_integer_and_save()