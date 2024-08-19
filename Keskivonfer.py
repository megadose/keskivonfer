import argparse
from keskivonfer import Requester

parser = argparse.ArgumentParser()
required = parser.add_argument_group('required arguments')
parser.add_argument('-v', '--vintedExtensionWebsite',help="Vinted Extension for example .fr .com default=com",required=False)
parser.add_argument('-u','--username',help="One username",required=True)
args = parser.parse_args()


infos=Requester().get_information(args.username,args.vintedExtensionWebsite)
print("Id : "+str(infos["id"]) + " | login : "+str(infos["login"]))
print("Anon id : "+str(infos["anon_id"]))
print("Real Name : "+str(infos["real_name"]))
print("Email : "+str(infos["email"]))
print("Facebook user id : "+str(infos['facebook_user_id']))
print("Birthday : "+str(infos["birthday"]))
print("Item count : "+str(infos["item_count"]))
print("Real Name : "+str(infos["real_name"]))
print("Followers : "+str(infos["followers_count"])+" | Following : "+str(infos["following_count"]))
print("Last logged on : "+str(infos["last_loged_on_ts"]))
print("City : "+str(infos["city"]) + " | Country : "+str(infos["country_title"]))

if infos["photo"] is not None:
    print("Profile picture : "+str(infos["photo"]["url"]))

else :
    print("Profile picture : "+str(infos["photo"]))
print("Verified Information's : ")

for v in infos["verification"]:
    toprint=str(v) + " "
    for i in infos["verification"][v]:
        toprint+= " | "+str(i)+" : "+str(infos["verification"][v][i])
    print(toprint)
