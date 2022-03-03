"""
	Bonus task: load all the available coffee recipes from the folder 'recipes/'
	File format:
		first line: coffee name
		next lines: resource=percentage

	info and examples for handling files:
		http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#operatii_cu_fisiere
		https://docs.python.org/3/library/io.html
		https://docs.python.org/3/library/os.path.html
"""
import io


RECIPES_FOLDER = "recipes/"

def show_recipe(recipe):
    recipe_path = recipe
    recipe_path = RECIPES_FOLDER + recipe_path + ".txt"
    with open(recipe_path) as recipe_to_show:
        print("The recipe for " + recipe + " is -->")
        for line in recipe_to_show:
            print(line)

