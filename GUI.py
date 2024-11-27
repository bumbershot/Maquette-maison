
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
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

#menu principal 
@ui.page('/') 
def main_page():
    with ui.row().classes('fixed-center'):
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(heure_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\heure.png')
            with ui.card_section():
                ui.label('changer l heure')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(saison_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\saison.png')
            with ui.card_section():
                 ui.label('changer la saison')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(chauffage_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\chauffage.png')
            with ui.card_section():
                ui.label('gestion chauffage')
        with ui.card(align_items = 'stretch').tight().on('click', lambda: ui.navigate.to(heure_page, new_tab=False)):
            ui.image(r'C:\Users\Asus\Desktop\maquette\eclairage.png')
            with ui.card_section():
                ui.label('gestion éclairage')

#page1  changement d heure
@ui.page('/heure') 
def heure_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour changer l'heure")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
#page2 Changement de saison
@ui.page('/saison') 
def saison_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour changer la saison")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))

#page3  GESTION ELEC
@ui.page('/chauffage') 
def chauffage_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour gestion chauffe")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
#page4 GESTION 
@ui.page('/eclairage') 
def eclairage_page():
    with ui.row().style('align-items: center; justify-content: center; gap: 40px;'):
        ui.label("Page pour gestion éclairage")
        ui.button('Retour', on_click=lambda : ui.navigate.to(main_page))
ui.navigate.to(main_page, new_tab=False)

ui.run()

