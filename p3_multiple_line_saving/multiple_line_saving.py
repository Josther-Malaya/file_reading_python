class MultipleLineSaving:
    def __init__(self):
        self.file_path = "C:\\python_projects\\file_reading_python_coding\\file_reading_python\\p3_multiple_line_saving\\"

    def multiple_line_saving(self):
        try:
            with open(self.file_path + "mylife.txt", "a") as file:
                while True:
                    text = input("Enter line: ")
                    more = input("Are there more lines (y/n)? ").lower()
                    file.write(f"{text}\n")

                    if more != "y":
                        break

        except:
            print("Error writing to file.")

if __name__ == "__main__":
    MultipleLineSaving().multiple_line_saving()