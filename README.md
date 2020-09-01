# practice graphql with graphene

<br>

> Fetch Ingredients list
```
query {
  allIngredients {
    id
    name
    category {
        name
    }
  }
}
```
```
{
    "data": {
        "allIngredients": [
            {
                "id": "1",
                "name": "Eggs",
                "notes": "Good old eggs",
                "category": {
                    "name": "Dairy"
                }
            },
            {
                "id": "2",
                "name": "Milk",
                "notes": "Comes from a cow",
                "category": {
                    "name": "Dairy"
                }
            },
            {
                "id": "3",
                "name": "Beef",
                "notes": "Much like milk, this comes from a cow",
                "category": {
                    "name": "Meat"
                }
            },
            {
                "id": "4",
                "name": "Chicken",
                "notes": "Definitely doesn't come from a cow",
                "category": {
                    "name": "Meat"
                }
            }
        ]
    }
}
```

<br>

> Fetch Category list
```
query {
  allCategories {
    id
    name
  }
}
```
```
{
    "data": {
        "allCategories": [
            {
                "id": "1",
                "name": "Dairy"
            },
            {
                "id": "2",
                "name": "Meat"
            }
        ]
    }
}
```

<br>

> Fetch Category where ingredients category is Meat
```
query {
  categoryByName(name:"Meat") {
    id
    name
    ingredients {
        name
    }
  }
}
```
```
{
    "data": {
        "categoryByName": {
            "id": "2",
            "name": "Meat",
            "ingredients": [
                {
                    "name": "Beef"
                },
                {
                    "name": "Chicken"
                }
            ]
        }
    }
}
```