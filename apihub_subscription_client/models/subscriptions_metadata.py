# coding: utf-8

"""
    API Subscriptions Sandbox

    This API lets you manage the subscriptions to API Hub asynchronous events. It enables you to receive notifications (asynchronous events) from Círculo de Crédito next-generation products (Open Banking & Data Aggregation).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: api@circulodecredito.com.mx
"""


import pprint
import re  # noqa: F401

import six


class SubscriptionsMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'metadata': 'Metadata',
        'subscriptions': 'list[Subscription]'
    }

    attribute_map = {
        'metadata': '_metadata',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, metadata=None, subscriptions=None):  # noqa: E501
        """SubscriptionsMetadata - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._subscriptions = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def metadata(self):
        """Gets the metadata of this SubscriptionsMetadata.  # noqa: E501


        :return: The metadata of this SubscriptionsMetadata.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SubscriptionsMetadata.


        :param metadata: The metadata of this SubscriptionsMetadata.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def subscriptions(self):
        """Gets the subscriptions of this SubscriptionsMetadata.  # noqa: E501


        :return: The subscriptions of this SubscriptionsMetadata.  # noqa: E501
        :rtype: list[Subscription]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this SubscriptionsMetadata.


        :param subscriptions: The subscriptions of this SubscriptionsMetadata.  # noqa: E501
        :type: list[Subscription]
        """

        self._subscriptions = subscriptions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SubscriptionsMetadata, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubscriptionsMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
