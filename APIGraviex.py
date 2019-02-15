#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import hmac
import requests
import time
import ssl
import json
import collections

class APIGraviex:
    def __init__(self, access_key, secret_key):
    
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        
        self.access = access_key
        self.secret = secret_key
        
        self.timer = int(time.time()) * 1000
        self.timer2 = int(time.time()) * 1000
        
    def api_query(self, type, feature_requested, get_parameters={}):
        
        timer = int(time.time()) * 1000
        # print(timer)
        if self.timer == timer:
            self.timer2 = self.timer2 + 1
        else:
            self.timer = timer
            self.timer2 = timer
        
        # print(self.timer2)
        get_parameters['tonce'] = str(self.timer2)
        get_parameters = collections.OrderedDict(sorted(get_parameters.items(), key=lambda t: t[0]))
        text = ''
        for key, value in get_parameters.items():
            if value != '':
                text = text + '&' + key + '=' + str(value)
                
        req = 'access_key=' + self.access + text
        message = type + '|/api/v3/' + feature_requested + '|' + req
        # print(message)
        
        signature = hmac.new(
            bytes(self.secret , 'latin-1'),
            bytes(message, 'latin-1'),
            hashlib.sha256 
        ).hexdigest()
       
        if type == 'GET':
            query = 'https://graviex.net/api/v3/' + feature_requested  \
                + '?' + (req) + '&signature=' + (signature) 
                               
            #print(query)
            r = requests.get(query)
            try:
                data = json.loads(r.content.decode('utf-8'))
                return data
            except:
                return r.content.decode('utf-8')
        else:
            query = 'https://graviex.net/api/v3/' + feature_requested  \
                 + '?' + (req)  + '&signature=' + (signature) 
            # print(query)
           
            r = requests.post(query)
            # print(r.url)
            data = json.loads(r.content.decode('utf-8'))
            return data    
    
    def api_query_public(self, feature_requested, get_parameters=None):
        query = 'https://graviex.net/api/v3/' + feature_requested + "/" + ('/'.join(i for i in get_parameters.values()
                           ) if get_parameters is not None else "") 
        # print(query)
        r = requests.get(query)
        data = json.loads(r.content.decode('utf-8'))
        return data

    def timestamp(self):
        return self.api_query_public('timestamp')
    
    def market(self):
        return self.api_query_public('markets')
        
    def tickers(self):
        return self.api_query_public('tickers')
        
    def ticker(self, market):
        return self.api_query_public('tickers', get_parameters={'market': market.lower()})
        
    def me(self):
        return self.api_query('GET', 'members/me') 
        
    def deposits(self, currency, limit = '', state = ''):   
        return self.api_query('GET', 'deposits', get_parameters={'currency':currency.lower(), 'limit':limit, 'state':state}) 
     
    def deposit(self, txid):   
        return self.api_query('GET', 'deposit', get_parameters={'txid':txid}) 
        
    def deposit_address(self, currency):   
        return self.api_query('GET', 'deposit_address', get_parameters={'currency':currency.lower()})      
        
    def get_order_market(self, market = '', limit = '', state = '', page = '', order_by = ''):   
        return self.api_query('GET', 'orders', get_parameters={'market':market.lower(), 'limit':limit, 'state':state, 'page':page, 'order_by':order_by})     
    
    def put_orders(self, market = '', side = '', volume = '', price = ''):   
        return self.api_query('POST', 'orders', get_parameters={'market':market.lower(), 'side':side, 'volume':volume, 'price':price})  

    def clear_orders(self, side = ""):
        return self.api_query('POST', 'orders/clear', get_parameters={'side':side}) 

    def get_order_id(self, id = ''):   
        return self.api_query('GET', 'order', get_parameters={'id':id})    
        
    def depth(self, market = '', limit = ''):   
        return self.api_query('GET', 'depth', get_parameters={'market':market.lower(), 'limit':limit}) 
        
        
        
        
