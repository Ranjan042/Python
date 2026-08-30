marks={
    "harry":100,
    "shubham":56,
    "Rohan":23
}
# print(marks.items())
# print(marks.keys())
print(marks.values())
marks.update({"harry":99})
# print(marks)
print(marks["harry"]) #prints none
print(marks.get("harry")) #display an error