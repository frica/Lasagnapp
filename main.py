from nicegui import ui
import os
from gettext import translation

localedir = './locales'
DEFAULT_LANG = 'fr'
lang_fr = translation('base', localedir=localedir, fallback=False, languages=[DEFAULT_LANG])
lang_fr.install()


def switch_language(language_code):
    ui.notify(f"Switching to \"{language_code}\"")
    language = translation('base', localedir=localedir, fallback=True, languages=[language_code])
    language.install()
    build_ui.refresh()


@ui.refreshable
def build_ui():
    with ui.row():
        ui.label(_("Ingrédients: (pour 6 à 8 personnes)")).style('font-weight: bold')
        ui.button("FR 🇫🇷", on_click=lambda: switch_language("fr")).style('font-size : 10px').props('sm outline dense')
        ui.button("EN 🇬🇧", on_click=lambda: switch_language("en")).style('font-size : 10px').props('sm outline dense')

    # Based on Quasar so use props to set component styling
    ui.tree([
        {'id': _("Sauce bolognaise"),
         'children': [{'id': _('1 kg de viande: 600g filet américain pur boeuf et 400 g de haché veau + porc')},
                      {'id': _('2 oignons')},
                      {'id': _('1 à 2 carottes')},
                      {'id': _('1200 ml de sauce tomate')},
                      {'id': _('Sel')},
                      {'id': _('Poivre')},
                      {'id': _('Un petit verre de lait')}]},
    ], label_key='id').props("dense no-connectors").style("color: #8B4513")  # icon='looks_one'

    ui.tree([
        {'id': _(' Sauce béchamel'), 'children': [{'id': _('50 cl de lait')},
                                                  {'id': _('50 g de beurre')},
                                                  {'id': _('50 g de farine')},
                                                  {'id': _('Noix de muscade')}]},
    ], label_key='id').props("dense no-connectors").style("color: #8B4513")  # icon='looks_two'

    ui.tree([
        {'id': _('Lasagnes'), 'children': [{'id': _('Un paquet de lasagnes avec une vingtaine de feuilles')},
                                           {'id': _('150 g de mozzarella')},
                                           {'id': _('100 g de parmesan')}]},
    ], label_key='id').props("simple dense no-connectors").style(
        "color: #8B4513")  # icon='restaurant_menu icon='looks_3'

    with ui.stepper().props('vertical').classes('w-full') as stepper:
        with ui.step(_("Préparation de la sauce bolognaise")):
            ui.label(_("Faites revenir les oignons dans de l'huile d'olive."))
            ui.label(_("Ajoutez les carottes. Laissez revenir."))
            ui.label(_("Ajoutez la viande et remuez bien le tout. Attendez que la viande soit cuite."))
            ui.label(_("Ajoutez la sauce tomate, le sel, le poivre, les feuilles de basilic et le verre de lait."))
            ui.label(_("Remuez et laissez cuire à 800W pendant 15 min puis à 600W pendant 30 min. "
                       "Si votre feu est fort vous pouvez baisser jusqu'à 400W le dernier quart d'heure."))
            with ui.stepper_navigation():
                ui.button(_('Suivant'), on_click=stepper.next)
        with ui.step(_('Préparation de la sauce béchamel')):
            ui.label(_("Faites fondre le beurre dans une casserole sur feu vif. Lorsqu'il commence à mousser, "
                       "versez la farine d'un coup et fouettez vivement avec un fouet."))
            ui.label(
                _("Quand le mélange est homogène, versez d'un coup le lait, et fouettez fortement pour éviter la formation "
                  "de grumeaux. Salez, poivrez, et ajoutez la muscade."))
            ui.label(_("Continuez de fouetter sans jamais arrêter, jusqu'à ce que la béchamel commence à épaissir. "
                       "Lorsqu'elle est suffisamment épaisse, retirez-la du feu."))
            with ui.stepper_navigation():
                ui.button(_('Suivant'), on_click=stepper.next)
                ui.button(_('Retour'), on_click=stepper.previous).props('flat')
        with ui.step(_("Dressage du plat")):
            ui.label(_("Mettez un peu de sauce tomate simple dans le fond du plat."))
            ui.label(
                _("Précuisez quelques minutes les feuilles de lasagnes dans un grand saladier avec de l'eau très chaude."))
            ui.label(
                _("Si votre béchamel est compacte, vous pouvez la liquéfier un peu avec un peu de lait avant de dresser."))
            ui.label(
                _("Dressez chaque étage avec les feuilles de lasagnes (entre 4 et 5 selon votre plat), 3 cuillères à "
                  "soupe de bolognaise, 3 cuillères à soupe de béchamel. Mélangez bien sur chaque étage en veillant à "
                  "ce que les coins soient recouverts de sauce."))
            ui.label(_("Mettez de la mozzarella et une pincée de parmesan avant de passer à l'étage suivant."))
            ui.label(_("Répetez l'opération 3 à 4 fois pour avoir des lasagnes bien hautes."))
            ui.label(
                _("Mettez le reste de béchamel et de bolognaise sur la couche supérieure avec le reste de parmesan."))
            with ui.stepper_navigation():
                ui.button(_('Suivant'), on_click=stepper.next)
                ui.button(_('Retour'), on_click=stepper.previous).props('flat')
        with ui.step(_('Cuisson')):
            ui.label(_("Faites cuire 25 minutes à 200°C au four à chaleur tournante."))
            ui.label(_("Ouvrez le four de temps en temps pour laisser échapper la vapeur."))
            ui.label(_("Laissez refroidir 5 minutes et servir."))
            with ui.stepper_navigation():
                ui.button(_('Fin'), on_click=lambda: ui.notify('Mama mia !', type='positive'))
                ui.button(_('Retour'), on_click=stepper.previous).props('flat')


app_name = 'Lasagnapp'
ui.page_title(app_name)

# app styling: font, bg color and step font size
ui.add_head_html('''
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Handlee&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans" rel="stylesheet">
    <style>
        header {
            font-family: 'Handlee', serif;
            font-color : black;
            font-size : 38px;
        }
        body {
            font-family: 'Noto Sans', serif;
            font-size : 16px;
      }
    </style>
''')

# in case you want to change body background
# ui.query('body').style('background-color: #ffeedd')
ui.add_css('.q-stepper__title { font-size: 18px; color: black}')
ui.colors(primary='#BD2B26')

title = _('La vraie bonne recette de lasagnes')

with ui.header().style('background-color: white') as header:
    ui.label(text=title).style("color: black; font-weight: bold")
    ui.separator().props('color=black size=2px')

build_ui()

with (ui.footer().style('background-color: white') as footer):
    ui.markdown('Copyright (c) 2024 Fabien Rica 🇫🇷 & [Vittorio](https://vittorio.gent)  🇮🇹').style(
        'color: black; font-size : 14px')

ui.run(reload='FLY_ALLOC_ID' not in os.environ, favicon='🤌')

# design experiments

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
