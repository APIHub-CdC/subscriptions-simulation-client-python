# subscriptions-simulation-client-python
This API lets you manage the subscriptions to API Hub asynchronous events. It enables you to receive notifications (asynchronous events) from Círculo de Crédito next-generation products (Open Banking & Data Aggregation).

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import apihub_subscription_client
```

## Getting Started
##### Step 1. Get your x-api-key
Get your ```x-api-key``` Following step 1, 2 and 3 the start guide https://developer.circulodecredito.com.mx/guia-de-inicio

##### Step 2. Change url and request data

The following data to modify can be found in ```/test/test_web_hook_subscriptions_api.py ``` It is important change of initializing the url and host. Modify the URL ```host=the_url```  and ```x_api_key = 'your_api_key'```, as shown in the following code snippet:

```python
class TestWebHookSubscriptionsApi(unittest.TestCase):
    x_api_key = 'your_api_key'
    host = 'the_url'
    subscription_id = None

    def setUp(self):
        configuration =Configuration(host=self.host)        
        self.api = WebHookSubscriptionsApi(apihub_subscription_client.ApiClient(configuration))  # noqa: E501

    ...
    def test_post_subscription(self):        
        try:     
            enrollment = Subscription(
                event_type="mx.com.circulolaboral.employmentcheck",
                web_hook_url="your_url_webhook",
                enrollment_id=str(uuid.uuid4())
            )
           
            api_response =  self.api.post_subscription(self.x_api_key, enrollment)
            pprint(api_response)
            print(api_response.subscription.subscription_id)
        except ApiException as e:
            print("Exception when calling TestWebHookSubscriptionsApi->test_post_subscription: %s\n" % e)
    ...

```

##### Step 3 Run the unit test

Having the previous steps, all that remains is to run the unit test, with the following command:

```sh
python3 test_web_hook_subscriptions_api.py
```
## Author

api@circulodecredito.com.mx

