from nicegui import ui
import os
# import gettext

# TODO: find out how pot works and generates the .po file for French

# lang2 = gettext.translation('myapplication', languages=['en'])
# lang1 = gettext.translation('myapplication', languages=['fr'])

# setup in French
# lang1.install()

ui.page_title('Lasagnapp')

# app styling: font, bg color and step font size
ui.add_head_html('''
    <link rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Noto+Sans">
    <style>
      body {
        font-family: 'Noto Sans', serif;
        font-size : 18px;
      }
    </style>
''')
ui.query('body').style('background-color: #ffeedd')
ui.add_css('.q-stepper__title { font-size: 20px; color: black}')

title = 'La vraie bonne recette de lasagnes'

with ui.header().style('background-color: white') as header: #
    ui.label(text=title).style('color: #CF2435; font-size: 150%; font-weight: bold')

# file = open("ingredients.md", "r", encoding="utf-8")
# ui.markdown(file.read())

# with ui.row():
#     with ui.card().tight():
#         with ui.card_section():
#             ui.label("Sauce bolognaise")
#             ui.markdown("this is a test ")
#     with ui.card().tight():
#         with ui.card_section():
#             ui.label("Sauce béchamel")
#             ui.markdown("this is a test")
#     with ui.card().tight():
#         with ui.card_section():
#             ui.label("Lasagnes")
#             ui.markdown("this is a test")

ui.label("Ingrédients: (pour 6 à 8 personnes)").style('font-weight: bold')

# Based on Quasar so use props to set component styling
ui.tree([
    {'id': ' Sauce bolognaise', 'children': [{'id': '1 kg de viande: 600g filet américain pur boeuf et 400 g de haché veau + porc'},
                                    {'id': '2 oignons'},
                                    {'id': '1 à 2 carottes'},
                                    {'id': '1200 ml de sauce tomate'},
                                    {'id': 'Sel'},
                                    {'id': 'Poivre'},
                                    {'id': 'Un petit verre de lait'}]},
], label_key='id').props("dense no-connectors") # icon='looks_one'

ui.tree([
    {'id': ' Sauce béchamel', 'children': [{'id': '50 cl de lait'},
                                    {'id': '50 g de beurre'},
                                    {'id': '50 g de farine'},
                                    {'id': 'Noix de muscade'}]},
], label_key='id').props("dense no-connectors") # icon='looks_two'

ui.tree([
    {'id': ' Lasagnes', 'children': [{'id': 'Un paquet de lasagnes avec une vingtaine de feuilles'},
                                    {'id': '150 g de mozzarella'},
                                    {'id': '100 g de parmesan'}]},
], label_key='id').props("simple dense no-connectors") # icon='restaurant_menu icon='looks_3'


with ui.stepper().props('vertical').classes('w-full') as stepper:
    with ui.step("Préparation de la sauce bolognaise"):
        ui.label("Faites revenir les oignons dans de l'huile d'olive.")
        ui.label("Ajoutez les carottes. Laissez revenir.")
        ui.label("Ajoutez la viande et remuez bien le tout. Attendez que la viande soit cuite.")
        ui.label("Ajoutez la sauce tomate, le sel, le poivre, les feuilles de basilic et le verre de lait.")
        ui.label("Remuez et laissez cuire à 800W pendant 15 min puis à 600W pendant 30 min. "
                 "Si votre feu est fort vous pouvez baisser jusqu'à 400W le dernier quart d'heure.")
        with ui.stepper_navigation():
            ui.button('Suivant', on_click=stepper.next)
    with ui.step('Préparation de la sauce béchamel'):
        ui.label("Faites fondre le beurre dans une casserole sur feu vif. Lorsqu'il commence à mousser, "
                 "versez la farine d'un coup et fouettez vivement avec un fouet.")
        ui.label("Quand le mélange est homogène, versez d'un coup le lait, et fouettez fortement pour éviter la formation "
                 "de grumeaux. Salez, poivrez, et ajoutez la muscade.")
        ui.label("Continuez de fouetter sans jamais arrêter, jusqu'à ce que la béchamel commence à épaissir. "
                 "Lorsqu'elle est suffisamment épaisse, retirez-la du feu.")
        with ui.stepper_navigation():
            ui.button('Suivant', on_click=stepper.next)
            ui.button('Retour', on_click=stepper.previous).props('flat')
    with ui.step("Dressage du plat"):
        ui.label("Mettez un peu de sauce tomate simple dans le fond du plat.")
        ui.label("Précuisez quelques minutes les feuilles de lasagnes dans un grand saladier avec de l'eau très chaude.")
        ui.label("Si votre béchamel est compacte, vous pouvez la liquéfier un peu avec un peu de lait avant de dresser.")
        ui.label("Dressez chaque étage avec les feuilles de lasagnes (entre 4 et 5 selon votre plat), 3 cuillères à soupe de bolognaise, 3 cuillères à soupe de "
                 "béchamel. Mélangez bien sur chaque étage en veillant à ce que les coins soient recouverts de sauce.")
        ui.label("Mettez de la mozzarella et une pincée de parmesan avant de passer à l'étage suivant.")
        ui.label("Répetez l'opération 3 à 4 fois pour avoir des lasagnes bien hautes.")
        ui.label("Mettez le reste de béchamel et de bolognaise sur la couche supérieure avec le reste de parmesan.")
        with ui.stepper_navigation():
            ui.button('Suivant', on_click=stepper.next)
            ui.button('Retour', on_click=stepper.previous).props('flat')
    with ui.step('Cuisson'):
        ui.label("Faites cuire 25 minutes à 200°C au four à chaleur tournante.")
        ui.label("Ouvrez le four de temps en temps pour laisser échapper la vapeur.")
        ui.label("Laissez refroidir 5 minutes et servir.")
        with ui.stepper_navigation():
            ui.button('Fin', on_click=lambda: ui.notify('Mama mia !', type='positive'))
            ui.button('Retour', on_click=stepper.previous).props('flat')

with ui.footer().style('background-color: white') as footer:
    ui.label('Copyright (c) 2024 Fabien Rica').style('color: black')
    ui.link('Merci à Vittorio', 'https://vittorio.gent').style('color: black')

ui.run(reload='FLY_ALLOC_ID' not in os.environ, favicon='🤌')
