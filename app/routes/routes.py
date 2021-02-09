from app import app
from utils import caching
from flask import request, json, jsonify


@app.route("/transaction", methods=['GET']) 
def transaction():
    return  validate_transaction()

def validate_transaction():
    data = json.loads(request.data)['transaction']
    id = data['id']
    consumer_id = data['consumer_id']
    income = data['income']
    score = data['score']
    requested_value = data['requested_value']
    installments = data['installments']
    income_final = income * 0.3 #I calculate to get 30% of the consumer's income
    installments_value = requested_value / installments
    last_transaction = caching.get_item_cache(consumer_id, requested_value, installments)

    
    #Checks if the number of installments is less than the minimum 
    if installments < 6: 
        violation = "minimum-installments"

    #Checks if the value of the parcel is less than 30% of the consumer's income
    elif installments_value > income_final: 
        violation = "compromised-income"

    #Checks whether the score is greater than the minimum allowed
    elif score < 200:
        violation = "low-score"

    elif last_transaction:
        violation = "doubled-transaction"
    else: 
        caching.set_item_cache(consumer_id, requested_value, installments, data)
        violation = "authorized-transaction" 
      
    return jsonify({"transaction": {"id": id, "violations": [violation]}})

    