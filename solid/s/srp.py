# class Report:
#     def generate(self):
#         return "Report Data"
#
#     def save_to_file(self, filename):
#         with open(filename, 'w') as file:
#             file.write(self.generate())

class Report:
    def generate(self):
        return "Report Data"


class FileManager:
    def save_to_file(self, data, filename):
        with open(filename, 'w') as file:
            file.write(data)

# Usage


report = Report()
file_manager = FileManager()
file_manager.save_to_file(report.generate(), "report.txt")
