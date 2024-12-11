import os
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from fct_inter import validate_temperature,validate_time,last_time
from Garage import Garage
from paramètres import *
from stepperMoteur import Stepper
from Tracker import tracker   
# from gpiozero import AngularServo

# def show(event: ValueChangeEventArguments):
#     name = type(event.sender).__name__
#     ui.notify(f'{name}: {event.value}')

# ui.button('Button', on_click=lambda: ui.notify('Click'))
# with ui.row():
#     ui.checkbox('Checkbox', on_change=show)
#     ui.switch('Switch', on_change=show)
# ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
# with ui.row():
#     ui.input('Text input', on_change=show)
#     ui.select(['One', 'Two'], value='One', on_change=show)
# ui.link('And many more...', '/documentation').classes('mt-8')
#AJOUT PAGE
# @ui.page('/RDCch/')
#def _page():
#    with ui.row().style('align-item: center; justify-content: center; gap: 70px'):
#        ui.label('vous être en train de modifier le chauffage de')
#        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))

#menu principal 
@ui.page('/') 
def main_page():
    with ui.row().classes('fixed-center'):
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(heure_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\heure.png')
            with ui.card_section():
                ui.label("changer l'heure")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(saison_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\saison.png')
            with ui.card_section():
                 ui.label('changer la saison')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chauffage_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\chauffage.png')
            with ui.card_section():
                ui.label('gestion chauffage')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(eclairage_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\eclairage.png')
            with ui.card_section():
                ui.label('gestion éclairage')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(auto_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\auto.png')
            with ui.card_section():
                ui.label('jounée type')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(gar_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\gar.png')
            with ui.card_section():
                ui.label('Porte de garage')
                
#arrêt
    with ui.row().classes('absolute bottom-0 right-0 p-4'):
        ui.button("RESET",color='red', on_click=lambda: ui.notify('arrêt absolu!'))
                                                        #  ,os.system("sudo reboot")))


#page1  changement d heure
@ui.page('/heure') 

def heure_page():
    global last_time
 
    # global trackerSolaire
    # global heure
    # global minutes

    # global trackerSolaire
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour changer l'heure")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        last_time_label=ui.label(f"Heure précedente:{last_time}")  
    # Inserer l'heure
    with ui.row():
        hour_input = ui.input(label="HH", placeholder="00", value="00").props('type=number').style("width: 50px;")
        ui.label(":")
        minute_input = ui.input(label="MM", placeholder="00", value="00").props('type=number').style("width: 50px;")
  # Zone d'affichage des résultats
    result = ui.label()
    # Bouton de validation
    # ui.button("Valider l'heure souhaitée", on_click=lambda: (checkAndMove(hour_input, minute_input, result,last_time_label)))
    ui.button("Valider l'heure souhaitée", on_click=lambda:validate_time(hour_input, minute_input, result,last_time_label))
# def checkAndMove(hour_input, minute_input, result,last_time_label):
#     # global trackerSolaire
#     # global servo_horizontal
#     # global servo_vertical
#     trackerSolaire = tracker(servo_horizontal,servo_vertical)
#     if validate_time(hour_input, minute_input, result,last_time_label):
#         azimut,elevation = trackerSolaire.calculPositionWithDateAzimut(season,heure,minutes)
#         trackerSolaire.goToPosition(azimut,elevation)


   


#page2 Changement de saison
last_season = "Automne"
@ui.page('/saison') 
def saison_page():
    global last_season
    global season

    season = season_selector

    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour changer la saison")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
    # Fonction pour afficher la saison choisie
    def afficher_saison(e):
        global last_season
        last_season_label.set_text(f"Saison précédente : {last_season}")
        last_season = e.value
        result.set_text(f"Vous avez choisi : {e.value}")
    with ui.row().style('align-items: center; justify-content: center; gap: 20px;'):
        last_season_label = ui.label(f"Saison précédente : {last_season}")
    with ui.row().style('gap: 20px;'):
        # Sélecteur de saison
        ui.label('Choisissez une saison :')
        season_selector = ui.radio(
            ['Automne', 'Hiver', 'Printemps', 'Été'], 
            value='Automne', 
            on_change=afficher_saison ).props('inline')

    # affichage de la saison choisie
    result = ui.label(f"Vous avez choisi : {season_selector.value}")


   

#CHAUFFAGE 
#page3  GESTION chau
@ui.page('/chauffage') 
def chauffage_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 70px;'):
        ui.label("Page pour gestion chauffe")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
    with ui.row().classes('fixed-center'):
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(RDCch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\rdcplandesign.png')
            with ui.card_section():
                ui.label("modifier le chauffage du RDC")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(etagech_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\etageplandesign.png')
            with ui.card_section():
                ui.label("modifier le chauffage du premier étage")
#pageintegree chauffage1  
@ui.page('/RDCch')
def RDCch_page():
    with ui.row().style(' justify-content:center; gap:40px'):
        ui.label("vous êtes en train de modifier le chauffage du RDC")
        ui.button('Retour', on_click=lambda : ui.navigate.to(chauffage_page))
    with ui.row():
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(garagech_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\garage.png')
            with ui.card_section():
                ui.label("modifier le chauffage du garage")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(celierch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\celier.png')
            with ui.card_section():
                ui.label("modifier le chauffage du celier")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sejourch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sejour.png')
            with ui.card_section():
                ui.label("modifier le chauffage du séjour")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(cuisinech_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\cuisine.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la cuisine")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(SDBch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sdb.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la salle de bain")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(salonch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\salon.png')
            with ui.card_section():
                ui.label("modifier le chauffage du salon")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre1ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\chambre1.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la chambre 1")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(Hallch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\hall.png')
            with ui.card_section():
                ui.label("modifier le chauffage du hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(SDBHallch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sdbhall.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la SDB Hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(WCch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\wc.png')
            with ui.card_section():
                ui.label("modifier le chauffage des WC")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(bureauch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\bureau.png')
            with ui.card_section():
                ui.label("modifier le chauffage du bureau")

# les differentes pieces chauffées du RDC
#garage
@ui.page('/RDCch/garage')
def garagech_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous êtes en train de modifier le chauffage du garage')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

#celier
@ui.page('/RDCch/celier')
def celierch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du celier')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

      
#SDB
@ui.page('/RDCch/SDB')
def SDBch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage de la salle de bain')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

#HALL SDB      
@ui.page('/RDCch/SDBHall')
def SDBHallch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du hall de la salle de bain')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                 # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))


#séjour
@ui.page('/RDCch/sejour')
def sejourch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du séjour')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                 # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))


#cuisine
@ui.page('/RDCch/cuisine')
def cuisinech_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage de la cuisine')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))


#chambre 1
@ui.page('/RDCch/chambre1')
def chambre1ch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage de la chambre 1')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                 # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))


#hall RDC
@ui.page('/RDCch/hall')
def Hallch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du Hall')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                 # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))


#bureau
@ui.page('/RDCch/bureau')
def bureauch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du bureau')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))


#salon
@ui.page('/RDCch/salon')
def salonch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du salon')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                  # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

#WC
@ui.page('/RDCch/wc')
def WCch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage des WC')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCch_page))
                 # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))


#pageintegree chauffage2 
@ui.page('/etagech')
def etagech_page():
    with ui.row().style('align-item:center; justify-content:center; gap:70px'):
        ui.label("vous êtes en train de modifier le chauffage du premier étage")
        ui.button('Retour', on_click=lambda : ui.navigate.to(chauffage_page))
    with ui.row():
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(bureau2ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\bureau.png')
            with ui.card_section():
                ui.label("modifier le chauffage du bureau")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sasch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sas.png')
            with ui.card_section():
                ui.label("modifier le chauffage du SAS")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(hall2ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\hall.png')
            with ui.card_section():
                ui.label("modifier le chauffage du hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre2ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\chambre2.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la chambre 2")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sdb2ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sdb.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la salle de bain")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre3ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\chambre3.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la chambre 3")

# les differentes pieces chauffées du premier étage
@ui.page('/etagech/bureau')
def bureau2ch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du bureau')
        ui.button('Retour', on_click=lambda: ui.navigate.to(etagech_page))
                # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

@ui.page('/etagech/sas')
def sasch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du SAS')
        ui.button('Retour', on_click=lambda: ui.navigate.to(etagech_page))
              # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

@ui.page('/etagech/hall')
def hall2ch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du hall')
        ui.button('Retour', on_click=lambda: ui.navigate.to(etagech_page))
                # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

@ui.page('/etagech/sdb')
def sdb2ch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du hall de la salle de bain')
        ui.button('Retour', on_click=lambda: ui.navigate.to(etagech_page))
             # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

@ui.page('/etagech/chambre2')
def chambre2ch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage de la chambre 2')
        ui.button('Retour', on_click=lambda: ui.navigate.to(etagech_page))
                # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))

@ui.page('/etagech/chambre3')
def chambre3ch_page():
    with ui.column().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage de la chambre 3')
        ui.button('Retour', on_click=lambda: ui.navigate.to(etagech_page))
                    # Zone pour afficher les résultats
        result = ui.label()

        # Champ de saisie pour la température
        with ui.row().style('align-items: center; gap: 10px'):
            temp_input = ui.input(value="0").props("type=number").style("width: 80px;")
            ui.label("°C") 
        # Bouton de validation de température
        ui.button("Valider la température souhaitée", on_click=lambda:validate_temperature(temp_input,result))



   


#ELCLAIRAGE
#page4 GESTION elec
@ui.page('/eclairage') 
def eclairage_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour gestion éclairage")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
    with ui.row().classes('fixed-center'):
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(RDCec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\rdcplandesign.png')
            with ui.card_section():
                ui.label("modifier l'eclairage du RDC")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(etageec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\etageplandesign.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du premier étage")
#pageintegree eclairage  
@ui.page('/RDCec')
def RDCec_page():
    with ui.row().style(' justify-content:center; gap:40px'):
        ui.label("vous êtes en train de modifier l'éclairage du RDC")
        ui.button('Retour', on_click=lambda : ui.navigate.to(eclairage_page))
    with ui.row():
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(garageec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\garage.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du garage")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(celierec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\celier.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du celier")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sejourec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sejour.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du séjour")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(cuisineec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\cuisine.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la cuisine")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(SDBec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sdb.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la salle de bain")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(salonec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\salon.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du salon")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre1ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\chambre1.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la chambre 1")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(Hallec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\hall.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(SDBHallec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sdbhall.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la SDB Hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(WCec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\wc.png')
            with ui.card_section():
                ui.label("modifier l'éclairage des WC")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(bureauec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\bureau.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du bureau")


#allumer elec notif/changement a voir plus tard
def on_switch_change(event):
    ui.notify(f"LEDs: {'allumées' if event.value else 'éteintes'}")

# les differentes pieces du RDC
@ui.page('/RDCec/garage')
def garageec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du garage")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/celier')
def celierec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du celier")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/SDB')
def SDBec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage de la salle de bain")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/SDBHall')
def SDBHallec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du hall de la salle de bain")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/sejour')
def sejourec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du séjour")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/cuisine')
def cuisineec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage de la cuisine")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/chambre1')
def chambre1ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage de la chambre 1")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/hall')
def Hallec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du Hall")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/bureau')
def bureauec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du bureau")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/salon')
def salonec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du salon")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/RDCec/wc')
def WCec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage des WC")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)



#pageintegree eclairage2 
@ui.page('/etageec')
def etageec_page():
    with ui.row().style('align-item:center; justify-content:center; gap:70px'):
        ui.label("vous êtes en train de modifier l'éclairage du premier étage")
        ui.button('Retour', on_click=lambda : ui.navigate.to(eclairage_page))
    with ui.row():
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(terrasseec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\terrasse.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la terrasse")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(bureau2ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\bureau.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du bureau")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sasec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sas.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du SAS")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(hall2ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\hall.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre2ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\chambre2.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la chambre 2")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sdb2ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\sdb.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la salle de bain")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre3ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\img\chambre3.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la chambre 3")

# les differentes pieces du premier étage
@ui.page('/etageec/terasse')
def terrasseec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage dela terrasse")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/etageec/bureau')
def bureau2ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du bureau")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/etageec/sas')
def sasec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du SAS")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/etageec/hall')
def hall2ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du hall")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/etageec/sdb')
def sdb2ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du hall de la salle de bain")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/etageec/chambre2')
def chambre2ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage de la chambre 2")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)
@ui.page('/etageec/chambre3')
def chambre3ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage de la chambre 3")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
    with ui.row():
        ui.switch('allumer', on_change=on_switch_change)



   

#page5  journee type 
@ui.page('/auto') 
def auto_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page journée type")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))

#page6  garage 
@ui.page('/garage')
def gar_page():
    global garage
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("garage")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
    #partie rasp
    with ui.column().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.button("ouvrir le garage ",color='green', on_click= lambda : garage.ouverture())
        ui.button("fermer le garage ",color='red', on_click=lambda : garage.Fermeture())
        
#plage de modif parametres 
#from Sphere import sphere
#sphere = sphere(paramtre)
# porte garage 
stepper = Stepper(param_stepper["pinENA"],param_stepper["pinDIR"],param_stepper["pinPUL"])
garage = Garage(stepper,param_FC_ouverture["pin"],param_FC_fermeture["pin"])
# tracker
# if __name__ == "__main__":
#     heure =  12
#     minutes = 30
#     season = 'Printemps'
#     trackerSolaire = None

#     print("param_servo_tracker_horizontal:", param_servo_tracker_horizontal['pin'])
#     servo_horizontal=AngularServo(param_servo_tracker_horizontal['pin'], min_angle=param_servo_tracker_horizontal['min_angle'],max_angle=param_servo_tracker_horizontal['max_angle'],min_pulse_width=param_servo_tracker_horizontal['min_pulse_width'],max_pulse_width= param_servo_tracker_horizontal['max_pulse_width'])   #servo noir
#     servo_vertical = AngularServo(param_servo_tracker_vertical['pin'], min_angle=param_servo_tracker_vertical['min_angle'],max_angle=param_servo_tracker_vertical['max_angle'],min_pulse_width=param_servo_tracker_vertical['min_pulse_width'],max_pulse_width=param_servo_tracker_vertical['max_pulse_width'])     #servo bleu
#     trackerSolaire = tracker(servo_horizontal,servo_vertical)
#     azimut,elevation = trackerSolaire.calculPositionWithDateAzimut('Printemps',12,30)
#     trackerSolaire.goToPosition(azimut,elevation)


ui.navigate.to(main_page, new_tab=False)

ui.run()