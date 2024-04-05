from nicegui import ui
# import gettext


# TODO: find out how pot works and generates the .po file for French

# lang2 = gettext.translation('myapplication', languages=['en'])
# lang1 = gettext.translation('myapplication', languages=['fr'])

# setup in French
# lang1.install()

file = open("ingredients.md", "r", encoding="utf-8")
ui.markdown(file.read())

title = 'La vraie bonne recette de lasagnes'

with ui.header().classes() as header:
    ui.label(text=title).style('color: white; font-size: 200%; font-weight: 300')

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

ui.run()
