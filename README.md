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
Le but de cette expérience c'est de comparer les performances de l'algorithme [**pagerank**](https://fr.wikipedia.org/wiki/PageRank), entre une implémentation [Pig](https://en.wikipedia.org/wiki/Pig_Latin#:~:text=Pig%20Latin%20is%20a%20language,to%20create%20such%20a%20suffix.) et une implémentation [PySpark](https://spark.apache.org/docs/latest/api/python/). Cette expérience est inspiré d'une démonstration realisée lors de la conférence [NDSI 2012 présentation des Resilient Distributed Datasets (RDD)](https://www.youtube.com/watch?v=dXG4yC8ICEI).

Premièrement, nous présentons les [configurations utilisées](#11-configurations-utilisées) pour réaliser cette expérience, ensuite nous comparons les [temps d'exécution](#2-exécutions-pagerank---pig-vs-pyspark) du pagerank avec des [diagrammes à ligne brisée](#2-exécutions-pagerank---pig-vs-pyspark) et nous illustrons [les meilleurs pagerank](#3-meilleur-pagerank) computés. Finalement, nous présentons les [conclusions et récomendations](#4-conclusions-et-recommendations) issues des comparaisons et le déroulement de l'expérience.

## 1.1 Configurations utilisées
Afin de mesurer la performance entre les implémentations Pig et Pyspark, nous avons eu recours au service d'exécution de tâches [Dataproc](https://cloud.google.com/dataproc?hl=fr) de la suite Google cloud. Les configurations et considérations tenus en comptes pour réaliser cette expérience s'énumèrent ci-après:
* **Paramètres pagerank**: le nombre d'iterations a été fixé à **3**, et le facteur pagerank utilisé à {d = **0.85**}, pour les deux implémentations. 
* **Nombre de noeuds**: 2, 3, 4 et 5. Le nombre de noeuds a été déterminé en raison des restrictions du quota et la puissance minimale requise pour le fonctionnement des algorithmes.
* **Région du cluster**: fixé à **europe-west1**, définie en function de la proximité avec le bucket hébergeant les données d'entrée.
* **Données d'entrée**: le dataset [page_links_en.nt.bz2](http://downloads.dbpedia.org/3.5.1/en/page_links_en.nt.bz2), 
préchargé dans le bucket public **gs://public_lddm_data//page_links_en.nt.bz2**
* **Version PIG installée dans le cluster**: Apache Pig version 0.18.0-SNAPSHOT
* **Version PySpark installée dans le cluster**: Spark 3.1.3

Implémentations du pagerank utilisées:
* Implémentation Pig  
https://github.com/oahjimenez/x3ia020_pagerank/blob/main/pig/dataproc.py    
* Commandes d'exécution Pig  
https://github.com/oahjimenez/x3ia020_pagerank/blob/main/pig/run.sh  
* Implémentation PySpark  
https://github.com/oahjimenez/x3ia020_pagerank/blob/main/pyspark/pagerank.py  
* Commandes d'exécution PySpark  
https://github.com/oahjimenez/x3ia020_pagerank/blob/main/pyspark/run.sh  
* Code source original, auteur professeur Pascal MOLLI:
https://github.com/momo54/large_scale_data_management  

## 1.2 Modifications aux sources originales 
### Pig
* Rajout du calcul **DISTINCT** dans la méthode **INIT**, afin de supprimer des tuples url dupliquées et de rendre les résultats équivalents à ceux obtenus avec PySpark.
* Rajout du calcul des top pageranks, retenant les url voisines (**to_url**) qui sont autrement écartées dans la prochaine itération lors de l'application du **cogroup** inner.

### PySpark
* Applique un **partitionnement** aux [rdds](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html) **links** et **ranks**, visant la réduction des Shuffles entre les joins par itération. Nous avons utilisé la function de partition [portable_hash sur les clés et le calcul du nombre de partitions par défaut](https://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.partitionBy).

# 2. Exécutions pagerank - Pig vs PySpark
Les résultats issus des exécutions pageranks en utilisant les différentes configurations de cluster sont présentés ci-dessous. Pour l'implémentation PySpark, on distingue le temps d'exécution entre l'implémentation sans et avec partitionnement contrôlé.

## PIG
| Nombre de noeuds | Temps d'exécution  | Dataproc Job id
| ------------- | -------------| ------------- |
| 2 | 57 min 19 sec | 83edf25aa5e24364a1ea968a99ab415f |
| 3 | 47 min 50 sec | 85961f8339bc43bcbaf5cf69cd13719d |
| 4 | 38 min 8 sec | 6d80276d638d4d0096f0d2bbad55debc |
| 5 | 35 min 27 sec | 1ad6eaf435d24191878899943ae73a15 |

## PySpark Basic
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 43 min 30 sec | 895b7b281f794d4393278962e01169ad |
| 3 | 38 min 23 sec | 527ace71d1ce4f9da1b5f5ab5581c2dd |
| 4 | 35 min 28 sec | e870244c239b47e1bf2e6c86691d4bfa |
| 5 | 35 min 04 sec | 9d52c020836c41cba2c50e3da3de29e7 |

## PySpark avec partionnement contrôlé
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 42 min 48 sec | 71dd624351af42128d8d321c5fc314dd |
| 3 | 31 min 41 sec | f0c04b5b485b4504952c75b7e51b3e44 |
| 4 | 29 min 12 sec | 3f475ada46de4c7ab8e0ca526c1ed5a5 |
| 5 | 30 min 20 sec | 98c8047900634a33882b2296b8a8293a |

## PIG vs PySpark Basic vs PySpark avec partionnement

Ci-après suit un diagramme  à ligne brisée illustrant la comparaison des temps d'exécution entre les implémentations pagerank, pour chaque configuration de cluster utilisée
<br/>
<img align=center src= https://github.com/oahjimenez/x3ia020_pagerank/blob/main/comp_diag.png>
<br/>
Sur ce graphique nous pouvons constater les points suivants:
* Pig est l'implémentation la moins performante avec peu des noeuds, ce qui pourrait s'expliquer par les écritures des résultats intermediaries sur le disque avec des ressources limitées. 
* PySpark avec du partitionnement est l'implémentation qui performe le mieux en moyen, néanmoins cette implémentation atteint un seuil à 4 noeuds.
* Pig bénéficie le plus de l'augmentation du nombre de noeuds, ce qui devient plus évident dans le range de 4 à 5 noeuds. Nous pouvons apprécier que les implémentations sur PySpark atteignent un seuil dans leurs temps d'exécution dans cette range  de 4 à 5 noeuds, tandis que le temps d'exécution continue à diminuer pour Pig.
* L'implémentation sur Pig rattrape l'implémentation sur PySpark Basic pour la configuration à 5 noeuds
* Avec des ressources limitées (2 noeuds), Pyspark ne semble pas bénéficier d'une amélioration en raison du partionnement.

Les meilleurs pagerank trouvés dans le contexte de ces exécutions sont présentés dans la section suivante.
# 3. Meilleur pagerank
En réalisant cette expérience nous avons obtenu que l'entité avec le plus grand pagerank c'est l'uri <http://dbpedia.org/resource/Living_people>, avec un pagerank de **36,794.33**. On présente ci-après le top 10 d'url ayant les meilleur pagerank, issue de 3 itérations de l'algorithme pagerank.
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

Ces valeurs de pagerank correspondent aux résultats issus de l'implémentation Pyspark. Des résultats équivalents sont obtenus avec Pig, [à condition de rajouter la clause DISTINCT dans la méthode INIT et de calculer les pageranks sur le jeu de données **to_url** avant le dernier cogroup.](#12-modifications-aux-sources-originales)

# 4. Conclusions et recommendations
Cette étude nous a permis d'appliquer les savoir-faire appris dans ce module afin de mettre en oeuvre et comparer les implémentations Pig et PySpark de l'algorithme PageRank, dans le contexte du traitement des données massives sur l'environnement distribué GCP. On résume ci-dessous les principales conclusions dérivées de cette expérience:

1. PySpark avec du partitionnement contrôlé  est l'implémentation qui performe le mieux en moyen. Bien que l'on esperait que les opérations des RDD dans le RAM et les optimisations en matière de partage de ressources allaient dépasser significativement l'implémentation sur Pig, pour cette expérience nous avons obtenu qu'au but de 5 noeuds, Pig a rattrapé en temps d'exécution, ce qui pourrait indiquer que les avantages offerts par les RDD et le partionnement contrôlé n'ont pas été exploités au maximum pour cette expérience.

2. Quant à l'implementation PySpark avec du partitionnement controlé, nous avons utilisé le calcul du [nombre de partitions par défaut](https://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.partitionBy). Nous recommandons de mettre en oeuvre des configurations plus exactes pour mieux bénéficier des avantages du partionnement, par exemple une [sélection du nombre de partitions en function des nombres de coeurs](https://similaranswer.fr/combien-de-partitions-dois-je-avoir-pyspark/#comment-pyspark-determine-t-il-le-nombre-de-partitions) disponibles dans le cluster.

3. Pour une même configuration d'exécution, nous avons constaté des différences non négligables en termes du temps d'exécution. Nous attribuons ce comportement aux variations dans les disponibilités et état des santés des clusters. Afin de minimiser ce bruit dans l'analyse du temps d'exécution, nous recommandons, pour chaque configuration, d'exécuter les expériences à plusieurs reprises pour ensuite présenter les résultats moyens. Les résultats présentés pour cette expérience correspondent aux **modes** des paires d'expériences, en raison des limites sur les crédits GC.

4. Nous recommandons d'explorer les types de données recommandées autres que le float pour éviter une [perte de précision pour les calculs sur Pig](https://www.oreilly.com/library/view/programming-pig/9781449317881/ch04.html), au but de minimiser les différences entre les valeurs pagerank de chaque implémentation.

