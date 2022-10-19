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
* **Paramètres pagerank**: le nombre d'iterations a été fixé à 3, et le facteur pagerank utilisé de {d = 0.85}, pour les deux implémentations. 
* **Nombres de workers**: 2, 3, 4 et 5. Le nombre de noeuds a été déterminé en raison des restrictions du quota.
* **La région**: europe-west1, défini en function de la proximité avec le bucket hebergéant les données d'entrée
* **Dataset d'entrée**: dataset [page_links_en.nt.bz2](http://downloads.dbpedia.org/3.5.1/en/page_links_en.nt.bz2), disponibles sur le bucket publique gs://public_lddm_data//page_links_en.nt.bz2
* **Version PIG installé dans le cluster**: Apache Pig version 0.18.0-SNAPSHOT
* **Version PySpark installé dans le cluster**: Spark 3.1.3

Implémentations du pagerank utilisées:
* Implémentation Pig
https://github.com/oahjimenez/x3ia020_pagerank/blob/main/pig/dataproc.py  
* Implémentation PySpark
https://github.com/oahjimenez/x3ia020_pagerank/blob/main/pyspark/pagerank.py  
* Code source original, auteur Pascal MOLLI:
https://github.com/momo54/large_scale_data_management  

## 1.2 Modifications aux sources originales 
**Pig**:
* Rajout du calcul **DISTINCT** dans la méthode INIT, afin de supprimer des tuples url duplicats et de rendre les résultats équivalents à ceux obtenus avec PySpark.
* Rajout du calcul des top pageranks, retenant les url voisines qui sont autrement ignorées dans la prochaine itération lors de l'application du cogroup inner.

**PySpark**:
* Applique un **partitionnement** aux rdds links et ranks, visant la réduction des Shuffles entre les joins. Nous avons utilisé la function de partition[portable_hash sur les clés et le calcul du nombre de partitionnements par défaut] https://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.partitionBy

Les résultats de l'exécution avec les configurations citées sont presentés dans la section suivante.
# 2. Exécutions pagerank - Pig vs PySpark
Ci-dessous on présente les résultats issus des exécutions pageranks en utilisant les différentes configurations de cluster. Pour l'implementation PySpark, on distingue le temps d'exécution de l'implémentation sans et avec partitionnement contrôlé.

## PIG
| Nombre de noeuds | Temps d'exécution | Temps d'exécution avec Distinct  | Dataproc Job id
| ------------- | -------------| ------------- | ------------- |
| 2 | 49 min 52 sec | -| 83edf25aa5e24364a1ea968a99ab415f |
| 3 | 37 min 25 sec | -| 85961f8339bc43bcbaf5cf69cd13719d |
| 4 | 34 min 34 sec | -| 6d80276d638d4d0096f0d2bbad55debc |
| 5 | 29 min 45 sec | -| 1ad6eaf435d24191878899943ae73a15 |

## PySpark Basic
| Nombre de noeuds | Temps d'exécution | Dataproc Job id
| ------------- | ------------- | ------------- |
| 2 | 43 min 30 sec | 895b7b281f794d4393278962e01169ad |
| 3 | 38 min 23 sec | 527ace71d1ce4f9da1b5f5ab5581c2dd |
| 4 | 35 min 28 sec | e870244c239b47e1bf2e6c86691d4bfa |
| 5 | 35 min 04 sec | 9d52c020836c41cba2c50e3da3de29e7 |

## PySpark avec partionnement
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

Ces valeurs exactes de pagerank correspondent aux résultats issus de l'implémentation Pyspark. Des résultats équivalents sont obtenus avec Pig, [à condition de rajouter la clause DISTINCT dans la méthode INIT et de calculer les pageranks sur le jeu de données **to_url** avant le dernier cogroup.](#12-modifications-aux-sources-originales)

# 4. Conclusions et recommendations
Cette étude nous a permis d'appliquer les savoir-faire appris dans ce module afin de mettre en oeuvre et comparer les implémentations Pig et PySpark de l'algorithme PageRank, dans le contexte du traitement des données massives sur l'environnement distribué GCP. On résume ci-dessous les principales conclusions dérivées de cette expérience:

1. PySpark avec du partitionnement controlé est l'implémentation qui performe le mieux en moyen. Bien que l'on esperait que les opérations des RDD dans le RAM et les optimisations en matière de partage de ressources allaient dépasser significativement l'implémentation sur Pig, pour cette expérience nous avons obtenu qu'au bout de 5 noeuds, Pig a ratrappé en temps d'exécution, ce qui pourrait évidencier que les avantages offertes par les RDD et le partionnement controle n'ont pas été exploités au maximum pour cette experience. **A reecrire

2. Quant à l'implementation PySpark avec du partitionnement controlé, nous avons utilisé le calcul du [nombre de partitions par défaut](https://spark.apache.org/docs/latest/api/python/_modules/pyspark/rdd.html#RDD.partitionBy). Nous recommandons de mettre en oeuvre des configurations plus exactes pour mieux bénéficier des avantages du partionnement, par exemple une [sélection du nombre de partitions en function des nombres de coeurs](https://similaranswer.fr/combien-de-partitions-dois-je-avoir-pyspark/#comment-pyspark-determine-t-il-le-nombre-de-partitions) disponibles dans le cluster et l'utilisation de la [méthode repartition pour partionner les données en mémoire](https://similaranswer.fr/combien-de-partitions-dois-je-avoir-pyspark/#comment-pyspark-determine-t-il-le-nombre-de-partitions). 

3. Pour une même configuration d'exécution, nous avons constaté des différences notables en termes du temps d'exécution. Nous attribuons ce comportement aux variations dans les disponibilités et état des santés des clusters. Afin de minimiser ce bruit dans l'analyse du temps d'exécution, nous recommandons, pour chaque configuration, d'exécuter les expériences à plusieurs reprises pour ensuite présenter les résultats moyens. Les résultats présentés pour cette expérience correspondent aux **modes** des paires d'expériences, en raison des limites sur les crédits GC. **A reviser

4. Finalement, nous avons constaté une différence notable des valeurs pagerank entre les implémentations Pyspark et Pig. Nous attribuons cette différence due aux pertes de précisions lors des calculs numériques. Par exemple, en expérimentant avec un volume modeste de données, la différence est négligeable e.g. 3.57179(PySpark) contre 3.57073(Pig), tandis que pour le plus grand dataset utilisé, la différence déforme jusqu'à 33320.50 (Pig), contre 36794.33 (Pyspark), pour le site http://dbpedia.org/resource/Living_people. Nous recommandons d'explorer les exécutions des pagerank en utilisant les types de données recommandées pour éviter une [perte de précision pour Pig](https://www.oreilly.com/library/view/programming-pig/9781449317881/ch04.html).

