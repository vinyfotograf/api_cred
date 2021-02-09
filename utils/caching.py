from app import cache 

def get_item_cache(consumer_id: int, requested_value: float, installments: int):
    return cache.get(f"{consumer_id}-{requested_value}-{installments}")

def set_item_cache(consumer_id: int, requested_value: float, installments: int, data: dict):
    cache.set(f"{consumer_id}-{requested_value}-{installments}", data)
