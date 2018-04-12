def template_bd(txt):
    tag = "{{bd|"
    p = txt.find(tag)

    if p < 0: return txt
    
    t1 = txt[:p]
    t2 = txt[p + len(tag):]
    t3 = t2[t2.find("}}") + 2:]
    t2 = t2[:t2.find("}}")]

    arg = t2.split("|")

    t2 = arg[0] + arg[1] + "－"

    for a in arg[1:-1]:
        t2 += a
    return template_bd(t1 + t2 + t3)

s1 = "嘿嘿嘿abc{{bd|?年||前522年|catIdx=Z子產}}acd哈哈哈{{bd|1870年|4月22日|1924年|1月21日|catIdx=Л}}"
s2 = "（{{lang-ru|Влади́мир Ильи́ч Улья́нов|p= vɫɐˈdʲimʲɪr ɪlʲˈjit͡ɕ ʊlʲˈjænəf }}；{{bd|1870年|4月22日|1924年|1月21日|catIdx=Л}}）"

print(template_bd(s1))
print(template_bd(s2))