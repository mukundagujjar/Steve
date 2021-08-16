import wolframalpha
import PySimpleGUI as sg
import wikipedia


client = wolframalpha.Client('4HPU7Q-VXTP3YW8R7')

sg.theme('DarkBlue')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Person',size=(6,1)), sg.InputText(key='person',do_not_clear=False)],
            [sg.Text('Place',size=(6,1)), sg.InputText(key='place',do_not_clear=False)],
            [sg.Button('Summary',size=(7,1),key="summary"),sg.Button('Details',size=(7,1),key="details")],
            [sg.Text('_'*54)],
            [sg.Text('Formula',size=(6,1)), sg.InputText(key='formula',do_not_clear=False)],
            [sg.Text('General',size=(6,1)), sg.InputText(key='general',do_not_clear=False)],
            [sg.Button('Search',size=(7,1),key="search")] ]

# Create the Window
window = sg.Window('Steve', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:	# if user closes window or clicks cancel
        break

    if event == "summary":
        if values['place']:
            try:
                wiki = wikipedia.page(values['place'])
                sg.popup_non_blocking(wikipedia.summary(values['place'],sentences=4),title=wiki.title)     
            except:
                query1 = client.query(values['place'])
                res = next(query1.results).text
                sg.popup_non_blocking(res,title=values['place'])
        if values['person']:
            try:
                wiki = wikipedia.page(values['person'])
                sg.popup_non_blocking(wikipedia.summary(values['person'],sentences=4),title=wiki.title)     
            except:
                sg.popup_non_blocking("Sorry. I don't know who this person is.",title='UwU')
    
    if event=='details':
        if values['person']:
            wiki0 = wikipedia.page(values['person'])
            wiki = wikipedia.summary(values['person'])
            sg.popup_scrolled(wiki,title=wiki0.title,non_blocking=True,grab_anywhere=True)
        if values['place']:
            wiki0 = wikipedia.page(values['place'])
            wiki = wikipedia.summary(values['place'])
            sg.popup_non_blocking(wiki,title=wiki0.title)
            
    if event == 'search':
        if values['formula']:
            query1 = client.query(values['formula'])
            res = next(query1.results).text
            sg.popup_non_blocking(res,title=values['formula'])


                 

    

window.close()
