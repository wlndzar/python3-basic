def convert_mood(list_mood):
    mood_list ={
        "senang":"😊",
        "biasa":"😐",
        "sedih":"😭",
        "semangat":"😜"
    }

 return list(map(lambda m: mood_map.get(m,"💀")))   