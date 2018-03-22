def tachycardia(age, average_heart_rate):
    """
    Uses age and average heart rate data to determine if the patient is
    tachycardic
    """
    if age > 15:
        if average_heart_rate > 100:
            tachycardia = True
        else:
            tachycardia = False
    if 12 <= age <= 15:
        if average_heart_rate > 119:
            tachycardia = True
        else:
            tachycardia = False
    if 8 <= age <= 11:
        if average_heart_rate > 130:
            tachycardia = True
        else:
            tachycardia = False
    if 5 <= age <= 7:
        if average_heart_rate > 133:
            tachycardia = True
        else:
            tachycardia = False
    if 3 <= age <= 4:
        if average_heart_rate > 137:
            tachycardia = True
        else:
            tachycardia = False
    if 1 <= age <= 2:
        if average_heart_rate > 151:
            tachycardia = True
        else:
            tachycardia = False
    is_tachycardic = tachycardic(tachycardia)
    return is_tachycardic


def tachycardic(tachycardia):
    """
    Returns string declaring whether or not given the tachycardia boolean the
    patient is tachycardic
    """
    if tachycardia is True:
        is_tachycardic = "User is tachycardic"
    else:
        is_tachycardic = "User is NOT tachycardic"
    return is_tachycardic
