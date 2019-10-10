def twitter_api():
    import json
    count = 0
    retweet_lock = 0


    ## the results
    han = 0
    hon = 0
    hen = 0
    den = 0
    det = 0
    denna = 0
    denne = 0

    ## script

    with open("./0ecdf8e0-bc1a-4fb3-a015-9b8dc563a92f") as fp:
        big_data = fp.readlines()
        for line in big_data:
            if len(line)>5:
                retweet_lock = 0
                data = json.loads(line)
                for x in data:
                    if x=="retweeted_status":
                        retweet_lock = 1
                        #print("retweet count ", count)
                for x in data:
                    if x=="text" and retweet_lock==0:
                        count = count + 1
                        word_list = data[x].split(" ")
                        for word in word_list:
                            if word == "han":
                                han = han + 1
                            elif word == "hon":
                                hon = hon + 1
                            elif word == "hen":
                                hen = hen + 1
                            elif word == "den":
                                den = den + 1
                            elif word == "det":
                                det = det + 1
                            elif word == "denna":
                                denna = denna + 1
                            elif word == "denne":
                                denne = denne + 1
                            else:
                                pass



    #print("total tweet counts ", count)
    result = {"han" : han,
    "hon" : hon,
    "hen" : hen,
    "den" : den,
    "det" : det,
    "denna" : denna,
    "denne" : denne}

    to_json= json.dumps(result)
    return to_json


r_value = twitter_api()
print(r_value)
