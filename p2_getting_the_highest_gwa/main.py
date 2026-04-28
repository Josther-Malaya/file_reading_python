class HighestGwa:
    def __init__(self):
        self.file_path = "C:\\python_projects\\file_reading_python_coding\\file_reading_python\\p2_getting_the_highest_gwa\\"

    def read_file(self) -> list[str]:
        with open(self.file_path + "highest_gwa.txt", 'r') as file:
            content = [line.rstrip("\n") for line in file.readlines()]
        return content

    def get_highest(self, data: list):
        new_data = [info.split(",") for info in data]
        highest_gwa = max(new_data, key=lambda x: x[1])
        print(f"Highest GWA\nStudent: {highest_gwa[0]}\nGWA: {highest_gwa[1]}")

if __name__ == "__main__":
    gwa = HighestGwa()
    data = gwa.read_file()
    gwa.get_highest(data)