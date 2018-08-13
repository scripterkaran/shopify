
import Client from 'shopify-buy';

const client = Client.buildClient({
    domain: 'mishipaypos.myshopify.com',
    storefrontAccessToken: 'f1cabf456825f3ecff4f856a278760ad'
});

export default client
