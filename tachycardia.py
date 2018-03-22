def tachycardia(user.age, average_heart_rate):
    if user.age > 15:
        if average_heart_rate > 100:
            tachycardia = True
        else:
            tachycardia = False
    if 12 <= user.age <= 15:
        if average_heart_rate > 119:
            tachycardia = True
        else:
            tachycardia = False
    if 8 <= user.age <= 11:
        if average_heart_rate > 130:
            tachycardia = True
        else:
            tachycardia = False
    if 5 <= user.age <= 7:
        if average_heart_rate > 133:
            tachycardia = True
        else:
            tachycardia = False
    if 3 <= user.age <= 4:
        if average_heart_rate > 137:
            tachycardia = True
        else:
            tachycardia = False
    if 1 <= user.age <= 2:
        if average_heart_rate > 151:
            tachycardia = True
        else:
            tachycardia = False
    return tachycardia
