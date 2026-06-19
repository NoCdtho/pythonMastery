blockchain = [{'data': 'genesis block', 'prev_hash': '0'}]
blockchain.append({data: 'Block1', 
                   'prev_hash': hashlib.sha256(str(blockchain[-1]).encode()).hexdigest()})
