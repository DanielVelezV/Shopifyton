# Python library to get requests in Luci 

# Converts normal data to data used on the Shopify GraphQL admin API

# Enums with all webhook topics
# Convert normal data to Shopify data: Ej: LineItemId to gid://LineItems:12312312

from enum import Enum

class WebhookTopics(Enum):
    APP_SUBSCRIPTIONS_UPDATE = "APP_SUBSCRIPTIONS_UPDATE"
    APP_UNINSTALLED = "APP_UNINSTALLED"
    ATTRIBUTED_SESSIONS_FIRST = "ATTRIBUTED_SESSIONS_FIRST"
    ATTRIBUTED_SESSIONS_LAST = "ATTRIBUTED_SESSIONS_LAST"
    BULK_OPERATIONS_FINISH = "BULK_OPERATIONS_FINISH"
    CARTS_CREATE = "CARTS_CREATE"
    CARTS_UPDATE = "CARTS_UPDATE"
    CHANNELS_DELETE = "CHANNELS_DELETE"
    CHECKOUTS_CREATE = "CHECKOUTS_CREATE"
    CHECKOUTS_DELETE = "CHECKOUTS_DELETE"
    CHECKOUTS_UPDATE = "CHECKOUTS_UPDATE"
    COLLECTIONS_CREATE = "COLLECTIONS_CREATE"
    COLLECTIONS_DELETE = "COLLECTIONS_DELETE"
    COLLECTIONS_UPDATE = "COLLECTIONS_UPDATE"
    COLLECTION_LISTINGS_ADD = "COLLECTION_LISTINGS_ADD"
    COLLECTION_LISTINGS_REMOVE = "COLLECTION_LISTINGS_REMOVE"
    COLLECTION_LISTINGS_UPDATE = "COLLECTION_LISTINGS_UPDATE"
    COLLECTION_PUBLICATIONS_CREATE = "COLLECTION_PUBLICATIONS_CREATE"
    COLLECTION_PUBLICATIONS_DELETE = "COLLECTION_PUBLICATIONS_DELETE"
    COLLECTION_PUBLICATIONS_UPDATE = "COLLECTION_PUBLICATIONS_UPDATE"
    CUSTOMERS_CREATE = "CUSTOMERS_CREATE"
    CUSTOMERS_DELETE = "CUSTOMERS_DELETE"
    CUSTOMERS_DISABLE = "CUSTOMERS_DISABLE"
    CUSTOMERS_ENABLE = "CUSTOMERS_ENABLE"
    CUSTOMERS_MARKETING_CONSENT_UPDATE = "CUSTOMERS_MARKETING_CONSENT_UPDATE"
    CUSTOMERS_UPDATE = "CUSTOMERS_UPDATE"
    CUSTOMER_GROUPS_CREATE = "CUSTOMER_GROUPS_CREATE"
    CUSTOMER_GROUPS_DELETE = "CUSTOMER_GROUPS_DELETE"
    CUSTOMER_GROUPS_UPDATE = "CUSTOMER_GROUPS_UPDATE"
    CUSTOMER_PAYMENT_METHODS_CREATE = "CUSTOMER_PAYMENT_METHODS_CREATE"
    CUSTOMER_PAYMENT_METHODS_REVOKE = "CUSTOMER_PAYMENT_METHODS_REVOKE"
    CUSTOMER_PAYMENT_METHODS_UPDATE = "CUSTOMER_PAYMENT_METHODS_UPDATE"
    DISPUTES_CREATE = "DISPUTES_CREATE"
    DISPUTES_UPDATE = "DISPUTES_UPDATE"
    DOMAINS_CREATE = "DOMAINS_CREATE"
    DOMAINS_DESTROY = "DOMAINS_DESTROY"
    DOMAINS_UPDATE = "DOMAINS_UPDATE"
    DRAFT_ORDERS_CREATE = "DRAFT_ORDERS_CREATE"
    DRAFT_ORDERS_DELETE = "DRAFT_ORDERS_DELETE"
    DRAFT_ORDERS_UPDATE = "DRAFT_ORDERS_UPDATE"
    FULFILLMENTS_CREATE = "FULFILLMENTS_CREATE"
    FULFILLMENTS_UPDATE = "FULFILLMENTS_UPDATE"
    FULFILLMENT_EVENTS_CREATE = "FULFILLMENT_EVENTS_CREATE"
    FULFILLMENT_EVENTS_DELETE = "FULFILLMENT_EVENTS_DELETE"
    INVENTORY_ITEMS_CREATE = "INVENTORY_ITEMS_CREATE"
    INVENTORY_ITEMS_DELETE = "INVENTORY_ITEMS_DELETE"
    INVENTORY_ITEMS_UPDATE = "INVENTORY_ITEMS_UPDATE"
    INVENTORY_LEVELS_CONNECT = "INVENTORY_LEVELS_CONNECT"
    INVENTORY_LEVELS_DISCONNECT = "INVENTORY_LEVELS_DISCONNECT"
    INVENTORY_LEVELS_UPDATE = "INVENTORY_LEVELS_UPDATE"
    LOCALES_CREATE = "LOCALES_CREATE"
    LOCALES_UPDATE = "LOCALES_UPDATE"
    LOCATIONS_CREATE = "LOCATIONS_CREATE"
    LOCATIONS_DELETE = "LOCATIONS_DELETE"
    LOCATIONS_UPDATE = "LOCATIONS_UPDATE"
    MARKETS_CREATE = "MARKETS_CREATE"
    MARKETS_DELETE = "MARKETS_DELETE"
    MARKETS_UPDATE = "MARKETS_UPDATE"
    ORDERS_CANCELLED = "ORDERS_CANCELLED"
    ORDERS_CREATE = "ORDERS_CREATE"
    ORDERS_DELETE = "ORDERS_DELETE"
    ORDERS_EDITED = "ORDERS_EDITED"
    ORDERS_FULFILLED = "ORDERS_FULFILLED"
    ORDERS_PAID = "ORDERS_PAID"
    ORDERS_PARTIALLY_FULFILLED = "ORDERS_PARTIALLY_FULFILLED"
    ORDERS_UPDATED = "ORDERS_UPDATED"
    ORDER_TRANSACTIONS_CREATE = "ORDER_TRANSACTIONS_CREATE"
    PAYMENT_TERMS_CREATE = "PAYMENT_TERMS_CREATE"
    PAYMENT_TERMS_DELETE = "PAYMENT_TERMS_DELETE"
    PAYMENT_TERMS_UPDATE = "PAYMENT_TERMS_UPDATE"
    PRODUCTS_CREATE = "PRODUCTS_CREATE"
    PRODUCTS_DELETE = "PRODUCTS_DELETE"
    PRODUCTS_UPDATE = "PRODUCTS_UPDATE"
    PRODUCT_LISTINGS_ADD = "PRODUCT_LISTINGS_ADD"
    PRODUCT_LISTINGS_REMOVE = "PRODUCT_LISTINGS_REMOVE"
    PRODUCT_LISTINGS_UPDATE = "PRODUCT_LISTINGS_UPDATE"
    PRODUCT_PUBLICATIONS_CREATE = "PRODUCT_PUBLICATIONS_CREATE"
    PRODUCT_PUBLICATIONS_UPDATE = "PRODUCT_PUBLICATIONS_UPDATE"
    PROFILES_CREATE = "PROFILES_CREATE"
    PROFILES_DELETE = "PROFILES_DELETE"
    PROFILES_UPDATE = "PROFILES_UPDATE"
    REFUNDS_CREATE = "REFUNDS_CREATE"
    SCHEDULED_PRODUCT_LISTINGS_ADD = "SCHEDULED_PRODUCT_LISTINGS_ADD"
    SCHEDULED_PRODUCT_LISTINGS_REMOVE = "SCHEDULED_PRODUCT_LISTINGS_REMOVE"
    SCHEDULED_PRODUCT_LISTINGS_UPDATE = "SCHEDULED_PRODUCT_LISTINGS_UPDATE"
    SEGMENTS_CREATE = "SEGMENTS_CREATE"
    SEGMENTS_DELETE = "SEGMENTS_DELETE"
    SEGMENTS_UPDATE = "SEGMENTS_UPDATE"
    SELLING_PLAN_GROUPS_CREATE = "SELLING_PLAN_GROUPS_CREATE"
    SELLING_PLAN_GROUPS_DELETE = "SELLING_PLAN_GROUPS_DELETE"
    SELLING_PLAN_GROUPS_UPDATE = "SELLING_PLAN_GROUPS_UPDATE"
    SHIPPING_ADDRESSES_CREATE = "SHIPPING_ADDRESSES_CREATE"
    SHIPPING_ADDRESSES_UPDATE = "SHIPPING_ADDRESSES_UPDATE"
    SHOP_UPDATE = "SHOP_UPDATE"
    SUBSCRIPTION_BILLING_ATTEMPTS_CHALLENGED = "SUBSCRIPTION_BILLING_ATTEMPTS_CHALLENGED"
    SUBSCRIPTION_BILLING_ATTEMPTS_FAILURE = "SUBSCRIPTION_BILLING_ATTEMPTS_FAILURE"
    SUBSCRIPTION_BILLING_ATTEMPTS_SUCCESS = "SUBSCRIPTION_BILLING_ATTEMPTS_SUCCESS"
    SUBSCRIPTION_CONTRACTS_CREATE = "SUBSCRIPTION_CONTRACTS_CREATE"
    SUBSCRIPTION_CONTRACTS_UPDATE = "SUBSCRIPTION_CONTRACTS_UPDATE"
    TAX_SERVICES_CREATE = "TAX_SERVICES_CREATE"
    TAX_SERVICES_UPDATE = "TAX_SERVICES_UPDATE"
    TENDER_TRANSACTIONS_CREATE = "TENDER_TRANSACTIONS_CREATE"
    THEMES_CREATE = "THEMES_CREATE"
    THEMES_DELETE = "THEMES_DELETE"
    THEMES_PUBLISH = "THEMES_PUBLISH"
    THEMES_UPDATE = "THEMES_UPDATE"
    VARIANTS_IN_STOCK = "VARIANTS_IN_STOCK"
    VARIANTS_OUT_OF_STOCK = "VARIANTS_OUT_OF_STOCK"

class WebhookFormat(Enum):
    JSON = "JSON"
    XML = "XML"

class ShopifyDataConverter():
    @staticmethod
    def LineItemGIDFromId(id: str):
        return f"gid://shopify/LineItem/{id}"
    
    @staticmethod
    def OrderGIDFromId(id: str):
        return f"gid://shopify/Order/{id}"

    @staticmethod
    def WebhookGIDFromId(id: str):
        return f"gid://shopify/WebhookSubscription/{id}"