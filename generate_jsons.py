import json
import os

import requests


def save_object_as_json(data, jsonPath):
	with open(jsonPath, "w") as f:
		json.dump(data, f, indent="\t")
	print(f"Saved: {jsonPath}")


def generate_v1_data():
	v1_json_path = "data/v1/prize.json"
	jo = json.load(open(v1_json_path))
	prizes = jo["prizes"]

	years = {}
	categories = {}
	for prize in prizes:
		year = prize["year"]
		if year in years:
			years[year]["prizes"].append(prize)
		else:
			years[year] = {"prizes": []}

		category = prize["category"]
		if category in categories:
			categories[category]["prizes"].append(prize)
		else:
			categories[category] = {"prizes": []}

	for year in years:
		data = years[year]
		jsonPath = f"src/v1/{year}.json"
		save_object_as_json(data, jsonPath)

	for category in categories:
		data = categories[category]
		jsonPath = f"src/v1/{category}.json"
		save_object_as_json(data, jsonPath)


def main():
	generate_v1_data()


if __name__ == '__main__':
	main()
