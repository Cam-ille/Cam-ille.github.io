import time
fin = open('words_in.txt', 'rt', encoding='utf-8-sig')
lines = fin.readlines()
fin.close()

fout = open('words_out.txt', 'wt', encoding='utf-8-sig')
for line in lines:
    # time.sleep(0.2)
    for i in range(len(line)):
        al = line[i]
        if not al.lower().islower() and al not in (' ', '-') :
            print(':'.join((line[0:i-1:],line[i:-1:])), file=fout)
            break
fout.close()