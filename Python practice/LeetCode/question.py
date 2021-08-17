# Enter your code here. Read input from STDIN. Print output to STDOUT

# 100 USD to EUR
# Can exchange to other currencies

# No transaction fees

# Non zeroes, non negatives
# No positive loops
# return the maximum value? keep in mind for the exchange path
# don't use int for conversion
# BTC -> USD 990
# USD -> BTC / 1000
# Always be a path between start and end

import requests
from collections import deque


tickers = {
    "BTC-USD": {"ask": 1000, "bid": 990},
    "BTC-EUR": {"ask": 1200, "bid": 1150},
    "ETH-USD": {"ask": 200, "bid": 180},
    "ETH-EUR": {"ask": 220, "bid": 210},
    "BTC-ETH": {"ask": 5.6, "bid": 5.5}
}

products = requests.get("https://api.pro.coinbase.com/products").json()


def buildTicker(url):
    tickers = {}

    products = requests.get(url).json()
    for product in products:
        id = product["id"]
        productTicker = requests.get(
            "https://api.pro.coinbase.com/products/" + id + "/ticker").json()
        tickers[id] = {
            "ask": productTicker["ask"],
            "bid": productTicker["bid"]
        }
    return tickers


# tickers = buildTicker("https://api.pro.coinbase.com/products")

