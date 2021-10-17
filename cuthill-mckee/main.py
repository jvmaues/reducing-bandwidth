import logging
import datetime
from os import error
import csv
import datetime
from numpy import arange
import readInstances as ri
import cuthillAlgo
import cuthilllib

import read_filenames as rf


#ALgoritmos testados


mypath = "/home/joao/Documents/CEFET/IC/Bandwidth-reduction/Codes/oficial/data"

list_path = rf.readFilesInDict(mypath, '.mtx')

with open('./resultados.csv', mode='w+') as csv_file:

        fieldnames = ['instance', 
                      'CM lib',
                      'RCM lib', 
                      'CM', 
                      'RCM', 
                      'CM Random node',
                      'RCM Random node', 
                      'CM max degree node', 
                      'RCM max degree node'
                       ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for instance_path in list_path:


                instance_name = instance_path.replace(mypath, "").replace("/", "").replace(".mtx", "")

                nnodes, nedges, edges, neighbours, lista_adj = ri.load_instance(instance_path)

                ## cuthill mckee lib networkx
                try:
                        w1 = cuthilllib.cuthill(edges)
                except:
                        w1 = "error"
                ## reverse cuthill mckee lib networkx
                try:
                        w2 = cuthilllib.reverse_cuthill(edges)
                except:
                        w2 = "error"
                ## cuthill mckee own algorithm
                try:
                        r, l, w3 = cuthillAlgo.CuthillMckee(neighbours)
                except:         
                        w3 = "erro"
                ## reverse cuthill mckee own algorithm
                try:
                        r, l, w4 = cuthillAlgo.ReverseCuthillMckee(neighbours)
                except: 
                        w4 = "erro"

                ## cuthill mckee own algorithm random best init
                try:
                        random_width = []
                        for i in range(nnodes):
                                r, l, w = cuthillAlgo.CuthillMckeeRandom(neighbours)
                                random_width.append(w)
                        w5 = min(random_width)
                except:         
                        w5 = "erro"
                ## reverse cuthill mckee own algorithm random best init
                try:
                        random_width = []
                        for i in range(nnodes):
                                r, l, w = cuthillAlgo.ReverseCuthillMckeeRandom(neighbours)
                                random_width.append(w)
                        w6 = min(random_width)
                        
                except: 
                        w6 = "erro"
                ## cuthill mckee own algorithm max degree init
                try:
                        r, l, w7 = cuthillAlgo.CuthillMckeeMaxDegree(neighbours)
                except:         
                        w7 = "erro"
                ## reverse cuthill mckee own algorithm max degree init
                try:
                        r, l, w8 = cuthillAlgo.ReverseCuthillMckeeMaxDegree(neighbours)
                except: 
                        w8 = "erro"
        
                
                
                writer.writerow({'instance': instance_name,
                                'CM lib': w1, 
                                'RCM lib': w2, 
                                'CM': w3, 
                                'RCM': w4,
                                'CM Random node': w5,
                                'RCM Random node': w6,
                                'CM max degree node': w7,
                                'RCM max degree node': w8
                                })