# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:31:17 2018

@author: foxta
"""

#import nltk
import nltk

from nltk import word_tokenize

#print stopwords in EN, one per line
stopwordsEN = nltk.corpus.stopwords.words('english')
for swEN in stopwordsEN:
    #print(swEN)

#print stopwords in FR, one per line
stopwordsFR = nltk.corpus.stopwords.words('french')
for swFR in stopwordsFR:
    #print(swFR)

#print stopwords in ES, one per line
stopwordsES = nltk.corpus.stopwords.words('spanish')
for swES in stopwordsES:
    print(swES)
    
#print stopwords in CA, one per line
#source: http://latel.upf.edu/morgana/altres/pub/ca_stop.htm
stopwordsCA1 = " a, abans, abans-d'ahir, abintestat, ací, adesiara, adés, adéu, adàgio, ah, ahir, ai, aitambé, aitampoc, aitan, aitant, aitantost, aixà, això, així, aleshores, algun, alguna, algunes, alguns, algú, alhora, allà, allèn, allò, allí, almenys, alto, altra, altre, altres, altresí, altri, alça, al·legro, amargament, amb, ambdues, ambdós, amunt, amén, anc, andante, andantino, anit, ans, antany, apa, aprés, aqueix, aqueixa, aqueixes, aqueixos, aqueixs, aquell, aquella, aquelles, aquells, aquest, aquesta, aquestes, aquests, aquèn, aquí, ara, arran, arrera, arrere, arreu, arri, arruix, atxim, au, avall, avant, aviat, avui, açò, bah, baix, baldament, ballmanetes, banzim-banzam, bastant, bastants, ben, bis, bitllo-bitllo, bo, bé, ca, cada, cal, cap, car, caram, catorze, cent, centes, cents, cerca, cert, certa, certes, certs, cinc, cinquanta, cinquena, cinquenes, cinquens, cinquè, com, comsevulla, contra, cordons, corrents, cric-crac, d, daixonses, daixò, dallonses, dallò, dalt, daltabaix, damunt, darrera, darrere, davall, davant, de, debades, dedins, defora, dejorn, dejús, dellà, dementre, dempeus, demés, demà, des, desena, desenes, desens, després, dessobre, dessota, dessús, desè, deu, devers, devora, deçà, diferents, dinou, dins, dintre, disset, divers, diversa, diverses, diversos, divuit, doncs, dos, dotze, dues, durant, ecs, eh, el, ela, elis, ell, ella, elles, ells, els, em, emperò, en, enans, enant, encara, encontinent, endalt, endarrera, endarrere, endavant, endebades, endemig, endemés, endemà, endins, endintre, enfora, engir, enguany" 
stopwordsCA1 = stopwordsCA1.split(",")
stopwordsCA2 = " enguanyasses, enjús, enlaire, enlloc, enllà, enrera, enrere, ens, ensems, ensota, ensús, entorn, entre, entremig, entretant, entrò, envers, envides, environs, enviró, ençà, ep, ep, era, eren, eres, ergo, es, escar, essent, esser, est, esta, estada, estades, estan, estant, estar, estaran, estarem, estareu, estaria, estarien, estaries, estaré, estarà, estaràs, estaríem, estaríeu, estat, estats, estava, estaven, estaves, estem, estes, esteu, estic, estiguem, estigueren, estigueres, estigues, estiguessis, estigueu, estigui, estiguin, estiguis, estigué, estiguérem, estiguéreu, estigués, estiguí, estos, està, estàs, estàvem, estàveu, et, etc, etcètera, ets, excepte, fins, fora, foren, fores, força, fos, fossin, fossis, fou, fra, fui, fóra, fórem, fóreu, fóreu, fóssim, fóssiu, gaire, gairebé, gaires, gens, girientorn, gratis, ha, hagi, hagin, hagis, haguda, hagudes, hagueren, hagueres, haguessin, haguessis, hagut, haguts, hagué, haguérem, haguéreu, hagués, haguéssim, haguéssiu, haguí, hala, han, has, hauran, haurem, haureu, hauria, haurien, hauries, hauré, haurà, hauràs, hauríem, hauríeu, havem, havent, haver, haveu, havia, havien, havies, havíem, havíeu, he, hem, heu, hi, ho, hom, hui, hàgim, hàgiu, i, igual, iguals, inclusive, ja, jamai, jo, l, la, leri-leri, les, li, lla, llavors, llevat, lluny, llur, llurs, lo, los, ls, m, ma, mai, mal, malament, malgrat, manco, mant, manta, mantes, mantinent, mants, massa, mateix, mateixa, mateixes, mateixos, me, mentre, mentrestant, menys, mes, meu, meua, meues, meus, meva, meves, mi, mig, mil, mitges, mitja, mitjançant, mitjos, moixoni, molt, molta, moltes, molts, mon, mos, més, n, na, ne, ni, ningú, no, nogensmenys, només, noranta, nos, nosaltres, nostra, nostre, nostres, nou, novena, novenes, novens, novè, ns, nòs, nós, o, oh, oi, oidà, on, onsevulga, onsevulla, onze, pas, pengim-penjam, per, perquè, pertot, però, piano, pla, poc, poca, pocs, poques, potser, prest, primer, primera, primeres, primers, pro, prompte, prop, prou, puix, pus, pàssim, qual, quals, qualsevol, qualsevulla, qualssevol, qualssevulla, quan, quant, quanta, quantes, quants, quaranta, quart, quarta, quartes, quarts, quasi, quatre, que, quelcom, qui, quin, quina, quines, quins, quinze, quisvulla, què, ran, re, rebé, renoi, rera, rere, res, retruc, s, sa, salvament, salvant, salvat, se, segon, segona, segones, segons, seguida, seixanta, sempre, sengles, sens, sense, ser, seran, serem, sereu, seria, serien, series, seré, serà, seràs, seríem, seríeu, ses, set, setanta, setena, setenes, setens, setze, setè, seu, seua, seues, seus, seva, seves, si, sia, siau, sic, siguem, sigues, sigueu, sigui, siguin, siguis, sinó, sis, sisena, sisenes, sisens, sisè, sobre, sobretot, sol, sola, solament, soles, sols, som, son, sos, sota, sots, sou, sovint, suara, sí, sóc, són, t, ta, tal, tals, també, tampoc, tan, tanmateix, tant, tanta, tantes, tantost, tants, te, tercer, tercera, terceres, tercers, tes, teu, teua, teues, teus, teva, teves, ton, tos, tost, tostemps, tot, tota, total, totes, tothom, tothora, tots, trenta, tres, tret, tretze, tu, tururut, u, uf, ui, uix, ultra, un, una, unes, uns, up, upa, us, va, vagi, vagin, vagis, vaig, vair, vam, van, vares, vas, vau, vem, verbigràcia, vers, vet, veu, vint, vora, vos, vosaltres, vostra, vostre, vostres, vostè, vostès, vuit, vuitanta, vuitena, vuitenes, vuitens, vuitè, vés, vàreig, vàrem, vàreu, vós, xano-xano, xau-xau, xec, érem, éreu, és, ésser, àdhuc, àlies, ça, ço, òlim, ídem, últim, última, últimes, últims, únic, única, únics, úniques"
stopwordsCA2 = stopwordsCA2.split(",")

counter1 = 0
for i in stopwordsCA1:
    print(stopwordsCA1[counter1])   
    counter1 = counter1 + 1

counter2 = 0 
for i in stopwordsCA2:
    print(stopwordsCA2[counter2])   
    counter2 = counter2 + 1
    
        