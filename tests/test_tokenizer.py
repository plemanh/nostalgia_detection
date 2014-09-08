# -*- coding: utf-8 -*-
'''
test tokenizer.py
'''
import os
os.chdir('/Users/paullemanh/Dev/nostalgia_detection')
from algos.tokenizer import tokenizer

content= u"Cela fait aujoud'hui 14 jours que Fouad Mourtada a été arrêté pour avoir commis l'erreur, mais pas le délit, de créer un profil sur Facebook au nom duprince Moulay Rachid, sans que ce profil ne contienne d'injures ou n'ait servi à des tentatives d'escroquerie. Son nom fût immédiatement livré en pâture au public, au mépris de toute présomption d'innocence, et il affirme avoir été frappé et maltraité lors de son arrestation. Il a initialement eu des difficultés à trouver un avocat disposé à le défendre. L'audience, prévue pour le 15 février dernier, a été reportée au vendredi 22 février, et la demande de mise en liberté provisoire a été rejetée. Pour cette raison, ce blog sera en grève ce mardi 19 en solidarité avec Fouad Mourtada. Pour en savoir plus sur le cas de Fouad Mourtada, le site de son comité de soutien: http://www.helpfouad.com/ . Solidaires : moonlight , mazagan , zskdan , taha balafrej , AbMoul , Farid Taha , Eatbees , Ibn Kafka , Bunix, Reda , LionnedAtlas , EcoMaroc , BLUESMAN , SEM , Larbi , Naim , Ayoub , Laila Lalami , Mohamed El Kortbi , mecano , citoyenhmida , Loula la nomade , Fhamator , B2 , SABA , Lady Zee , kb, SimoBenso , Laurent Bervas , kenza , Zaz , ML et bien d'autres... --- Ce billet grève est bien le dernier gravé sur le log de ce navire. J’aurai préféré voir coulé cette embarcation sur une note plus gaie, mais les circonstances ont fait que … dommage. C'est ce que retiendra l'Eternité, ou du moins l'espérance de vie des serveurs Google. Maintenant, joignez-vous à nous aux obsèques de ce que fut cette aventure. Saba , moony ... it would never have worked between us darlings. I'm sorry... Fhamator ... nice defense. Friends... This is the day that you will always remember as the day that you almost caught... Au revoir"	
print('#################################')
print('###Web content to be tokenized###')
print('#################################')
print(content)
#Default tokenizer
tokenizerObj = tokenizer('french')
sentences = tokenizerObj.getSentences(content)
print('#################################')
print('############Sentences############')
print('#################################')
print(sentences)
tokens = tokenizerObj.getTokens(sentences[1])
print('#################################')
print('##############Tokens#############')
print('#################################')
print(tokens)

#tokenizer with stemmer
tokenizerObjBis = tokenizer('french', stemming=True)
tokens = tokenizerObjBis.getTokens(sentences[1])
print('#################################')
print('#######Tokens with stemming######')
print('#################################')
print(tokens)