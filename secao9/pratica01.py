"""
Pratica 1 usando filter:
    Neste exemplo eu filtrei a lista de dicionarios contida em data
"""

fear_and_greed = {
    "name": "Fear and Greed Index",
    "data": [
        {
            "value": "71",
            "value_classification": "Greed",
            "timestamp": "06-17-2024",
            "time_until_update": "-1718574577"
        },
        {
            "value": "71",
            "value_classification": "Greed",
            "timestamp": "06-16-2024"
        },
        {
            "value": "74",
            "value_classification": "Greed",
            "timestamp": "06-15-2024"
        },
        {
            "value": "74",
            "value_classification": "Greed",
            "timestamp": "06-14-2024"
        },
        {
            "value": "70",
            "value_classification": "Greed",
            "timestamp": "06-13-2024"
        },
        {
            "value": "72",
            "value_classification": "Greed",
            "timestamp": "06-12-2024"
        },
        {
            "value": "74",
            "value_classification": "Greed",
            "timestamp": "06-11-2024"
        },
        {
            "value": "72",
            "value_classification": "Greed",
            "timestamp": "06-10-2024"
        },
        {
            "value": "75",
            "value_classification": "Greed",
            "timestamp": "06-09-2024"
        },
        {
            "value": "72",
            "value_classification": "Greed",
            "timestamp": "06-08-2024"
        }
    ],
    "metadata": {
        "error": None
    }
}

filtro = int(input('Digite o filtro de valor:'))

res = filter(lambda dado: int(dado['value']) > filtro, fear_and_greed['data'])
print(list(res))
