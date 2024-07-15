marks={
    "koshali":100,
    "komal":98,
    "rohan":23,
    "list":[1,2,3]
}
print(marks.items()) # Returns a list of (key,value)tuples
print(marks.keys())  # Returns a list containing dict's keys
print(marks.values())  # Returns a list containing dict's values

marks.update({"koshali":99, "shanti":34})
print(marks.items())
print(marks.get("komal"))