
from __future__ import print_function

import json
import time
import worth
from worth.rest import ApiException
from pprint import pprint

def main():
    configuration = worth.Configuration()

    # Enter a context with an instance of the API client
    with worth.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = worth.AuthenticatorApi(api_client)
        api_device = worth.DeviceApi(api_client)
        access_key = '30ec62934072bd5f3313cd90958318fa' # str | access_key
        secret_key = 'f815ab5f87091bdb09cd7cb869cce8bc' # str | secret_key
        try:
            # 生成token
            api_response = api_instance.gen_token(access_key, secret_key)
            token = api_response.data['token'] 
            pprint(token)
	
            api_client.set_default_header('Authorization', token)

            data = {
			    'ACTION': 'SET_FEED_DEVICE_CONTROL',
			    'VALUE': {
				    'weight': 1,
			    },
		    }

            action = {
                'device_id': '3105000000000123',
                'data': json.dumps(data),
            }
            api_response = api_device.send_action(action)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticatorApi->gen_token: %s\n" % e)


if __name__ == "__main__":
    main()
