# worth.DeviceApi

All URIs are relative to *https://iot.worthcloud.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_action**](DeviceApi.md#send_action) | **POST** /v1/devices/send_action | 发送指令


# **send_action**
> APIResponse send_action(body)

发送指令

发送指令

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
    api_instance = worth.DeviceApi(api_client)
    body = worth.ActionReq() # ActionReq | 

    try:
        # 发送指令
        api_response = api_instance.send_action(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceApi->send_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActionReq**](ActionReq.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

