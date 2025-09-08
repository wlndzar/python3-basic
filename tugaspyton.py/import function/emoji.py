def convert_mood(list_mood):
    mood_list ={
        "senang":"😊",
        "biasa":"😐",
        "sedih":"😭",
        "semangat":"😜"
    }

 return list(map(lambda m: mood_list.get(m,"💀"),list_mood))   