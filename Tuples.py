#Tuples are immutable

# coordinates = (4, 7, 9)
# coordinates[1] = 5
# print(coordinates)

birth_date=(23, "june", 2003)


# fruits = {"apple", "banana", "cherry"}
# print(fruits[1])


#dictionary
contact={
    "name": "sarishma",
    "num": 7
}

book = {
  "title": "1984",
  "author": "George Orwell"
}
book_info = book.values()
print(book_info)

cities= {"paris", "kathmandu", "new deli" }
cities_cap=[x.capitalize() for x in cities]
print(cities_cap)

#Code a list comprehension to add a hashtag '#' to the values of the tags list

tags = ["python", "coding", "machinelearning"]
hashtags=[f"#{tag}" for tag in tags]
print(hashtags)

hashtags=["#"+ x for x in tags]
print(hashtags)

#Create a list that includes only the values from the points list that are higher than or equal to 8.

points=[1, 40, 8, 9 ,5, 6]
winners=[x for x in points if x >=  8]
print(winners)

