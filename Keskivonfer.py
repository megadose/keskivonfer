from keskivonfer import getInfo
import argparse
parser = argparse.ArgumentParser()
required = parser.add_argument_group('required arguments')
parser.add_argument('-v', '--vintedExtensionWebsite',help="Vinted Extension for example .fr .com default=com",required=False)
parser.add_argument('-u','--username',help="One username",required=True)
args = parser.parse_args()


infos=getInfo(args.username,args.vintedExtensionWebsite)
print("Id : "+str(infos["id"]) + " | login : "+str(infos["login"]))
print("Anon id : "+str(infos["anon_id"]))
print("Real Name : "+str(infos["real_name"]))
print("Email : "+str(infos["email"]))
print("Facebook user id : "+str(infos['facebook_user_id']))
print("Gender : "+str(infos["gender"])+" | Birthday : "+str(infos["birthday"]))
print("Item count : "+str(infos["item_count"]))
print("Real Name : "+str(infos["real_name"]))
print("Followers : "+str(infos["followers_count"])+" | Following : "+str(infos["following_count"]))
print("Created at : "+str(infos["created_at"]))
print("Last loged on : "+str(infos["last_loged_on_ts"]))
print("City : "+str(infos["city"]) + " | Country : "+str(infos["country_title"]))
if infos["photo"]["url"]!=None:
    print("Profile pictue : "+str(infos["photo"]["url"]))
else :
    print("Profile pictue : "+str(infos["photo"]))
print("Verified Informations : ")

for v in infos["verification"]:
    toprint=str(v) + " "
    for i in infos["verification"][v]:
        toprint+= " | "+str(i)+" : "+str(infos["verification"][v][i])
    print(toprint)
