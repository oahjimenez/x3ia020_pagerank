# x3ia020_pagerank
PageRank - Pig vs PySpark comparison https://madoc.univ-nantes.fr/mod/assign/view.php?id=1511791

# Description Expérience
* Objetif: comparer les performance d'execution de l'algorithme pagerank, entre une implantation Pig et une implantation PySpark, 
inspire de l'experience fait lors de la conference NDSI 2012. 
* Afin de messurer la performance d'execution entre ces deux implementation, nous avons eu recours a la suite Google cloud.
* On a utilisé des clusters avec plusieurs configuration, notamment en variant le nombre de workers. Nous avons utilisé 2,3,4 (5?) nombre de workers, visant a comparer l'evolution de temp d'executions entre les deux implementations.
* On presente la comparaison avec des diagrammes, et ensuite produit des conclusions basées sur ces comparaison et le deroulement de l'experience

Version PIG utilisé:
Version pyspark utilisé: 

# Comparaisons d'exécutions
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


# Conclusions
note: faire remarque pour les possibilités de changement de temps d'exécution
