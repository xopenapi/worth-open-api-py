# worth.AuthenticatorApi

All URIs are relative to *https://iot.worthcloud.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gen_token**](AuthenticatorApi.md#gen_token) | **GET** /v1/authenticator/{access_key}/{secret_key} | 生成token


# **gen_token**
> GenTokenResponse gen_token(access_key, secret_key)

生成token

生成token

### Example

```python
from __future__ import print_function
import time
import worth
from worth.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://iot.worthcloud.net
# See configuration.py for a list of all supported configuration parameters.
configuration = worth.Configuration(
    host = "https://iot.worthcloud.net"
)


# Enter a context with an instance of the API client
with worth.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = worth.AuthenticatorApi(api_client)
    access_key = 'access_key_example' # str | access_key
secret_key = 'secret_key_example' # str | secret_key

    try:
        # 生成token
        api_response = api_instance.gen_token(access_key, secret_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticatorApi->gen_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | **str**| access_key | 
 **secret_key** | **str**| secret_key | 

### Return type

[**GenTokenResponse**](GenTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

