#temperature
def validate_temperature(temp_input, result):
    try:
        temp = temp_input
        if -20 <= temp <= 40:
            result.set_text(f"Température validée : {temp}°C")
            return True
        else:
            result.set_text("Erreur : La température doit être entre -20°C et 40°C")
            return False
    except ValueError:
        result.set_text("Erreur : Veuillez entrer un nombre valide")
        return False


#heure
last_time= "00:00"
def validate_time(hour,result_time,last_time_label):
    global last_time
    try:
        time = hour.value 
        # Récupération des valeurs des champs
        HH ,MM = map(int, time.split(':'))
        
        # Vérification des plages horaires valides
        if 0 <= HH < 24 and 0 <= MM < 60:
            last_time_label.set_text(f"Heure précedente : {last_time}")
            last_time = f'{HH:02}:{MM:02}'
            result_time.set_text(f"Heure validée : {HH:02}:{MM:02}")
            return True
        else:
            result_time.set_text("Erreur : heure ou minute invalide")
            return False
    except ValueError: # Gestion des entrées non numériques
        result_time.set_text("Erreur : entrez uniquement des chiffres")
        return False

