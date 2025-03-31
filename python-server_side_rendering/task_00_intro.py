from os.path import exists


def generate_invitations(template, invitees):
    if isinstance(template, str):
        if template == "":
            print("Template is empty, no output files generated.")
            return
    else:
        print("Template is not a string")
        return
    if isinstance(invitees, list):
        if len(invitees) <= 0 or not isinstance(invitees[0], dict):
            print("No data provided, no output files generated.")
            return
    else:
        print("Invitees in not a list of dictionaries")
        return
    for i, x in enumerate(invitees):
        if not exists("output_{}.txt".format(i + 1)):
            with open("output_{}.txt".format(i + 1), "w") as invite:
                message = ""
                if "name" in x.keys:
                    message = template.replace("{name}", x["name"] or "N/A")
                if "event_title" in x.keys:
                    message = message.replace("{event_title}", x["event_title"] or "N/A")
                if "event_date" in x.keys:
                    message = message.replace("{event_date}", x["event_date"] or "N/A")
                if "event_location" in x.keys:
                    message = message.replace("{event_location}", x["event_location"] or "N/A")
                invite.write(message)
