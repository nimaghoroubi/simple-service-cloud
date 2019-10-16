import json
import tarfile

def twitter_api():
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
    limit = 0
    #reading tarfile
    tar = tarfile.open("/media/stewie/Median/Applied Cloud Computing/Labs/Lab 3/data.tar.gz", "r:gz")
    members = tar.getmembers()
    for member in members:
        fp = tar.extractfile(member)
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
