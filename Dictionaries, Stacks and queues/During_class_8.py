#interactive mode

person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

>>> person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

>>> person["surname"] = "Nowak"
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person["married"] = not person["married"]
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person["gender"] = "male"
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999'}, 'gender': 'male'}
>>> person["hobby"].append("bicycle")
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions', 'bicycle'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999'}, 'gender': 'male'}
>>> person["phone"]["work"] = "123235657"
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions', 'bicycle'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999', 'work': '123235657'}, 'gender': 'male'}