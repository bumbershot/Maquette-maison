
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from fct_inter import validate_temperature,validate_time
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
            ui.image(r'C:\Users\Asus\Desktop\maquette\heure.png')
            with ui.card_section():
                ui.label("changer l'heure")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(saison_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\saison.png')
            with ui.card_section():
                 ui.label('changer la saison')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chauffage_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\chauffage.png')
            with ui.card_section():
                ui.label('gestion chauffage')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(eclairage_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\eclairage.png')
            with ui.card_section():
                ui.label('gestion éclairage')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(auto_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\auto.png')
            with ui.card_section():
                ui.label('jounée type')
#arrêt d urgence
    with ui.row().classes('absolute bottom-0 right-0 p-4'):
        ui.button("ARRÊT D'URGENCE",color='red', on_click=lambda: ui.notify('arrêt absolu!'))



#page1  changement d heure
@ui.page('/heure') 
def heure_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour changer l'heure")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
          
    # Inserer l'heure
    with ui.row():
        hour_input = ui.input(label="HH", placeholder="00", value="00").props('type=number').style("width: 50px;")
        ui.label(":")
        minute_input = ui.input(label="MM", placeholder="00", value="00").props('type=number').style("width: 50px;")
  # Zone d'affichage des résultats
    result = ui.label()
    # Bouton de validation
    ui.button("Valider l'heure souhaitée", on_click=lambda: validate_time(hour_input, minute_input, result))


   


#page2 Changement de saison
@ui.page('/saison') 
def saison_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour changer la saison")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
    # Fonction pour afficher la saison choisie
    def afficher_saison(e):
        resultat.set_text(f"Vous avez choisi : {e.value}")
    with ui.row().style('gap: 20px;'):
        # Sélecteur de saison
        ui.label('Choisissez une saison :')
        saison_selecteur = ui.radio(
            ['Automne', 'Hiver', 'Printemps', 'Été'], 
            value='Automne', 
            on_change=afficher_saison ).props('inline')

    # Zone pour afficher la saison choisie
    resultat = ui.label(f"Vous avez choisi : {saison_selecteur.value}")

#CHAUFFAGE 
#page3  GESTION chau
@ui.page('/chauffage') 
def chauffage_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 70px;'):
        ui.label("Page pour gestion chauffe")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
    with ui.row().classes('fixed-center'):
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(RDCch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\rdcplandesign.png')
            with ui.card_section():
                ui.label("modifier le chauffage du RDC")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(etagech_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\etageplandesign.png')
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
            ui.image(r'C:\Users\Asus\Desktop\maquette\garage.png')
            with ui.card_section():
                ui.label("modifier le chauffage du garage")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(celierch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\celier.png')
            with ui.card_section():
                ui.label("modifier le chauffage du celier")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sejourch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sejour.png')
            with ui.card_section():
                ui.label("modifier le chauffage du séjour")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(cuisinech_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\cuisine.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la cuisine")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(SDBch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sdb.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la salle de bain")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(salonch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\salon.png')
            with ui.card_section():
                ui.label("modifier le chauffage du salon")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre1ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\chambre1.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la chambre 1")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(Hallch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\hall.png')
            with ui.card_section():
                ui.label("modifier le chauffage du hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(SDBHallch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sdbhall.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la SDB Hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(WCch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\wc.png')
            with ui.card_section():
                ui.label("modifier le chauffage des WC")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(bureauch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\bureau.png')
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
            ui.image(r'C:\Users\Asus\Desktop\maquette\bureau.png')
            with ui.card_section():
                ui.label("modifier le chauffage du bureau")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sasch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sas.png')
            with ui.card_section():
                ui.label("modifier le chauffage du SAS")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(hall2ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\hall.png')
            with ui.card_section():
                ui.label("modifier le chauffage du hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre2ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\chambre2.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la chambre 2")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sdb2ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sdb.png')
            with ui.card_section():
                ui.label("modifier le chauffage de la salle de bain")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre3ch_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\chambre3.png')
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
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
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
            ui.image(r'C:\Users\Asus\Desktop\maquette\rdcplandesign.png')
            with ui.card_section():
                ui.label("modifier l'eclairage du RDC")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(etageec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\etageplandesign.png')
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
            ui.image(r'C:\Users\Asus\Desktop\maquette\garage.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du garage")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(celierec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\celier.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du celier")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sejourec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sejour.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du séjour")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(cuisineec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\cuisine.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la cuisine")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(SDBec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sdb.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la salle de bain")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(salonec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\salon.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du salon")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre1ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\chambre1.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la chambre 1")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(Hallec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\hall.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(SDBHallec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sdbhall.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la SDB Hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(WCec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\wc.png')
            with ui.card_section():
                ui.label("modifier l'éclairage des WC")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(bureauec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\bureau.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du bureau")

# les differentes pieces du RDC
@ui.page('/RDCec/garage')
def garageec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du garage')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/celier')
def celierec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du celier')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/SDB')
def SDBec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage de la salle de bain')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/SDBHall')
def SDBHallec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du hall de la salle de bain')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/sejour')
def sejourec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage du séjour')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/cuisine')
def cuisineec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage de la cuisine')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/chambre1')
def chambre1ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label('vous être en train de modifier le chauffage de la chambre 1')
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/hall')
def Hallec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du Hall")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/bureau')
def bureauec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du bureau")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/salon')
def salonec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du salon")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))
@ui.page('/RDCec/wc')
def WCec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage des WC")
        ui.button('Retour', on_click=lambda: ui.navigate.to(RDCec_page))



#pageintegree eclairage2 
@ui.page('/etageec')
def etageec_page():
    with ui.row().style('align-item:center; justify-content:center; gap:70px'):
        ui.label("vous êtes en train de modifier l'éclairage du premier étage")
        ui.button('Retour', on_click=lambda : ui.navigate.to(eclairage_page))
    with ui.row():
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(terrasseec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\terrasse.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la terrasse")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(bureau2ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\bureau.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du bureau")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sasec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sas.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du SAS")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(hall2ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\hall.png')
            with ui.card_section():
                ui.label("modifier l'éclairage du hall")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre2ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\chambre2.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la chambre 2")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(sdb2ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\sdb.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la salle de bain")
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chambre3ec_page, new_tab=False) ):
            ui.image(r'C:\Users\Asus\Desktop\maquette\chambre3.png')
            with ui.card_section():
                ui.label("modifier l'éclairage de la chambre 3")

# les differentes pieces du premier étage
@ui.page('/etageec/terasse')
def terrasseec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage dela terrasse")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
@ui.page('/etageec/bureau')
def bureau2ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du bureau")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
@ui.page('/etageec/sas')
def sasec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du SAS")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
@ui.page('/etageec/hall')
def hall2ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du hall")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
@ui.page('/etageec/sdb')
def sdb2ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage du hall de la salle de bain")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
@ui.page('/etageec/chambre2')
def chambre2ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage de la chambre 2")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))
@ui.page('/etageec/chambre3')
def chambre3ec_page():
    with ui.row().style('align-item: center; justify-content: center; gap: 40px'):
        ui.label("vous être en train de modifier l'éclairage de la chambre 3")
        ui.button('Retour', on_click=lambda: ui.navigate.to(etageec_page))


#page5  journee type 
@ui.page('/auto') 
def auto_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page journée type")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
ui.navigate.to(main_page, new_tab=False)

ui.run()