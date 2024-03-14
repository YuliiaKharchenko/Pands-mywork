# A program stores a student name and a list of her courses and
# grades in a dict.


student = {
        "name":"Mary",
        "modules": [
                 {
                 "courseName":"Programming",
                 "grade": 45
                 },
                 {
                 "courseName":"History",
                 "grade":99
                 },
                 {
                 "courseName":"",
                 "grade":0
                 }
                ]
        }
print ("Student: {}".format(student["name"]))

for module in student["modules"]:
    if module["courseName"] != "":  # check if the module is empty
          print("\t {} \t: {}".format(module["courseName"], module["grade"]))

# print("Number of modules is",len(student["modules"]))