tickers = {'GRT-GBP': {'ask': '0.5782', 'bid': '0.5777'}, 'BTC-EUR': {'ask': '37681.27', 'bid': '37670.01'}, 'XLM-USD': {'ask': '0.321373', 'bid': '0.321261'}, 'GNT-USDC': {'ask': '0.397934', 'bid': '0.397089'}, 'MASK-USDT': {'ask': '6.28', 'bid': '6.27'}, 'ALGO-USD': {'ask': '0.8726', 'bid': '0.8722'}, 'BTC-GBP': {'ask': '31947.98', 'bid': '31943.31'}, 'LOOM-USDC': {'ask': '0.090625', 'bid': '0.090038'}, 'IOTX-BTC': {'ask': '0.0000028', 'bid': '0.0000027'}, 'MASK-GBP': {'ask': '4.55', 'bid': '4.53'}, 'CGLD-EUR': {'ask': '2.5029', 'bid': '2.4986'}, 'TRU-USD': {'ask': '0', 'bid': '0'}, 'LRC-BTC': {'ask': '0.00000638', 'bid': '0.00000636'}, 'BAT-ETH': {'ask': '0.00023186', 'bid': '0.00023153'}, 'XTZ-USD': {'ask': '3.2887', 'bid': '3.2862'}, 'AAVE-USD': {'ask': '382.77', 'bid': '382.439'}, 'ICP-EUR': {'ask': '53.488', 'bid': '53.434'}, 'STORJ-USD': {'ask': '1.134', 'bid': '1.1333'}, 'QUICK-USD':
           {'ask': '583.02', 'bid': '582.52'}, 'BAND-BTC': {'ask': '0.00017325', 'bid': '0.00017292'}, 'ETC-USD': {'ask': '59.082', 'bid': '59.048'}, 'MANA-USD': {'ask': '0.777', 'bid': '0.776'}, 'LINK-GBP': {'ask': '17.72787', 'bid':
                                                                                                                                                                                                                 '17.7085'}, 'CHZ-GBP': {'ask': '0.2413', 'bid': '0.2409'}, 'ORN-USDT': {'ask': '8.71', 'bid': '8.67'}, 'MIR-GBP': {'ask': '2.456', 'bid': '2.45'}, 'USDT-USD': {'ask': '1.0004', 'bid': '1.0003'}, 'MASK-EUR': {'ask': '5.36', 'bid': '5.34'}, 'BNT-USD': {'ask': '3.9129', 'bid': '3.9086'}, 'ENJ-BTC': {'ask': '0.0000344', 'bid': '0.0000343'}, 'NU-EUR': {'ask': '0.2241', 'bid': '0.2237'}, 'UNI-BTC': {'ask': '0.0006191', 'bid': '0.00061869'}, 'FARM-USD': {'ask': '283.16', 'bid': '282.2'}, 'DOGE-BTC': {'ask': '0.0000059', 'bid': '0.0000058'}, 'NU-BTC': {'ask': '0.00000595', 'bid': '0.00000593'}, 'ICP-USDT': {'ask': '62.767', 'bid': '62.715'}, 'REN-BTC': {'ask': '0.00001063', 'bid': '0.0000106'}, 'MANA-ETH': {'ask': '0.000257', 'bid': '0.000256'}, 'ETH-EUR': {'ask': '2579.3', 'bid': '2578.77'}, 'ZEC-USDC': {'ask': '132.65', 'bid': '132.5'}, 'ADA-EUR': {'ask': '1.4618', 'bid': '1.4607'}, 'POLY-USDT': {'ask': '0.2845', 'bid': '0.2837'}, 'BCH-BTC': {'ask': '0.01363', 'bid': '0.01361'}, 'CGLD-USD': {'ask': '2.9374', 'bid': '2.9348'}, 'DOT-USDT': {'ask': '20.396', 'bid': '20.374'}, 'DOGE-EUR': {'ask': '0.2216', 'bid': '0.2214'}, 'AXS-EUR': {'ask': '0', 'bid': '0'}, 'BTC-USDC': {'ask': '44212.46', 'bid': '44202.2'}, 'UMA-BTC': {'ask': '0.00023957', 'bid': '0.00023904'}, 'SKL-GBP': {'ask': '0.2089', 'bid': '0.2086'}, 'BAT-USDC': {'ask': '0.701753', 'bid': '0.70083'}, 'BAT-EUR': {'ask': '0.598', 'bid': '0.596'}, 'LTC-GBP': {'ask': '118.33', 'bid': '118.26'}, 'CRV-EUR': {'ask': '1.6702', 'bid': '1.668'}, 'EOS-EUR': {'ask': '3.937', 'bid': '3.933'}, 'LINK-ETH':
           {'ask': '0.00810556', 'bid': '0.0080986'}, 'CGLD-GBP': {'ask': '2.1238', 'bid': '2.1178'}, 'ADA-GBP': {'ask': '1.2391', 'bid': '1.2382'}, 'BCH-EUR': {'ask': '513.18', 'bid': '512.66'}, 'REN-USD': {'ask': '0.4695', 'bid': '0.4692'}, 'ALGO-BTC': {'ask': '0.00001976', 'bid': '0.00001974'}, 'OGN-USD': {'ask': '0.888', 'bid': '0.886'}, 'BAL-USD': {'ask': '24.57802', 'bid': '24.55484'}, 'DOGE-GBP': {'ask': '0.1879', 'bid': '0.1876'}, 'CLV-USD': {'ask': '1.66', 'bid': '1.65'}, 'RLY-GBP': {'ask': '0.3685', 'bid': '0.3675'}, 'BOND-USD': {'ask': '25.44', 'bid': '25.38'}, 'UST-USD': {'ask': '1.003', 'bid': '1.002'}, 'CRV-BTC': {'ask': '0.0000444', 'bid': '0.0000442'}, 'ORN-USD': {'ask': '8.7', 'bid': '8.67'}, '1INCH-USD': {'ask': '2.749', 'bid': '2.746'}, 'WLUNA-USD': {'ask': '0', 'bid': '0'}, 'MIR-BTC': {'ask': '0.0000769', 'bid': '0.0000767'}, 'IOTX-USD': {'ask': '0.12258', 'bid': '0.12188'}, 'WLUNA-USDT': {'ask': '0', 'bid': '0'}, 'UMA-USD': {'ask': '10.574', 'bid': '10.57'}, 'YFI-BTC': {'ask': '0.82012', 'bid': '0.81972'}, 'AXS-USDT': {'ask': '0', 'bid': '0'}, 'ICP-BTC': {'ask': '0.0014195', 'bid': '0.0014181'}, 'ZEC-USD': {'ask': '132.6', 'bid': '132.49'}, 'ICP-GBP': {'ask': '45.346', 'bid': '45.25'}, 'BCH-GBP': {'ask': '435.16', 'bid': '434.65'}, 'SUSHI-EUR': {'ask': '9.122', 'bid': '9.109'}, 'ACH-USD': {'ask': '0.089923', 'bid': '0.089644'}, 'YFI-USD': {'ask': '36240.05', 'bid': '36216.92'}, 'ETC-GBP': {'ask': '42.613', 'bid': '42.547'}, 'KEEP-USD': {'ask': '0.33', 'bid': '0.3297'}, '1INCH-BTC': {'ask': '0.0000622', 'bid': '0.0000621'}, 'REP-USD': {'ask': '27.11', 'bid': '27.08'}, 'SOL-USDT': {'ask': '39.965', 'bid': '39.908'}, 'ANKR-GBP': {'ask': '0.06781', 'bid': '0.06769'}, 'CTSI-USD': {'ask': '0.6872', 'bid': '0.6863'}, 'AXS-USD': {'ask': '0', 'bid': '0'}, 'CGLD-BTC': {'ask': '0.0000664', 'bid': '0.00006631'}, 'PAX-USD': {'ask': '1.01', 'bid': '1'}, 'SOL-BTC': {'ask': '0.0009044', 'bid': '0.0009032'}, 'AXS-BTC': {'ask': '0', 'bid': '0'}, 'NMR-USD': {'ask': '39.3847', 'bid': '39.3306'}, 'RLY-EUR': {'ask': '0.4346', 'bid': '0.4337'}, 'FORTH-USD': {'ask': '16.446', 'bid': '16.409'}, 'NU-USD': {'ask': '0.2632', 'bid': '0.2631'}, 'RAI-USD': {'ask': '3.0038', 'bid': '2.9916'}, 'USDC-EUR': {'ask': '0.853', 'bid': '0.852'}, 'FIL-GBP': {'ask': '48.7699', 'bid': '48.713'}, 'BTC-UST': {'ask': '44203.99', 'bid': '44067'}, 'AMP-USD': {'ask': '0.06076', 'bid': '0.06072'}, 'BAT-USD': {'ask': '0.702', 'bid': '0.7'}, 'CRV-GBP': {'ask': '1.4158', 'bid': '1.4137'}, 'REQ-USD': {'ask': '0', 'bid': '0'}, 'SUSHI-USD': {'ask': '10.697', 'bid': '10.693'}, 'ZRX-BTC': {'ask': '0.00002097', 'bid': '0.00002094'}, 'PAX-USDT': {'ask': '1', 'bid': '0.99'}, 'MATIC-EUR': {'ask': '1.0996', 'bid': '1.0986'}, 'NMR-EUR': {'ask': '33.6024', 'bid': '33.5174'}, 'DNT-USDC': {'ask': '0.169978', 'bid': '0.169696'}, '1INCH-GBP': {'ask': '1.986', 'bid': '1.982'}, 'SNX-USD': {'ask': '10.1583', 'bid': '10.155'}, 'LPT-USD': {'ask': '17.84', 'bid': '17.8'}, 'DOT-EUR': {'ask': '17.369', 'bid': '17.348'}, 'REQ-USDT': {'ask': '0', 'bid': '0'}, 'KNC-BTC': {'ask': '0.00003874', 'bid': '0.00003867'}, 'BNT-EUR': {'ask': '3.3334', 'bid': '3.3275'}, 'ANKR-EUR': {'ask': '0.07994', 'bid': '0.07983'}, 'SNX-BTC': {'ask': '0.00022981', 'bid': '0.00022966'}, 'USDC-GBP': {'ask': '0.723', 'bid': '0.722'}, 'ALGO-GBP': {'ask': '0.6312', 'bid': '0.6304'}, 'IOTX-EUR':
           {'ask': '0.10378', 'bid': '0.10328'}, 'MKR-BTC': {'ask': '0.07251', 'bid': '0.07239'}, 'OMG-BTC': {'ask': '0.00011154', 'bid': '0.00011139'}, 'OMG-EUR': {'ask': '4.2009', 'bid': '4.195'}, 'ETH-DAI': {'ask': '3024.44', 'bid': '3023.32'}, 'XLM-BTC': {'ask': '0.00000727', 'bid': '0.00000725'}, 'BCH-USD': {'ask': '601.76', 'bid': '601.6'}, 'MIR-USD': {'ask': '3.395', 'bid': '3.392'}, 'XTZ-BTC': {'ask': '0.00007431', 'bid': '0.00007418'}, 'ANKR-BTC': {'ask': '0.00000213', 'bid': '0.00000212'}, 'XTZ-GBP': {'ask': '2.37231', 'bid': '2.37125'}, 'SOL-EUR': {'ask': '34.044', 'bid': '34.009'}, 'CVC-USDC': {'ask': '0.304739', 'bid': '0.304448'}, 'RLC-BTC': {'ask': '0.0000838', 'bid': '0.0000835'}, 'SUSHI-ETH': {'ask': '0.003539', 'bid': '0.003535'}, 'CLV-EUR': {'ask': '1.41', 'bid': '1.4'}, 'PLA-USD': {'ask': '0.9829', 'bid': '0.9815'}, 'ADA-USD': {'ask': '1.7146', 'bid': '1.7143'}, 'MANA-EUR':
           {'ask': '0.661', 'bid': '0.66'}, 'CHZ-USDT': {'ask': '0.3337', 'bid': '0.3331'}, 'ATOM-BTC': {'ask': '0.000314', 'bid': '0.000313'}, 'TRU-BTC': {'ask': '0', 'bid': '0'}, 'GRT-USD': {'ask': '0.7987', 'bid': '0.7985'}, 'TRU-USDT': {'ask': '0', 'bid': '0'}, 'STORJ-BTC': {'ask': '0.00002563', 'bid': '0.00002558'}, 'REQ-BTC': {'ask': '0', 'bid': '0'}, 'UST-EUR': {'ask': '0.855', 'bid': '0.853'}, 'UMA-GBP': {'ask': '7.651', 'bid': '7.632'}, 'LINK-USD': {'ask': '24.51105', 'bid': '24.50835'}, 'BNT-BTC': {'ask': '0.00008854', 'bid': '0.0000883'}, 'ETH-USDC': {'ask': '3026.45', 'bid': '3025.39'}, 'ETH-USDT': {'ask': '3025.66', 'bid': '3024.49'}, 'USDT-GBP': {'ask': '0.7228', 'bid': '0.7227'}, 'SNX-GBP': {'ask': '7.342', 'bid': '7.34'}, 'KNC-USD': {'ask': '1.7118', 'bid': '1.709'}, 'MANA-USDC': {'ask': '0.775644', 'bid': '0.774564'}, 'AAVE-EUR': {'ask': '326.297', 'bid': '325.851'}, 'LINK-BTC': {'ask': '0.00055456', 'bid': '0.00055415'}, 'SNX-EUR': {'ask': '8.6562', 'bid': '8.65'}, 'OMG-GBP': {'ask': '3.5615', 'bid': '3.5568'}, 'ICP-USD': {'ask': '62.729', 'bid': '62.68'}, 'MANA-BTC': {'ask': '0.0000176', 'bid':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '0.0000175'}, 'OXT-USD': {'ask': '0.3734', 'bid': '0.3733'}, 'GTC-USD': {'ask': '8.331', 'bid': '8.3'}, 'IOTX-USDT': {'ask': '0.12169', 'bid': '0.12089'}, 'WLUNA-GBP': {'ask': '0', 'bid': '0'}, 'CRV-USD': {'ask': '1.9601', 'bid': '1.9577'}, 'DAI-USD': {'ask': '1.00098', 'bid': '1.000965'}, 'DOGE-USD': {'ask': '0.2598', 'bid': '0.2597'}, 'LTC-EUR': {'ask': '139.59', 'bid': '139.49'}, 'GRT-EUR': {'ask': '0.6813', 'bid': '0.6805'}, 'FORTH-EUR': {'ask': '14.013', 'bid': '13.99'}, 'TRIBE-USD': {'ask': '0.6679', 'bid': '0.6607'}, 'ETC-BTC': {'ask': '0.001335', 'bid': '0.001334'}, 'OGN-BTC': {'ask': '0.0000201', 'bid': '0.00002'}, 'FORTH-BTC': {'ask': '0.0003725', 'bid': '0.0003713'}, 'ADA-USDC': {'ask': '1.715', 'bid': '1.713'}, 'RLY-USD': {'ask': '0.5106', 'bid': '0.5093'}, 'WBTC-USD': {'ask': '44222.85', 'bid': '44191.27'}, 'BAND-USD': {'ask': '7.6511', 'bid': '7.6437'}, 'FIL-EUR': {'ask': '57.5045', 'bid': '57.444'}, 'NU-GBP': {'ask': '0.1904', 'bid': '0.1898'}, 'DASH-BTC': {'ask': '0.00392697', 'bid': '0.00391955'}, 'ZEC-BTC': {'ask': '0.003001', 'bid': '0.002996'}, 'ALGO-EUR': {'ask': '0.7444', 'bid': '0.7435'}, 'MASK-USD': {'ask': '6.28', 'bid': '6.27'}, 'BAND-EUR': {'ask': '6.5225', 'bid': '6.5158'}, 'OMG-USD': {'ask': '4.9289', 'bid': '4.9263'}, 'MLN-USD': {'ask': '93.765', 'bid': '93.764'}, 'BTC-USD': {'ask': '44211.1', 'bid': '44211.09'}, 'BAT-BTC': {'ask': '0.0000159', 'bid': '0.0000158'}, 'RLY-USDT': {'ask': '0.5099', 'bid': '0.509'}, 'COMP-USD': {'ask': '445.62', 'bid': '445.41'}, 'DAI-USDC': {'ask': '1.001001', 'bid': '1.000981'}, 'REP-BTC': {'ask': '0.000613', 'bid': '0.000612'}, 'ORN-BTC': {'ask': '0.0001973', 'bid': '0.000196'}, 'CHZ-EUR': {'ask': '0.2846', 'bid': '0.2839'}, 'FET-USDT': {'ask': '0.4784', 'bid': '0.4778'}, 'UST-USDT': {'ask': '1.002',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'bid': '1.001'}, 'COMP-BTC': {'ask': '0.010084', 'bid': '0.01007'}, 'QNT-USD': {'ask': '149.37', 'bid': '149.15'}, 'LTC-USD': {'ask': '163.73', 'bid': '163.72'}, 'DASH-USD': {'ask': '173.474', 'bid': '173.307'}, 'SUSHI-GBP': {'ask': '7.738', 'bid': '7.729'}, 'NMR-GBP': {'ask': '28.4765', 'bid': '28.4081'}, 'XTZ-EUR': {'ask': '2.79882', 'bid': '2.79596'}, 'WLUNA-EUR': {'ask': '0', 'bid': '0'}, 'CLV-USDT': {'ask': '1.66', 'bid': '1.64'}, 'CHZ-USD': {'ask': '0.3337', 'bid': '0.3333'}, 'USDT-USDC': {'ask': '1.0003', 'bid': '1.0002'}, 'SUSHI-BTC': {'ask': '0.0002421', 'bid': '0.00024187'}, 'BTC-USDT': {'ask': '44212.84', 'bid': '44195.54'}, 'LTC-BTC': {'ask': '0.003704', 'bid': '0.003702'}, 'WLUNA-BTC': {'ask': '0', 'bid': '0'}, 'SKL-USD': {'ask': '0.2891', 'bid': '0.2889'}, 'ETH-BTC': {'ask': '0.06845', 'bid': '0.06843'}, 'SOL-GBP': {'ask': '28.89', 'bid': '28.851'}, 'DOT-USD': {'ask': '20.389', 'bid': '20.378'}, 'BAL-BTC': {'ask': '0.00055598', 'bid': '0.00055519'}, 'DOT-GBP': {'ask': '14.739', 'bid': '14.718'}, 'NKN-USD': {'ask': '0.4031', 'bid': '0.4024'}, 'RLC-USD': {'ask': '3.699', 'bid': '3.693'}, 'GRT-BTC': {'ask': '0.00001809', 'bid': '0.00001805'}, 'AAVE-BTC': {'ask': '0.00865422', 'bid': '0.00864968'}, 'SKL-BTC': {'ask': '0.00000654', 'bid': '0.00000653'}, 'REQ-EUR': {'ask': '0', 'bid': '0'}, 'FIL-BTC': {'ask': '0.00152567', 'bid': '0.00152398'}, '1INCH-EUR': {'ask': '2.343', 'bid': '2.338'}, 'CTSI-BTC': {'ask': '0.0000156', 'bid': '0.0000155'}, 'TRU-EUR': {'ask': '0', 'bid': '0'}, 'ATOM-USD': {'ask': '13.858', 'bid': '13.85'}, 'FIL-USD': {'ask': '67.4388', 'bid': '67.4269'}, 'ANKR-USD': {'ask': '0.09377', 'bid': '0.09372'}, 'ADA-ETH': {'ask': '0.000567', 'bid': '0.000566'}, 'ETH-USD': {'ask': '3025.47', 'bid': '3025.46'}, 'EOS-BTC': {'ask': '0.000105', 'bid': '0.000104'}, 'ZRX-USD': {'ask': '0.926042', 'bid': '0.925704'}, 'WBTC-BTC': {'ask': '1', 'bid': '0.9998'}, 'MATIC-BTC': {'ask': '0.00002917', 'bid': '0.00002915'}, 'FET-USD': {'ask': '0.4786', 'bid': '0.4781'}, 'NKN-BTC': {'ask': '0.0000092', 'bid': '0.000009'}, 'ZRX-EUR': {'ask': '0.789436', 'bid': '0.788861'}, 'MKR-USD': {'ask': '3206.6676', 'bid': '3204.5766'}, 'UNI-USD': {'ask': '27.3569', 'bid': '27.3475'}, 'UMA-EUR': {'ask': '9.029', 'bid': '9.015'}, 'ETC-EUR': {'ask': '50.266', 'bid': '50.231'}, 'POLY-USD': {'ask': '0.2841', 'bid': '0.2833'}, 'ADA-BTC': {'ask': '0.00003876', 'bid': '0.00003874'}, 'CLV-GBP': {'ask': '1.2', 'bid': '1.19'}, 'LRC-USD': {'ask': '0.2818', 'bid': '0.2816'}, 'DOT-BTC': {'ask': '0.0004611', 'bid': '0.0004607'}, 'XLM-EUR': {'ask': '0.273601', 'bid': '0.273263'}, 'ENJ-USD': {'ask': '1.519', 'bid': '1.517'}, 'MATIC-USD': {'ask': '1.2897', 'bid': '1.2894'}, 'USDT-EUR': {'ask': '0.8525', 'bid': '0.8523'}, 'DOGE-USDT': {'ask': '0.2595', 'bid': '0.2592'}, 'MATIC-GBP': {'ask': '0.9325', 'bid': '0.9314'}, 'AAVE-GBP': {'ask': '276.579', 'bid': '276.298'}, 'NMR-BTC': {'ask': '0.00089192', 'bid': '0.00088961'}, 'FORTH-GBP': {'ask': '11.889', 'bid': '11.83'}, 'EOS-USD': {'ask': '4.624', 'bid': '4.621'}, 'TRB-BTC': {'ask': '0.0010326', 'bid': '0.0010308'}, 'BNT-GBP': {'ask': '2.8252', 'bid': '2.8197'}, 'MIR-EUR': {'ask': '2.897', 'bid': '2.892'}, 'TRB-USD': {'ask': '45.683', 'bid': '45.609'}, 'SOL-USD': {'ask': '39.99', 'bid': '39.957'}, 'LINK-EUR': {'ask': '20.9133', 'bid': '20.89739'}, 'SKL-EUR': {'ask': '0.2465', 'bid': '0.2463'}, 'REQ-GBP': {'ask': '0', 'bid': '0'}, 'ETH-GBP': {'ask': '2187.55', 'bid': '2186.82'}, 'BAND-GBP': {'ask': '5.5395', 'bid': '5.5278'}}

