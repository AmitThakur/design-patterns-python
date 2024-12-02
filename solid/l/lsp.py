# ##### Before ######
# class Vehicle:
#     def start_engine(self):
#         raise NotImplementedError("Not yet implemented")
#
#
# class Bicycle(Vehicle):
#
#     def start_engine(self):
#         # Don't have engine!
#         pass
#
#
# class Car(Vehicle):
#     def start_engine(self):
#         print("Engine Started")
#

class Vehicle:

    def start(self):
        raise NotImplementedError("Not yet implemented")


class Bicycle(Vehicle):

    def start(self):
        print("Started bicycle...")


class Car(Vehicle):
    def start(self):
        print("Started car...")