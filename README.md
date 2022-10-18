# X3IA020 ALMA - Expérience PageRank Performance
### Faculté des Sciences et des Techniques - Nantes Université  
Gestion des données distribuées à large échelle  
**Professeur**: MOLLI Pascal  
**Étudiants**: BA RAGAA Mohammed ali ahmed, JIMENEZ Oswaldo  
PageRank - comparaison Pig vs PySpark. Consigne: https://madoc.univ-nantes.fr/mod/assign/view.php?id=1523335 

[1. Introduction - Description de l'expérience](#1-introduction---description-de-lexpérience)  
[2. Exécutions pagerank - Pig vs PySpark](#2-exécutions-pagerank---pig-vs-pyspark)  
[3. Meilleur pagerank](#3-meilleur-pagerank)  
[4. Conclusions et recommendations](#4-conclusions-et-recommendations)

# 1. Introduction - Description de l'expérience
Le but de cette expérience c'est de comparer les performances de l'algorithme [pagerank](https://fr.wikipedia.org/wiki/PageRank), entre une implantation [Pig](https://en.wikipedia.org/wiki/Pig_Latin#:~:text=Pig%20Latin%20is%20a%20language,to%20create%20such%20a%20suffix.) et une implantation [PySpark](https://spark.apache.org/docs/latest/api/python/). Cette expérience est inspiré d'une expérience realisée lors de la conférence [NDSI 2012 présentation des Resilient Distributed Datasets (RDD)](https://www.youtube.com/watch?v=dXG4yC8ICEI).

On compare les temps d'exécutions du pagerank avec des diagrammes dans la [section 2]((#2-exécutions-pagerank---pig-vs-pyspark)  ), ensuite les meilleurs pagerank trouvés sont illustrés dans la [section 3]((#3-meilleur-pagerank) ). Des conclusions basées sur ces comparaison et le déroulement de l'expérience sont abordés dans la [section 4](#4-conclusions-et-recommendations).

Ci-apres on enumére les configurations et considérations tenus en compte lors des exécutions Pig et PySpark.

## 1.1 Configurations utilisées
Afin de mesurer la performance d'exécution entre les implémentations Pig et Pyspark, nous avons eu recours au service d'exécution de tâches [Dataproc](https://cloud.google.com/dataproc?hl=fr) de la suite Google cloud. Les considerations et configurations utilisées pour réaliser cette expérience se résument ci-après:
* **Paramètres pagerank**: le nombre d'iterations a été fixé à 3, et le facteur pagerank utilisé de {d = 0.85}, pour les deux implementations. 
* **Nombres de workers**: 2, 3, 4 et 5
* **La région**: europe-west1, défini en function de la proximité avec le bucket hebergéant les données d'entrée
* **Dataset d'entrée**: dataset [page_links_en.nt.bz2](http://downloads.dbpedia.org/3.5.1/en/page_links_en.nt.bz2), disponibles sur le bucket publique gs://public_lddm_data//page_links_en.nt.bz2
* **Version PIG installé dans le cluster**: Apache Pig version 0.18.0-SNAPSHOT
* **Version pyspark installé dans le cluster**: 

Implementations du pagerank utilisées:
* Implementation Pig (copyright pascal) 
* Implementation PySpark (copyright pascal) 
* Implementation PySpark partition controle 

Les résultats de l'exécution avec les configurations citées sont presentés dans la section suivante.
# 2. Exécutions pagerank - Pig vs PySpark
Ci-dessous on présente les résultats issus des exécutions pageranks dans les différentes configurations de cluster. Pour l'implementation pyspark, on distingue le temps d'exécution de l'implémentation sans et avec partitionnement contrôlé.

## PIG
| Nombre de noeuds | Temps d'exécution  | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 49 min 52 sec | 83edf25aa5e24364a1ea968a99ab415f |
| 3 | 37 min 25 sec | 85961f8339bc43bcbaf5cf69cd13719d |
| 4 | 34 min 34 sec | 6d80276d638d4d0096f0d2bbad55debc |
| 5 | 29 min 45 sec | 1ad6eaf435d24191878899943ae73a15 |

## PySpark Basic
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 43 min 30 sec | 895b7b281f794d4393278962e01169ad |
| 3 | 38 min 23 sec | 527ace71d1ce4f9da1b5f5ab5581c2dd |
| 4 | 35 min 28 sec | e870244c239b47e1bf2e6c86691d4bfa |
| 5 | 35 min 04 sec | 9d52c020836c41cba2c50e3da3de29e7 |

## PySpark avec partionnement
Afin d'éviter les shuffles entre join, une mise en place des partitions contrôlées a été rajouté au script pyspark. Le nombre de partitions a eté laissé [par défaut](https://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.partitionBy), et pour la function de partitionnement un lambda utilisant les mêmes partitions d'url a été mis en place.
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 42 min 48 sec | 71dd624351af42128d8d321c5fc314dd |
| 3 | 31 min 41 sec | f0c04b5b485b4504952c75b7e51b3e44 |
| 4 | 29 min 12 sec | 3f475ada46de4c7ab8e0ca526c1ed5a5 |
| 5 | 30 min 20 sec | 98c8047900634a33882b2296b8a8293a |

## PIG vs PySpark Basic vs PySpark avec partionnement

Ci-après suit un diagramme de ligne illustrant la comparaison des temps d'exécution entre les implémentations pagerank, pour chaque configuration de cluster utilisée
<br/>
<img align=center src= https://github.com/oahjimenez/x3ia020_pagerank/blob/main/comp_diag.png>
<br/>
Sur ce graphique nous pouvons constater les points suivants:
* Pig est l'implémentation la moins performante avec deux noeuds, ce qui pourrait s'expliquer par les écritures des résultats intermediaries sur le disque avec des ressources limitées. 
* PySpark avec du partitionnement est l'implémentation qui performe le mieux en moyen, néanmoins cette implémentation atteint un seuil à 4 noeuds, et ensuite est rattrapé par Pig à 5 noeuds.
* Pig bénéficie plus de l'augmentation dans le nombre de workers, on peut apercevoir cela surtout dans l'increment de nombre de noeuds de 4 à 5, où l'on voit que les implémentatios sur PySpark atteignent un seuil dans leurs temps d'exécution, tandis que le temps d'exécution continue à diminuer pour Pig.
* Avec des ressources limitées (2 noeuds), Pyspark ne semble pas bénéficier d'une amélioration en raison du partionnement.

Les résultats des meilleurs pagerank trouvés sont présentés dans la section suivante.
# 3. Meilleur pagerank
Avec cette expérience nous avons obtenu que l'entité avec le plus grand pagerank c'est l'uri <http://dbpedia.org/resource/Living_people>, avec un pagerank de **36,794.33**. On présente ci-après le top 10 d'url ayant les meilleur pagerank, issue de 3 itérations de l'algorithme pagerank.
| Rank | Url  | Pagerank |
| ---- | ------------- | ------------- |
|:1st_place_medal:| http://dbpedia.org/resource/Living_people | 36794.33146754463  |
|:2nd_place_medal:| http://dbpedia.org/resource/United_States | 13201.340151981207  |
|:3rd_place_medal:| http://dbpedia.org/resource/Race_and_ethnicity_in_the_United_States_Census | 10371.162005541351  |
|4| http://dbpedia.org/resource/List_of_sovereign_states  | 5195.34736186218  |
|5| http://dbpedia.org/resource/United_Kingdom  | 4923.82130931521  |
|6| http://dbpedia.org/resource/Year_of_birth_missing_%28living_people%29  | 4615.7939763369795  |
|7| http://dbpedia.org/resource/France  | 4595.730518177778  |
|8| http://dbpedia.org/resource/Germany  | 4111.195621667528  |
|9| http://dbpedia.org/resource/Canada  | 3765.46156061246 |
|10| http://dbpedia.org/resource/Animal  | 3692.395898434714  |

Ces valeurs exactes de pagerank correspondent au résultats issus de l'implémentation Pyspark. On a favorisé ces résulats parce que pour Python les données numériques float ont une [double précision par défaut](https://zetcode.com/python/decimal/#:~:text=By%20default%2C%20Python%20interprets%20any,for%20financial%20and%20monetary%20calculations.) tandis que pour Pig les types autres que le long et int peuvent entrainer des [pertes de précisions](https://www.oreilly.com/library/view/programming-pig/9781449317881/ch04.html). Plus de détails sur ce point sont abordés dans la section finale.

# 4. Conclusions et recommendations
Cet étude nous a permis d'appliquer les savoir-faire appris dans ce module afin de mettre en oeuvre et comparer les exécutions des implémentations Pig et PySpark de l'algorithme PageRank, dans le contexte du traitement des données massives sur l'environnement distribué GCP. Or, on résume ci-dessous les principales conclusions dérivées de cette expérience:

* L'implémentation pySpark avec le partitionnement controlé c'est celle qui a performé le mieux en moyen. Néanmoins, il faut souligner qu'au bout de 5 noeuds, Pig a ratrappé en temps d'exécution, ce dernier béneficiant le plus d'une augmentation dans le nombre de workeurs, tant que pyspark attend un soeil a 4 noeuds.

* Nous avons utilisé la fonction de [partitionnement qui vient par défaut avec pySpark](https://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.partitionBy) (avec le param None) et ça pourrait avoir impacté la performance de la version partitionnée de pySpark, alors qu'il pourrait exister une autre implémentation plus optimale.

* Il y avait des inconvenients par exemple Il y avait des différences notables de temps d'exécution avec le même scripte et les mêmes données ce qui peut être à cause des ressources partagées entre plusieurs clusters pour différents clients qui peuvent bien avoir un impact sur les temps d'exécution. Afin de minimiser cela, une recommendation serait d'exécuter la même experiment plusieurs fois et calculer le moyen de chaque configuration, malheureusement le crédit ne suffit pas pour faire ce genre d'expérimentations.

* Restrictions crédit, limitations par rapport au nombre de noeuds (1 planté, 6 été pas dispo, pas possible d'executer plusieur configuration de noeuds en paralelle due a la quota.

* Finalment, nous avons constaté une différence significative de rank des pages entre pyspark et Pig et nous pensons que c'est due à une différence de précision pour les multiplications et divisions qui rendent différent les résultats, afin de vérifier cela nous avons fait une expérimentation avec un petit volume de données et il y avait une différence mais il était bien plus petit qu'avec le grand fichier. Par example, avec un petit fichier on peut obtenir une différence de xxx, tandis que pour les gros dataset la différence déforme jusqu'a 33320.5089 pour le meilleur pagerank calculé avec Pig, contre calculé avec Pyspark http://dbpedia.org/resource/Living_people pour le site. Nous recommendons d'explorer les exécutions des pagerank en utilisant les types de données recommendées pour éviter une [perte de précision pour Pig](https://www.oreilly.com/library/view/programming-pig/9781449317881/ch04.html).

