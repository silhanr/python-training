
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}


print(travel_log["France"][1])

travel_log2 = {
    "France": {
        "visited cities": [
            "Paris",
            "Lille",
            "Dijon"],
        "total_visits": 12
    },
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log2["France"]["visited cities"][1])