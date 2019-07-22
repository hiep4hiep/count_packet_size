import csv

top_dest = {}
count_http = {}
count_https = {}
top_test = {}

def add_list(list,address,count):
    list[address] = count

#with open('log_traffic_filter.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader:
#        if row[3] == '103.53.88.124' and row[16] == '443':
#            line_count += 1
#    add_list(top_test,'103.53.88.124 port 80',line_count)

def get_value_all_http(subnet):
    line_count = 0
    for ip in range(1,255):
        line_count = 0
        csv_file = open('log_traffic_filter.csv','r')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[3] == subnet+str(ip) and row[16] == '80':
                line_count += 1
        add_list(top_dest,subnet+str(ip)+' port 80',line_count)
        csv_file.close()
    return(top_dest)

def get_value_all_https(subnet):
    line_count = 0
    for ip in range(1,255):
        line_count = 0
        csv_file = open('log_traffic_filter.csv','r')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[3] == subnet+str(ip) and row[16] == '443':
                line_count += 1
        add_list(top_dest,subnet+str(ip)+' port 443',line_count)
        csv_file.close()
    return(top_dest)


def get_value_specific_http(ip):
    _less100 = 0
    _100to500 = 0
    _500to1k = 0
    _1kto2k = 0
    _2kto10k = 0
    _10kto16k = 0
    _17kto60k = 0
    _64kto128k = 0
    _128kto1m = 0
    _1mto6m = 0
    line_count = 0
    csv_file = open('log_traffic_filter.csv','r')
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[3] == ip and row[16] == '80' and int(int(row[19])) < 100:
            _less100 += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 100 and int(row[19]) < 500:
            _100to500 += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 500 and int(row[19]) < 1000:
            _500to1k += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 1000 and int(row[19]) < 2000:
            _1kto2k += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 2000 and int(row[19]) < 10000:
            _2kto10k += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 10000 and int(row[19]) < 16000:
            _10kto16k += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 16000 and int(row[19]) < 64000:
            _17kto60k += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 64000 and int(row[19]) < 128000:
            _64kto128k += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 1280000 and int(row[19]) < 1000000:
            _128kto1m += 1
        if row[3] == ip and row[16] == '80' and int(row[19]) > 1000000 and int(row[19]) < 6000000:
            _1mto6m += 1
    add_list(count_http,'<100',_less100)
    add_list(count_http, '100to500', _100to500)
    add_list(count_http, '500to1k', _500to1k)
    add_list(count_http, '1kto2k', _1kto2k)
    add_list(count_http, '2kto10k', _2kto10k)
    add_list(count_http, '10kto16k', _10kto16k)
    add_list(count_http, '17kto60k', _17kto60k)
    add_list(count_http, '64kto128k', _64kto128k)
    add_list(count_http, '128kto1m', _128kto1m)
    add_list(count_http, '1mto6m', _1mto6m)
    add_list(count_http, 'total_http',_less100 + _100to500 + _1kto2k + _2kto10k + _10kto16k + _17kto60k + _64kto128k + _128kto1m + _1mto6m)
    csv_file.close()
    return(count_http)

def get_value_specific_https(ip):
    _0to1k = 0
    _1kto2k = 0
    _2kto10k = 0
    _10kto16k = 0
    _17kto64k = 0
    _64kto128k = 0
    _128kto1m = 0
    _1mplus = 0
    line_count = 0
    csv_file = open('log_traffic_filter.csv','r')
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[3] == ip and row[16] == '443' and int(int(row[19])) < 1000:
            _0to1k += 1
        if row[3] == ip and row[16] == '443' and int(row[19]) > 1000 and int(row[19]) < 2000:
            _1kto2k += 1
        if row[3] == ip and row[16] == '443' and int(row[19]) > 2000 and int(row[19]) < 10000:
            _2kto10k += 1
        if row[3] == ip and row[16] == '443' and int(row[19]) > 10000 and int(row[19]) < 16000:
            _10kto16k += 1
        if row[3] == ip and row[16] == '443' and int(row[19]) > 16000 and int(row[19]) < 60000:
            _17kto64k += 1
        if row[3] == ip and row[16] == '443' and int(row[19]) > 64000 and int(row[19]) < 128000:
            _64kto128k += 1
        if row[3] == ip and row[16] == '443' and int(row[19]) > 1280000 and int(row[19]) < 1000000:
            _128kto1m += 1
        if row[3] == ip and row[16] == '443' and int(row[19]) > 1000000 and int(row[19]) < 20000000:
            _1mplus += 1
    add_list(count_https,'<100',_0to1k)
    add_list(count_https, '1kto2k', _1kto2k)
    add_list(count_https, '2kto10k', _2kto10k)
    add_list(count_https, '10kto16k', _10kto16k)
    add_list(count_https, '17kto60k', _17kto64k)
    add_list(count_https, '64kto128k', _64kto128k)
    add_list(count_https, '128kto1m', _128kto1m)
    add_list(count_https, '1mto6m', _1mplus)
    add_list(count_https, 'total_https', _0to1k + _1kto2k + _2kto10k + _10kto16k + _17kto64k + _64kto128k + _128kto1m + _1mplus)
    csv_file.close()
    return(count_https)

ipaddr = input('Which ip you want to check: ')
#sub = input('Which subnet you want to check: ')
#print("Packet count for subnet")
print("Packet count http for "+ ipaddr + " is:")
print(get_value_specific_http(ipaddr))
print("Packet count https for "+ ipaddr + " is:")
print(get_value_specific_https(ipaddr))
#print(top_test)
#print(top_dest['103.53.88.65 port 80'])

