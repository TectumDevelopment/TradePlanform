from .models import Commodity ,Asset
def validateCommodity(commodity_name):
    try:
        commodity = Commodity.objects.get(name = commodity_name)
        return commodity
    except:
        return None
