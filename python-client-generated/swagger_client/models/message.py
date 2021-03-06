# coding: utf-8

"""
    Ma super messagerie

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Message(object):
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
        'id': 'int',
        'emetteur': 'str',
        'contenu': 'str'
    }

    attribute_map = {
        'id': 'id',
        'emetteur': 'emetteur',
        'contenu': 'contenu'
    }

    def __init__(self, id=None, emetteur=None, contenu=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._emetteur = None
        self._contenu = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if emetteur is not None:
            self.emetteur = emetteur
        if contenu is not None:
            self.contenu = contenu

    @property
    def id(self):
        """Gets the id of this Message.  # noqa: E501

        Identifiant (unique) du message  # noqa: E501

        :return: The id of this Message.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Message.

        Identifiant (unique) du message  # noqa: E501

        :param id: The id of this Message.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def emetteur(self):
        """Gets the emetteur of this Message.  # noqa: E501

        Pseudo de l'emetteur du message  # noqa: E501

        :return: The emetteur of this Message.  # noqa: E501
        :rtype: str
        """
        return self._emetteur

    @emetteur.setter
    def emetteur(self, emetteur):
        """Sets the emetteur of this Message.

        Pseudo de l'emetteur du message  # noqa: E501

        :param emetteur: The emetteur of this Message.  # noqa: E501
        :type: str
        """

        self._emetteur = emetteur

    @property
    def contenu(self):
        """Gets the contenu of this Message.  # noqa: E501

        Contenu du message  # noqa: E501

        :return: The contenu of this Message.  # noqa: E501
        :rtype: str
        """
        return self._contenu

    @contenu.setter
    def contenu(self, contenu):
        """Sets the contenu of this Message.

        Contenu du message  # noqa: E501

        :param contenu: The contenu of this Message.  # noqa: E501
        :type: str
        """

        self._contenu = contenu

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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
