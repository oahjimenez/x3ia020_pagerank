#!/usr/bin/python
from org.apache.pig.scripting import *
import json
import time
from subprocess import call


def ranking(k):
	INIT = Pig.compile("""
	A = LOAD 'gs://mydatatesting/small_page_links.nt' using PigStorage(' ') as (url:chararray, p:chararray, link:chararray);
	B = GROUP A by url;                                                                                  
	C = foreach B generate group as url, 1 as pagerank, A.link as links;                                 
	STORE C into '$docs_in';
	""")

	UPDATE = Pig.compile("""
	-- PR(A) = (1-d) + d (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))
	previous_pagerank = 
	    LOAD '$docs_in' 
	    USING PigStorage('\t') 
	    AS ( url: chararray, pagerank: float, links:{ link: ( url: chararray ) } );
	outbound_pagerank =  
	    FOREACH previous_pagerank 
	    GENERATE 
		pagerank / COUNT ( links ) AS pagerank, 
		FLATTEN ( links ) AS to_url;
	new_pagerank = 
	    FOREACH 
		( COGROUP outbound_pagerank BY to_url, previous_pagerank BY url INNER )
	    GENERATE 
		group AS url, 
		( 1 - $d ) + $d * SUM ( outbound_pagerank.pagerank ) AS pagerank, 
		FLATTEN ( previous_pagerank.links ) AS links;
		
	STORE new_pagerank 
	    INTO '$docs_out' 
	    USING PigStorage('\t');
	""")

	params = { 'd': '0.5', 'docs_in': 'gs://mydatatesting/out_{}/pagerank_data_simple'.format(k) }

	stats = INIT.bind(params).runSingle()
	if not stats.isSuccessful():
	      raise 'failed initialization'

	for i in range(2):
	   out = "gs://mydatatesting/out_{}/pagerank_data_".format(k) + str(i + 1)
	   params["docs_out"] = out
	   Pig.fs("rmr " + out)
	   stats = UPDATE.bind(params).runSingle()
	   if not stats.isSuccessful():
	      raise 'failed'
	   params["docs_in"] = out
	
if __name__ == '__main__':
	data ={}
	for i in range(3,4):
		t1 = time.time()
		ranking(i)
		t2 = time.time()
		data[i]= t2-t1
		call(["gcloud" ,"dataproc",'clusters' ,'update', 'cluster-a35a', '--region=europe-west1','--num-workers='+str(i)])
	
	with open('json_data.json', 'w') as outfile:
		outfile.write(json.dumps(data))
	
	call(["gsutil" ,"cp",'json_data.json' ,'gs://mydatatesting/'])
	
	
	call(["gcloud" ,"dataproc",'clusters' ,'delete', 'cluster-a35a', '--region=europe-west1'])
	
	
	
    
