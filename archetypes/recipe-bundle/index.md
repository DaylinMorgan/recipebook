---
layout: recipe
date: {{ .Date }}
draft: true
title: "{{ replace .Name "-" " " | humanize | title }}" # The title of your awesome recipe
image: xkcd720.png # Name of image in recipe bundle
category: # type of meal --- must be a list!
# - Breakfast, Lunch, Dinner, Appetizer, Snack, Dessert
cuisine: # region for recipe --- must be a list!
# - French, Mediterranean, American, etc 
tags: # general info to connect to other recipes --- must be a list! 
# - savory, sweet, vegan, etc.
yield: # number of servings
prepTime: 
cookTime: 

ingredients:
  - Food stuff 

directions:
  - cook the food 

notes: #extra info about the recipe --- must be a list!
  # - don't watch the water boil, it slows it down

basedon: # reference links 
    # link: # web links to other recipes or videos 
        # - https://www.food.com/recipe/traditional-peanut-butter-and-jelly-243965
    # image: # name of image in directory with the recipe
        # - recipe-reference.jpg

---
