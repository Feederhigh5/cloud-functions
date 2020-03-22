#Noch nicht implementiert
#
#
#Hole Fragen und Antworten aus RKI FAQ

from requests_html import HTMLSession
session= HTMLSession()
r= session.get("https://www.rki.de/SharedDocs/FAQ/NCOV2019/FAQ_Liste.html")
accordeon=r.html.find('.alt-accordion-box-box')
fragen=[]
antwort=[]
for frage in accordeon:
    fragen.append((frage.text.split('?')[0] + '?'))
    antwort.append(frage.text.split('?')[1])
fragenantwort=dict(zip(fragen,antwort))

#
#
# Code um Knoten per API hinzuzufügen
#
#
 def create_node(workspace_id, intent, answer, debug=False):

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    nodeid = intent + "" + str(timestamp)

    try:
        node_response = assistant.create_dialog_node(
            workspace_id = workspace_id,
            dialog_node = node_id,
            conditions = "#" + intent,
            previous_sibling = welcome_node_id,
            title = intent,
            output = {
                'generic': [
                    {
                        'response_type': 'text',
                        'values': [
                            {
                                'text': answer
                            }
                        ]
                    }
                ]
            }
        ).get_result()

        if debug:
            print(json.dumps(node_response, indent=2))
        return {'success': True}
    except Exception as ex:
        return {'success': False, 'comment': 'An exception occurred: ' + str(ex)}
