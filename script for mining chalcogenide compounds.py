# -*- coding: utf-8 -*-
"""
@author: jr1n16
"""

import pandas as pd
from matminer.data_retrieval.retrieve_MP import MPDataRetrieval

api_key = 'WRITE API KEY'
mpdr = MPDataRetrieval(api_key)

df = pd.DataFrame() 

#Mine chalcogenide compounds from MP database
elements_of_interest = ["S, Te, Se"]
for elements in elements_of_interest:   
    df = df.append(mpdr.get_dataframe(
                            criteria={"nelements": {'$in': [2,3,4]}, 
                                      "band_gap": {'$gt': 0.16, '$lt': 4},
                                      "e_above_hull": 0,
                                      "nsites": {'$lt': 7}
                                      }, 
    
                            properties=["pretty_formula",
                                        "nelements",
                                        "density",
                                        "band_gap.search_gap.is_direct",
                                        "band_gap",
                                        "volume",
                                        "reduced_cell_formula",
                                        'spacegroup.number'
                                       ]
                           ,))
    

df.to_excel("dataset.xlsx")