

def testing(rate_now,rate_interesting,length):
    tolorence_individual=0.5
    tolorence_total=0.5
    temp=0
    for i in range(length):
        if temp>=2:
            break
        if -0.003<rate_interesting[i]<0.003:
            if -0.006<rate_now<0.006:
                continue
        if (rate_now[i]-rate_interesting[i]*(1-tolorence_individual))*(rate_now[i]-rate_interesting[i]*(1+tolorence_individual))>=0:
            temp+=1
    if temp<2:
        if ((rate_now[length-1]-rate_now[0])-(rate_interesting[length-1]-rate_interesting[0])*(1-tolorence_total))*((rate_now[length-1]-rate_now[0])-(rate_interesting[length-1]-rate_interesting[0])*(1+tolorence_total))<=0:
            return 1
    return 0

def rate(data_interest,length):
    rate=[]
    for i in range(length):
        rate.append((data_interest[i+1]-data_interest[i])/data_interest[i])
    return rate

def finding(datas, data_interest, length_interest):
    location=0
    rate_interest=rate(data_interest,length_interest-1)
    data_now=[]
    result=[]
    temp=length_interest-1
    for i in range(length_interest):
        data_now.append(datas[i])
    rate_now=rate(data_now,length_interest-1)
    if testing(rate_now,rate_interest,length_interest-1):
        result.append(location)
    temp+=1
    while True:
        try:
            data_now.pop(0)
            data_now.append(datas[temp])
            #print(data_now)
            temp+=1
            location+=1
            rate_now=rate(data_now,length_interest-1)
            #print(rate_now)
            if testing(rate_now,rate_interest,length_interest-1):
                result.append(location)
        except IndexError:
            print(temp)
            break
    return result
    
def main():
    file=open("../INXdata_2000_now.txt", "r")
    lines=file.read()
    data=list(map(float,lines.split("\n")))
    file.close()
    file=open("../INXdata_2000_to_anal.txt", "r")
    lines=file.read()
    data_interest=list(map(float,lines.split("\n")))
    file.close()
    length_interest=len(data_interest)
    result=finding(data,data_interest,length_interest)
    print(result)
    for location in result:
        print(location,":", end=' ')
        for i in range(length_interest):
            print(data[location+i],end=', ')
        print("")

main()
