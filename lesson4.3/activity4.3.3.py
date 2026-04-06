a={"INDIA":"0091"
   ,"PAKISTAN":"0092"
   ,"BANGLADESH":"0093"
   ,"SRI LANKA":"0094"
   ,"NEPAL":"0095"
   ,"BHUTAN":"0096"
    ,"MALDIVES":"0097"
    ,"AFGHANISTAN":"0093"
    ,"MYANMAR":"0095"}
print("first coustumer hi i am from " + str(a.get("INDIA", "not found")))
print("second customer hi i am from " + str(a.get("PAKISTAN", "not found")))
print("third customer hi i am from " + str(a.get("BANGLADESH", "not found")))
print("fourth customer hi i am from " + str(a.get("SRI LANKA", "not found")))
print("fifth customer hi i am from " + str(a.get("NEPAL", "not found")))
print("sixth customer hi i am from " + str(a.get("BHUTAN", "not found")))
print("seventh customer hi i am from " + str(a.get("MALDIVES", "not found")))
print("eighth customer hi i am from " + str(a.get("AFGHANISTAN", "not found")))
print("ninth customer hi i am from " + str(a.get("MYANMAR", "not found")))
print("tenth customer hi i am from " + str(a.get("japan", "not found")))