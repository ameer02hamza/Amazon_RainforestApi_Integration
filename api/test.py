import json
data = {"cate": [
    {"position": 1,
     "title": "Canon",
     "asin": "2nsn",
     "prices": [
         {
             "symbol": "$",
             "Value": "399",
             "currency": "USD",
         }
     ]
     },
    {"position": 2,
     "title": "Nikon",
     "asin": "2nsn",
     "prices": [

        {
             "symbol": "$",
             "Value": "566",
             "currency": "USD",
         }
     ]
     },
    {"position": 3,
     "title": "Sony",
     "asin": "dadsda",
     "prices": [
         {
             "symbol": "$",
             "Value": "88",
             "currency": "USD",
         },

     ]
     }
]}
d = json.loads(json.dumps(data))
# print(d["cate"][1])

# for i in range(len(d["cate"])):
#     # print(d["cate"][i])
#     l = len(d["cate"][i]["prices"])-1
#     print(l)
#     print(d["cate"][i]["prices"][l]["Value"])



