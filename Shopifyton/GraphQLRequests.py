# Python library to get requests in Luci 

# All GraphQL requests needed for Luci

# ORDERS_INFO
# Get last 10 orders with cursor
# Get order by ID
# Get all open orders (Unfulfilled and paid)
# 
# ORDERS_FULFILLMENT
# Fulfill order by order ID
# Update tracking info on an order by ID (Send email to the client for the first time)
# Cancel fulfill for an order
#
# WEBHOOKS
# Register any type of webhooks
# (Maybe) Save all the actual webhooks used 
#
#
from ShopifyData import WebhookFormat, WebhookTopics
import requests
from requests import Response

from ShopifyData import ShopifyDataConverter

class GraphQLRequests():
    def __init__(self, GraphQLUrl: str, Access_Token: str):
        self.GraphQLURL = GraphQLUrl
        self.Access_Token = Access_Token
        
    def __getHeaders(self):
        return { "X-Shopify-Access-Token" : self.Access_Token}

    #region Webhooks
    def CreateWebHook(self, topic: WebhookTopics, format: WebhookFormat, callbackUrl: str) -> Response:
        query = """
        mutation webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) {
            webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) {
                userErrors {
                    field
                    message
                }
                webhookSubscription {
                    id
                }
            }
            }
        """

        vars = dict({
            "topic": topic.value,
            "webhookSubscription": {
                "callbackUrl": callbackUrl,
                "format": format.value
            }
        })

        json = dict({"query" : query})
        json['variables'] = vars

        response = requests.post(url = self.GraphQLURL, 
                                headers = self.__getHeaders(), 
                                json = json)
        
        return response

    def DeleteWebHook(self, id: str):
        query = """
            mutation webhookSubscriptionDelete($id: ID!) {
                webhookSubscriptionDelete(id: $id) {
                    deletedWebhookSubscriptionId
                    userErrors {
                        field
                        message
                    }
                }
            }
        """ 

        vars = dict({
            "id": ShopifyDataConverter.WebhookGIDFromId(id)
        })

        json = dict({"query" : query})
        json['variables'] = vars

        response = requests.post(url = self.GraphQLURL, 
                                headers = self.__getHeaders(), 
                                json = json)
        
        return response
      
    #endregion

