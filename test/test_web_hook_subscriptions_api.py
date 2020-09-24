# coding: utf-8

"""
    API Subscriptions Sandbox

    This API lets you manage the subscriptions to API Hub asynchronous events. It enables you to receive notifications (asynchronous events) from Círculo de Crédito next-generation products (Open Banking & Data Aggregation).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: api@circulodecredito.com.mx
"""


from __future__ import absolute_import

import unittest

import apihub_subscription_client
from apihub_subscription_client.api.web_hook_subscriptions_api import WebHookSubscriptionsApi  # noqa: E501
from apihub_subscription_client.configuration import Configuration
from apihub_subscription_client.rest import ApiException
from apihub_subscription_client.models.subscription import Subscription

from pprint import pprint
import uuid


class TestWebHookSubscriptionsApi(unittest.TestCase):
    x_api_key = 'GKD25Kfmc6VeoxGLAGtlrbYgZobDdB7S'
    host = 'https://circulodecredito-dev.apigee.net/sandbox'
    subscription_id = None

    def setUp(self):
        configuration =Configuration(host=self.host)        
        self.api = WebHookSubscriptionsApi(apihub_subscription_client.ApiClient(configuration))  # noqa: E501

    def test_get_subscriptions(self):
        try:     
            api_response =  self.api.get_subscriptions(self.x_api_key, page=1,per_page=5)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TestWebHookSubscriptionsApi->test_get_subscriptions: %s\n" % e)

    def test_post_subscription(self):        
        try:     
            enrollment = Subscription(
                event_type="mx.com.circulolaboral.employmentcheck",
                web_hook_url="https://webhook.site/44296c39-f929-4ee7-a188-83520842bf45",
                enrollment_id=str(uuid.uuid4())
            )
           
            api_response =  self.api.post_subscription(self.x_api_key, enrollment)
            pprint(api_response)
            print(api_response.subscription.subscription_id)
            if api_response.subscription != None:
                self.subscription_id = api_response.subscription.subscription_id
                self.get_subscription()
                self.delete_subscription()
      

        except ApiException as e:
            print("Exception when calling TestWebHookSubscriptionsApi->test_post_subscription: %s\n" % e)

    def get_subscription(self):
        try:     
            api_response =  self.api.get_subscription(self.x_api_key, self.subscription_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TestWebHookSubscriptionsApi->get_subscription: %s\n" % e)
   

    def delete_subscription(self):
        
        try:     
            api_response =  self.api.delete_subscription(self.x_api_key, self.subscription_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TestWebHookSubscriptionsApi->delete_subscription: %s\n" % e)

    


if __name__ == '__main__':
    unittest.main()
