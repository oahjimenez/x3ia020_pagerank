# X3IA020 ALMA - Expérience PageRank Performance
### Faculté des Sciences et des Techniques - Nantes Université  
Gestion des données distribuées à large échelle  
**Professeur**: MOLLI Pascal  
**Étudiants**: RAGAA Mohammed ali ahmed, JIMENEZ Oswaldo  
PageRank - Pig vs PySpark comparison. Consigne: https://madoc.univ-nantes.fr/mod/assign/view.php?id=1523335 

[1. Introduction - Description de l'expérience](#1-introduction---description-de-lexpérience)  
[2. Exécutions pagerank - Pig vs PySpark](#2-exécutions-pagerank---pig-vs-pyspark)  
[3. Meilleur pagerank](#3-meilleur-pagerank)  
[4. Conclusions et recommendations](#4-conclusions-et-recommendations)

# 1. Introduction - Description de l'expérience
Le but de cette expérience c'est de comparer les performances de l'algorithme [pagerank](https://fr.wikipedia.org/wiki/PageRank), entre une implantation [Pig](https://en.wikipedia.org/wiki/Pig_Latin#:~:text=Pig%20Latin%20is%20a%20language,to%20create%20such%20a%20suffix.) et une implantation [PySpark](https://spark.apache.org/docs/latest/api/python/). Cette expérience est inspiré d'une expérience realisée lors de la conférence [NDSI 2012 présentation des Resilient Distributed Datasets (RDD)](https://www.youtube.com/watch?v=dXG4yC8ICEI).

On compare les temps d'exécutions du pagerank avec des diagrammes dans la [section 2]((#2-exécutions-pagerank---pig-vs-pyspark)  ), ensuite les meilleurs pagerank trouvés sont illustrés dans la [section 3]((#3-meilleur-pagerank) ). Des conclusions basées sur ces comparaison et le deroulement de l'experience sont abordés dans la [section 4](#4-conclusions-et-recommendations).

Ci-apres on enumére les configurations et considérations tenus en compte lors des exécutions Pig et PySpark.

## 1.1 Configurations utilisées
* Afin de messurer la performance d'execution entre ces deux implementation, nous avons eu recours au service d'exécution de taches [Dataproc](https://cloud.google.com/dataproc?hl=fr) de la suite Google cloud.
* On a utilisé des clusters avec plusieurs configuration, notamment en variant le nombre de workers. Nous avons utilisé 2,3,4 (5?) nombre de workers, visant a comparer l'evolution de temp d'executions entre les deux implementations.
* les clusters on ete crée en utilisant la meme région que les donnes pour beneficier des locations plus proches (réduire le temps de transfer réseau)
* Configuration pagerank utilisé: 3 itérations, avec des facteurs 0.15 + 0.85* sum (Brief description algo)


Version PIG utilisé: Apache Pig version 0.18.0-SNAPSHOT
liens ver implementation PIG (avec des credit et reference au code Pascal)
Version pyspark utilisé: 
liens ver implementation Pyspark (avec des credit et reference au code Pascal)
liens ver implementation Pyspark partition (avec des credit et reference au code Pascal)


# 2. Exécutions pagerank - Pig vs PySpark
* On presente le temps d'execution pris par les deux implementations, en function de nombre de worker utilisés. Pour l'implementation pyspark, on sépare le temps d'execution sans et avec partition.

## PIG
Configuration 1: 
Noeuds: 2
Itérations: 3

Exécution 1 (Exécuté par: Mohammed)
Temps d’exécution: 
Job id: 83edf25aa5e24364a1ea968a99ab415f 
Cluster id:  cluster-a35a 
Start time:  14 Oct 2022, 17:06:45
Elapsed time:  49 min 52 sec

Configuration 2: 
Noeuds: 3
Itérations: 3

Exécution a) (Exécuté par: Mohammed)
Temps d’exécution: 
Job id: 85961f8339bc43bcbaf5cf69cd13719d
Cluster id: cluster-a35a
Start time: 14 Oct 2022, 19:45:41  
Elapsed time:  37 min 25 sec


Configuration 3: 
Noeuds: 4
Itérations: 3

Exécution a) (Exécuté par: Mohammed)
Temps d’exécution: 
Job id: 6d80276d638d4d0096f0d2bbad55debc
Cluster id:  cluster-a35a
Start time:  14 Oct 2022, 18:59:22
Elapsed time:  34 min 34 sec



## PYSPARK BASIC
Configuration 1: 
Noeuds: 2
Itérations: 3


Exécution a) (Exécuté par: OSWALDO)
Temps d’exécution: 
Job id: 895b7b281f794d4393278962e01169ad
Cluster id: cluster-a35a
Start time: Oct 14, 2022, 10:15:21 AM
Elapsed time: 43 min 30 sec


Configuration 2: 
Noeuds: 3
Itérations: 3

Exécution a) (Exécuté par: - Amine )
Job id: 527ace71d1ce4f9da1b5f5ab5581c2dd 
Cluster id: cluster-a35a 
Start time: 14 oct. 2022, 18:52:25
Elapsed time: 38 min 23 s 



Configuration 3: 
Noeuds: 4
Itérations: 3


Exécution a) (Exécuté par: OSWALDO)
Temps d’exécution: 
Id cluster: e870244c239b47e1bf2e6c86691d4bfa
Cluster name: cluster-a35a
Start time: Oct 14, 2022, 11:30:05 AM
Elapsed time: 35 min 28 sec



## PYSPARK PARTITION
Afin d'éviter les shuffles entre join, une mise en place des partition controlé a eté rajouté au script pyspark. Le nombre de partition a eté laissé par défaut (Rajouter implementation pyspark), et pour la function de partitionnement un lambda utilisant les meme partition d'url a ete mis en place.

Configuration 1: 
Noeuds: 2
Itérations: 3

Exécution 1 (Exécuté par: - Mohammed )
Temps d’exécution: 
Job id: 895b7b281f794d4393278962e01169ad
Cluster id: cluster-a35a
Start time: Oct 14, 2022, 10:15:21 AM
Elapsed time: 43 min 30 sec



Configuration 2: 
Noeuds: 3
Itérations: 3
Exécution 1 (Exécuté par: - Mohammed )
Temps d’exécution: 
Job id: 895b7b281f794d4393278962e01169ad
Cluster id: cluster-a35a
Start time: Oct 14, 2022, 10:15:21 AM
Elapsed time: 43 min 30 sec



Exécution 1 (Exécuté par: Mohammed)
Temps d’exécution:

Configuration 3: 
Noeuds: 4
Itérations: 3

Temps d’exécution: 
Job id: 895b7b281f794d4393278962e01169ad
Cluster id: cluster-a35a
Start time: Oct 14, 2022, 10:15:21 AM
Elapsed time: 43 min 30 sec

Exécution 1 (Personne qui exécute: - )
Temps d’exécution:

* Descriptions de ce qu'on peut voir dans les diagrammes, points a souligner. 
* On appercoit une modeste amelioration par rapport a l'implementation basic pyspark, ce qui suggere qu'une meilleure configuration peut encore etre mis en place pour beneficier du partitionnement controler, ce point et abordé plus en détaille dans la section de conclusions et recommendations.

# 3. Meilleur pagerank
Avec cette expérience nous avons obtenu que l'entité avec le plus grand pagerank c'est l'uri <http://dbpedia.org/resource/Living_people>, avec un pagerank de 36,794.33. On présente ci-après le top 10 d'url ayant les meilleur pagerank, issue de 3 itérations de l'algorithme pagerank.
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

Répondre a la question: résultats calculés avec Pig ou pyspark? résultats similaires ou différents?

# 4. Conclusions et recommendations
note: faire remarque pour les possibilités de changement de temps d'exécution
* Recommendation pour améliorer pyspark -> raffiner la sélection de nombre de partitionneurs pour exploiter au maximum les vertus du partitionBy
* Recommendation exécuter plusieurs fois pour calculer un temps d'exécution moyen.
* Prendre en compre l'utilisation des ressources Google et comment ceux peuvent impacter sur les temps d'exécution

* Défis rencontrés:
* Restrictions crédit, limitations par rapport au nombre de noeuds (1 planté, 6 été pas dispo, pas possible d'executer plusieur configuration de noeuds en paralelle due a la quota, discrepence pagerank pig vs pyspark du au perte de précision