print(tickers)


def buildGraph(tickers):
    graph = {}

    for tickerKey in tickers.keys():
        if tickers[tickerKey]["bid"] != "0" and tickers[tickerKey]["ask"] != "0":
            ticker1, ticker2 = tickerKey.split('-')
            t1_t2_conversion = float(tickers[tickerKey]["bid"])
            t2_t1_conversion = 1 / float(tickers[tickerKey]["ask"])
            if ticker1 not in graph:
                graph[ticker1] = []
            if ticker2 not in graph:
                graph[ticker2] = []
            graph[ticker1].append((ticker2, t1_t2_conversion))
            graph[ticker2].append((ticker1, t2_t1_conversion))

    return graph


"""
graph is built

queue
visited set()
bestExchange{BTC: BESTPOSSIBLE}

queue.append(base_currency)

while queue:
    curr = pop()
    currentPrice = bestExchange[edge] 
    edges = graph[curr]

    for edge in edges:
        edgeprice = currentPrice * edge_exchange
        if edgeprice > bestExchange(edge):
            bestExchange = edgeprice
            if edge in visited:
                edge add to queue
                add to visited
    
return bestExchange[quoteCurrency]
"""


def calculateBestExchange(tickers, base_currency, base_amount, quote_currency):
    exchangeRates = buildGraph(tickers)

    bestExchangeRate = {}
    for key in exchangeRates.keys():
        bestExchangeRate[key] = 0
        if key == base_currency:
            bestExchangeRate[key] = base_amount
    queue = deque()
    queue.append(base_currency)
    visited = set()
    visited.add(base_currency)

    while queue:
        currentCurrency = queue.popleft()
        currentPrice = bestExchangeRate[currentCurrency]

        if currentCurrency == quote_currency:
            continue

        edges = exchangeRates[currentCurrency]
        for edge in edges:
            edgeCurrency, edgeExchangeRate = edge
            edgePrice = currentPrice * edgeExchangeRate
            if edgePrice > bestExchangeRate[edgeCurrency]:
                bestExchangeRate[edgeCurrency] = edgePrice
                if edgeCurrency not in visited:
                    visited.add(edgeCurrency)
                    queue.append(edgeCurrency)
    print(bestExchangeRate)
    return bestExchangeRate[quote_currency]


print(calculateBestExchange(tickers, "USD", 100, "EUR"))
"""
# https://api.pro.coinbase.com/products
# array
    #{"id":"OMG-GBP","base_currency":"OMG","quote_currency":"GBP"}
    id
    base
    quote
   
make 277 request

    
# https://api.pro.coinbase.com/products/BTC-USD/ticker
    {"trade_id":201722029,"price":"44233.62","size":"0.00112866","time":"2021-08-12T15:56:32.842082Z","bid":"44236.33","ask":"44236.34","volume":"12831.52060036"}
"""
