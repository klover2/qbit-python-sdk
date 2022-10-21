<p style="text-align: center;">
  <h1 align="center"><a href="javascript:void(0);">qbit-python-sdk</a></h1>
</p>

## Qbit 概念

开发者 API 旨在允许企业与 Qbit 系统集成，并轻松将其作为其工作流程的一部分。该 API 允许开发者使用【全球账户】、【量子卡】业务等。

## 项目状态

当前版本`1.0.0`为正式版本。暂时支持了 auth 相关的接口，其他接口带后续完善，同时也提供了 Qbit Api 所需的 Post、put、delete、get 请求，方便使用者更好调用其他接口，具体使用请看下面代码示例。

`注意`：请商户的专业技术人员在使用时注意系统和软件的正确性和兼容性，以及带来的风险。

## 环境要求

- Python 3.7+

## 安装

最新版本已经在 [pypi](https://pypi.org/project/qbit-py-sdk/) 发布。

`pip install qbit-py-sdk`

### 使用

```python
import qbit_py_sdk as Qbit

qbit = Qbit.QbitClient("qbit1f6efee44ceb8ca2", "8f70d42a1393802aebf567be27a47879", "https://api-global.qbitnetwork.com")
```

## 名词解释

- Client，合作伙伴在 Qbit 我们称之为 Client。
- Account， 合作伙伴的客户在 Qbit 我们称之为 Account
- clientId，商户 id，请联系我们申请。
- clientSecret，商户密钥，用于签名，请联系我们申请。

## 开始

### 获取 access token

```python
codeRes = qbit.get_code(state='324', redirect_uri='')
res = qbit.get_access_token(codeRes.code)
print(res)
```

### 刷新 access token

```python
res = qbit.refresh_access_token("refreshToken")
print(res)
```

### 调用其他接口示例

```python
# 返回值 status 在 200 - 300 内表示请求正常
params = {
        "id": "5d890eda-16aa-4760-90af-3d60837f5616",
        "limit": 10
    }

res = qbit.config("access_token").get_request(
        "https://api-global.qbitnetwork.com/open-api/v1/budget", **params)
```

## 敏感信息加解密

### 加密-HmacSHA256

```python
from qbit_py_sdk import encryptHmacSHA256

data = {
        "id": "ee74c872-8173-4b67-81b1-5746e7d5ab88",
        "accountId": None,
        "holderId": "d2bd6ab3-3c28-4ac7-a7c4-b7eed5eee367",
        "currency": "USD",
        "settlementCurrency": None,
        "counterparty": "SAILINGWOOD;;US;1800948598;;091000019",
        "transactionAmount": 11,
        "fee": 0,
        "businessType": "Inbound",
        "status": "Closed",
        "transactionTime": "2021-11-22T07:34:10.997Z",
        "transactionId": "124d3804-defa-4033-9f30-1d8b0468e506",
        "clientTransactionId": None,
        "createTime": "2021-11-22T07:34:10.997Z",
        "appendFee": 0,
    }
res = encryptHmacSHA256("25d55ad283aa400af464c76d713c07ad", **data)
print(res == "8287d5539c03918c9de51176162c2bf7065d5a8756b014e3293be1920c20d102")
```

## 联系我们

如果你发现了**BUG**或者有任何疑问、建议，请通过 issue 进行反馈。

也欢迎访问我们的[官网](https://www.qbitnetwork.com/#/)。
