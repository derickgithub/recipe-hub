from django.db import models

# Recipe Source Model
class RecipeSource(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.quantity} of {self.name}'


# Recipe Model
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    source = models.ForeignKey(RecipeSource, on_delete=models.SET_NULL, null=True, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Recipe Review Model
class RecipeReview(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.recipe.title} by {self.author}'


# Recipe Collection Model
class RecipeCollection(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe, related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name