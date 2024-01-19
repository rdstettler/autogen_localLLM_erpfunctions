import requests
import sys
import random
import autogen

def get_current_orderdata_for_workcenter(workcenter_id):
    """
    Calls the ERP api and requests the the current order data for a ERP workcenter. 

    Args:
        query (str): The ERP workcenter id.

    Returns:
        dict: array of dicts with current order data

    Example:
        >>> results = get_current_orderdata_for_workcenter("10110101")
    """
    # For testing purposes a randomizer
    return {
    "machineId": "M1002976",
    "localName": get_description_of_workcenter('blub'),
    "workcenter": "511V0B01",
    "location": "Factory A1",
    "doesSendToERP": False,
    "hasCounterData": False,
    "material": str(random.randint(3006606000, 4000606000)) + "A",
    "order": "1234567",
    "confirmation": "1827398172"
    }

def get_description_of_workcenter(workcenter_id):
    """
    Calls the ERP api and requests the description of a ERP Workcenter Id. This is a helper function.

    Args:
        query (str): The ERP workcenter id.

    Returns:
        string: The description of the ERP workcenter id

    Example:
        >>> results = get_description_of_ERP_workcenter("10110101")
        >>> print(results) # prints e.g. "Kugelstrahlanlage 10"
    """
    return random.choice(["Stanzanlage 3.12", "Montage M1233", "Verpackungsanlage 441", "Montagelinie A55"])
   