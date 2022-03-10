counties = ["Arapahoe","Denver","Jefferson"]

print(counties[0])
print(counties[1])
print(counties[2])

counties.append("El Paso")

counties.insert(2, "El Paso")


counties.remove("El Paso")
print(counties)

counties.pop(3)
print(counties)

counties_tuple = ("Arapahoe","Denver","Jefferson")

print(len(counties_tuple))
print(counties_tuple[1])

counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))

print(counties_dict.items())

print(counties_dict.keys())
print(counties_dict.values())

counties_dict.get("Denver")
print(counties_dict.get("Denver"))

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))

#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))

# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")



