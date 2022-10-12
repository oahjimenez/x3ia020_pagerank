
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
This is an example implementation of PageRank. For more conventional use,
Please refer to PageRank implementation provided by graphx

Example Usage:
bin/spark-submit examples/src/main/python/pagerank.py data/mllib/pagerank_data.txt 10
"""
import matplotlib #pip3 install matplotlib
import numpy as np
from matplotlib import pyplot

# create dataset
execution_times = [171,72,23]
programs = ('Pig', 'Basic Spark', 'Spark + Controlled Partitioning')
x_pos = np.arange(len(programs))

# Create bars and choose color
pyplot.bar(x_pos, execution_times, color = ('blue', 'red', 'green'))

# Add title and axis names
pyplot.title('PageRank Performance')
pyplot.xlabel('Program')
pyplot.ylabel('Time per iteration (s)')

n_bins = 200
x = [[171],[72],[23]]
print(x)
print(n_bins)

# Create names on the x axis
pyplot.xticks(x_pos, programs)
 
# Show graph
pyplot.show()
