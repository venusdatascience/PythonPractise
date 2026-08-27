student_mngmt_system = {
    "firststudent": {
        "name": "sita",
        "marks": [67, 87, 98, 68]
    },
    "secondstudent": {
        "name": "ram",
        "marks": [89, 78, 67, 86]
    }
}
student_mngmt_system["firststudent"]["name"]
s1 =student_mngmt_system["firststudent"]["marks"]
s1
sum =0
for i in s1:
    sum = i+sum


    
print((sum)/len(s1))
student_mngmt_system["firststudent"].items()
