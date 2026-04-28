import logging
logging.basicConfig(level=logging.INFO)
class EvenOddSeparator:
    def __init__(self):
        self.file_path = "C:\\python_projects\\file_reading_python_coding\\file_reading_python\\p1_even_odd_separator"
        self.even = []
        self.odd = []
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

    def separate_even_and_odd_integer_and_save(self):
        numbers = self.get_data()
        for i in numbers:
            if i % 2 == 0:
                self.even.append(i)
                continue
            self.odd.append(i)

        self.create_file("even_numbers.txt", self.even)
        self.create_file("odd_numbers.txt", self.odd)

if __name__ == "__main__":
    EvenOddSeparator().separate_even_and_odd_integer_and_save()