meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ТРЕШ":"Что-то безумное, плохое, выходящее за рамки привычного",
            "ПРУФ":"доказательство",
            "QQ":"Приветствие",
            "ИЗИ":"Легко"
            }
           
word = input("Введите непонятное слово (большими буквами!): ") 

if word in meme_dict.keys():
    print(meme_dict [word])
    
else:
    print(" Токое слово не найдено в базе данных ((")
    # Что делать, если слово не нашлось?
