text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

space = ' '
def correctText(itext):
    newtext = ''
    for i in itext:
        if i != space:
            newtext += chr(ord(i)+2)
        else:
            newtext += i
    print(newtext)

correctText(text)