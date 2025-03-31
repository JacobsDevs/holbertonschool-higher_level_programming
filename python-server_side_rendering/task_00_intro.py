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
                keys = ["{name}", "{event_title}", "{event_date}", "{event_location}"]
                dict_keys = x.keys()
                message = template
                for ind, k in enumerate(keys):
                    try:
                        message = message.replace("{}".format(k), x[k.strip("{}")] or "N/A")
                    except Exception as e:
                        print(e)
                        print(dict_keys)
                        message = message.replace("{}".format(k), "N/A")
                invite.write(message)
