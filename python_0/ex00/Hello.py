ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list = ["Hello", "tata!"]
# Les listes sont MODIFIABLES
ft_list[1] = "World!" # Midifcation par index on pourrai mettre -1 (dernier élément de la liste)
# Résultat : ["Hello", "world!"]

ft_tuple = ("Hello", "toto!")
# les tuples sont IMMUTABLES - on ne peut pas les dofier
# Soulution : créer un nouveau tuple
ft_tuple = ("Hello", "France!")
# Résultat : ("Hello", "France!") 

# Autre solution : convertir le tuple en liste, modifier la liste, puis convertir la liste de retour en tuple
# temp_list = list(ft_tuple) # Conversion en liste
# temp_list[1] = "France!" # Modification de la liste
# ft_tuple = tuple(temp_list) # Conversion de la liste de retour en tuple
# Résultat : ("Hello", "France!") 

# Les sets n'ont pas d'index, on utilise remove() et add()
ft_set.remove("tutu!") # Supprime l'ancien élément
ft_set.add("Perpignan!") # Ajouter le nouveau
# Résultat : "Hello", "France!")

ft_dict = {"Hello" : "titi!"}
# Modification par clé
ft_dict["Hello"] = "42Perpignan!"
# Résultat : {"Hello": "42Perpignan!"} ou {"Hello": "42Perpignan!"} (ordre des éléments non garanti)

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)