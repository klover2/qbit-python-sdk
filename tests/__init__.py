import qbit_py_sdk as Qbit
from qbit_py_sdk import encryptHmacSHA256

if __name__ == '__main__':
    qbit = Qbit.QbitClient("qbit1f6efee44ceb8ca2", "8f70d42a1393802aebf567be27a47879", "http://127.0.0.1:3000")

    codeRes = qbit.get_code(state='324', redirect_uri='')
    res = qbit.get_access_token(codeRes.code)

    res = qbit.refresh_access_token("983cd6b17c833b1149401f4ffaf1731c92b69621d9fa283164c0843c4a546e43")
    print(res)

    # params = {
    #     "cardId": "212fbeed-d27b-4b03-b7c0-b7601afa0a44",
    # }
    # res = qbit.config("6b4c6541ea36fcca82ed07d39093e70e32f5d191").delete_request(
    #     "http://127.0.0.1:3000/open-api/v1/cards", **params)
    # print(res)

    # data = {
    #     "id": "ee74c872-8173-4b67-81b1-5746e7d5ab88",
    #     "accountId": None,
    #     "holderId": "d2bd6ab3-3c28-4ac7-a7c4-b7eed5eee367",
    #     "currency": "USD",
    #     "settlementCurrency": None,
    #     "counterparty": "SAILINGWOOD;;US;1800948598;;091000019",
    #     "transactionAmount": 11,
    #     "fee": 0,
    #     "businessType": "Inbound",
    #     "status": "Closed",
    #     "transactionTime": "2021-11-22T07:34:10.997Z",
    #     "transactionId": "124d3804-defa-4033-9f30-1d8b0468e506",
    #     "clientTransactionId": None,
    #     "createTime": "2021-11-22T07:34:10.997Z",
    #     "appendFee": 0,
    # }
    # res = encryptHmacSHA256("25d55ad283aa400af464c76d713c07ad", **data)
    # print(res == "8287d5539c03918c9de51176162c2bf7065d5a8756b014e3293be1920c20d102")
