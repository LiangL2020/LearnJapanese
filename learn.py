"""
Date: 2/11/2025 
Initial idea: create a panel that asks user to one write haragana/katakana and repeats 
Subtasks: 
- needs to write a ML model that learns haragana and katakana 
- create a panel that collects hand written data to train the model 
"""
import os
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
