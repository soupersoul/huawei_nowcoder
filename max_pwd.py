def find_max_pwd(s):
    if s == s[::-1]:
        return len(s)
    maxlen = 0
    for i in range(len(s)):
        # include i
        if i - (maxlen + 2)  + 1>= 0 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
            maxlen += 2
            continue
        if i - (maxlen + 1) + 1 >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
            maxlen += 1
    return maxlen

#print(find_max_pwd('ABBA'))
#print(find_max_pwd('12ABBA'))
#print(find_max_pwd('51233214'))
#print(find_max_pwd('123321'))
#print(find_max_pwd('ABAKK'))
#print(find_max_pwd('ABA'))
print(find_max_pwd('qkvmilhdkmjqjzssjufwxvumeogpywxrixvmyvlbyuiykbzflreihurwcsdjkrhoqybjrljvwuwulmssvtrxfsvkicbnwnmzukssbtpwkdvkheeqyxtpojixxbtmbmwmlpxtwsfnltjusjkmnwzoeqvxoftenbgpystjxrjfeblfcomepsmcdkfoporeeqjobmmmsvpjfqxbtkebkwcmjtycisurvxsvttuyhtlewvdcvmlusbpkvubcvtnsduknupkznzfrbstsklcbzltmxovdcgvpycyejlsqoxhluucwocskmwxvcggzyhfcccqmcszniyypeocfkvtwuswcnynkuevgjmlwjutlgzkqsvlphsphligvqnfyrsqsnbooxecprzclqrczjimqcghtbpeovqfngjnyxyeknopsltwvibduwhtxctwqixckxxojegcrugpsqhhmpehsojobvglisylvspkgcyqebmkmohepnizjwttqvnsscgvzpqgfwfhkunpqlvvrfbpxglvnzduzsutixzkhugoixsisodxrpeqbqqwhouimrexktctwqzdspoefeooepctyestcrfxfluwxmjwogubedhdljisfmrboqcihxxjnscxwxgeftrnhvzdyiriivpsixwykydesyursbcuvvoqelyebqbcoutjnehflluqsrpprzktkgdcqnqokdhbwiccfljkukmhszexxgdfwtdonetfkfelxzsrsvbqgxyiykjvprqwfncjvimefetzftfjviiykfwmjsljpszheotouxqlvkbgkkjhecrixhxlgsemtfqfgdyfuivgiptnsmbsnuiiownshvvgdzhljztkvtbofjnpgbqlfbotrlzrdrxownjdkghsubbpzksurplcgxddfxfjiofmwtunqqgxfycoxrvwitvbcffbpimcrrcwrpbdyermztnwssxkzjqrgdmwzxdrmizsqqvdjvhzodhgstfzvktozikbiigkkszyoospiyjcsonjykrtmkcougzcjuodxbndwmwebbxmktqpzkwujedstlvjwnkfxiqgpeiqfhwbqlpprjzeswlyvgkkbwsemmbdmvzumovdqnuzjfbkhbxupwxlzqflyuefzjhdjsqythfjzedznuvqcdenqugzzhnzktrgokmfirdvnqlyxvsefevwpwwdeedogxetuqtqlqownqtojmvyidljsvwbfndssxjtlngqdqrcqlzqcojnphvvwcjmrebkenurdemjoicnquqfzhpwbbqbfisersjpodpvklypjnnwyfeputelulpppuotnepmptxr'))