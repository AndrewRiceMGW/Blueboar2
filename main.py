# -*- coding: utf-8 -*-
"""
Created on Fri May 11 12:20:37 2018

@author: andre
"""
import sys
import argparse
import joblib
import os
import pickle

def main():
    pass
     

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Detect malicious files')
    parser.add_argument('FILE', help= 'File to be tested')
    args =parser.parse_args()
    
    #load classifier
    clf = joblib.load(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'classifier/classifier.pkl'
    ))
    features = pickle.loads(open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'classifier/features.pkl'),
            'r').read()
    )
    data = extract_infos(args.FILE)
    
    pe_features = map(lambda x:data[x], features)
    
    res= clf.predict([pe_features])[0]
    print('The file %s is %s' % (
            os.path.basename(sys.arg[1]),
            ['malicious', 'legitimate'][res])
    )
    
