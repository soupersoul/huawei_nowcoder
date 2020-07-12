def make_dic(s):
    sets = s.split()
    l = int(sets[0])
    words = list(sets[1:l+1])
    target = sets[l+1]
    index = int(sets[-1])
    groups = {}
    while words:
        tk = words.pop()
        gkey = ''.join(sorted(tk))
        brothers = [tk]
        cp = words.copy()
        for w in cp:
            if gkey == ''.join(sorted(w)):
                brothers.append(w)
                words.remove(w)
        groups[gkey] = brothers
    tbrothers = groups.get(''.join(sorted(target)), [])
    try:
        tbrothers.remove(target)
    except:
        pass
    brothers = sorted(tbrothers)
    print(len(brothers))
    if brothers:
        print(brothers[index-1])

def make_dic2(s):
    terms = s.split()
    n = int(terms[0])
     
    word_list = list()
     
    i = 1
    while i < n + 1:
        word_list.append(terms[i])
        i = i + 1
         
    query_word = terms[i]
    query_index = int(terms[-1])
     
    sort_list = list()
     
    for word in word_list:
        if word == query_word:
            continue

        if len(word) != len(query_word):
            continue

        l = list(word)

        for each in query_word:
            if each in l:
                l.remove(each)
                 
        if len(l) == 0:
            sort_list.append(word)

    sort_list.sort()

    print(len(sort_list))
    print(sort_list)
    if query_index <= len(sort_list):
        print(sort_list[query_index - 1])

def make_dic3(s):
    sets = s.split()
    l = int(sets[0])
    words = list(sets[1:l+1])
    target = sets[l+1]
    index = int(sets[-1])

    brothers = []
    base = ''.join(sorted(target))
    for w in words:
        if base == ''.join(sorted(w)) and w != target:
            brothers.append(w)

    print(len(brothers))
    if index <= len(brothers):
        brothers.sort()
        print(brothers[index - 1])

make_dic3("774 ddcd aba abc b a dc abccc bdccc bcdbc cdbcd aa b dc dac a abcc cadb c dbc a bcbdb bdccb b abb ab ca caaa ddcca b acbda adbac daad cca aba dc ddcbc acbbc ca cda cbab dcbdc d d cbd dc cacaa abb dbc dbdd bb bccb a ba b babba cdcdb a ad d a baad adbab ccdaa cdbb dcbac a b ccaa aabca bd adcc bccbc a cccbb ad cbd cdadd d dbc ddbbd ab a a cddc ad adac cddba cddc c bb acdd ddd aacd cc bc cdbd ccdb da abaad db da c bad ddbb b c ad cccda ad cc bcda ba d b babd db dcb dacc adbd b daa ddaa d cdab b c ddcc a bac bc c bba bb ca ba a bbc dcbca a abb b bbacc dd bbaac dcaad cacaa ddd ada aaa abcdd b aa cdac a dca c a daaa aaadd dd caab bbda ba bdb bb bbcc a ccb dacb c acbab cbd caab aa adbb d bcc cabb ca c dcdaa dcbc dacc cdba ccca bbcd bbacc b c aca cdc aac b cb cad acdb b ccc aaba a bd ccc d ddcab dac a da dab bcab bccd cdcc babdd ccac bbcab bdbbc dc dbdaa cb aadbc c abdaa d ba dcd d bddaa ab cca dbd dac daacb cad cacd bc a ddaa caaab ddb cdccb bbcd ab b d ddc dccb bbddd cddb cbbca adb a cdcb d cbc c adad cccca a cabc dadd bddac abb cdbdb bba dbdbb aa caaba dbc c bdcda b b a bcbad aabdc abad b b c dc aaccb dacd ccc bdddc abaad b b abcd bdad a dcbc bbdcc dab dda ba bdcc aad cca dbd dabdb aacc ddb ba adc dcac c abcab d dcbbd bd daa dd baadd bd adb cabd ddd dc ada bc cccdd bdbdc c bac aaacd ab abcad ad dcda cd adab acaaa ccbdb adac ddaa dac d cdcdd abaad bb b bdd ca bb bbba c acabc aaac bda dd d acba abdad a bcd dcaa caba dca cddbd cbbac caab dcbb dbb dadbd cbad adada cddb dabbc ca a b cdabb cc bddcb aa bcdc cbad bb acbd bcb cdcad a dddd dbdc d c abccd cbc abcb ccba cc bbccd ad adbbd ca cddc dbdcc acd abad ddba da acacc bbba cbc c cdd bcad dbaa acdb daac c aba ca caad bd bccd c acbdb aadac dbbaa ad dcaa c addcd dbddb a b cabda a d cbbb c dcdd cb ccad cc a dbcc bcbc bd cacda cbbd cc bddbc b acd cdcb aaaad c aaab cb dcdaa cc ddbdc dbba bbb cabb dcda d acbbc dda aca dca d aa abbc ddb aa addc bbca bbacd abac acadb cbad caacd aabb aa bdda dcdc b adb a cba bba d bcda dbca ca bacc bcb d bcacb bd ddcab bdda bbcac cac dac acdad a bba badc ca ba db bcb d cccca abb c a dacca cdaa ca c dcb dad dcdab cc b d d ddaab aa abdad ab cacb baa bd cdc ad cd c bb d d d caabc addc d dcad b d dcbbb cbc cbbba abb acbab db dcaca abb cdd dd d b d acda bbb bcabc abc da bab cc acc aa aabdd a ddca d bb bbbbb cdd adda ddc daacb bdc bcca bbaa daabb bacca cac d d ca adda a accbc a ba bb b aa cdd cadbc dbcba abda dca aacc ccc dcb ba ddacb abbdc aaa abad cca cbcd dbc db a a b cddba dabbd dddcc b dab dbcc cccd daa db dbbbd b da ba dbdaa d c ad aaa c dd a dbdbd bdbab caad da bdbc bd aa cbac cda cbca acd cbcb daa cdcdb adac dac ca a ccc dbcab baa adbcc caba dbd db bddad cadc dcbca ac acbdb a a cdaa dc aa dbbc cdacc bdacd acba bccc da cda bc ddcaa a ca abc bccc dd cd cbab c a cdac c b ddbba bb bcdad caddc c cdaab cbcd ac abad cdcba a a acbcd caaa ca c adbcb bdcba dc b cdbd bcdb cbdb a bc dcca a bcaa bdcbb dcd ddbba b b abca c dc cdbdc c bcc bcdbb bbbcb bad cddd cabcc bddda cc ccbdc b a c bdc c c adcd cdda dbbbc caabc aa dbd ab c acacd aabb ab adcdc caca bcdd acadd cbbcb dac c dcd ac bcadd abba d c ccc cacab bdcb ad c cca bc dabc add bbdbb 2")