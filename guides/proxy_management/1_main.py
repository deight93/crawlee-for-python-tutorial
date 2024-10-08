# import asyncio
#
# from crawlee.proxy_configuration import ProxyConfiguration
#
#
# async def main() -> None:
#     proxy_configuration = ProxyConfiguration(
#         proxy_urls=[
#             'http://proxy-1.com/',
#             'http://proxy-2.com/',
#         ]
#     )
#
#     # The proxy URLs are rotated in a round-robin.
#     proxy_url_1 = await proxy_configuration.new_url()  # http://proxy-1.com/
#     proxy_url_2 = await proxy_configuration.new_url()  # http://proxy-2.com/
#     proxy_url_3 = await proxy_configuration.new_url()  # http://proxy-1.com/
#
# if __name__ == '__main__':
#     asyncio.run(main())


import asyncio

from crawlee.beautifulsoup_crawler import BeautifulSoupCrawler, BeautifulSoupCrawlingContext
from crawlee.proxy_configuration import ProxyConfiguration


async def main() -> None:
    # Create a ProxyConfiguration object and pass it to the crawler.
    proxy_configuration = ProxyConfiguration(
        proxy_urls=[
            'http://proxy-1.com/',
            'http://proxy-2.com/',
        ]
    )
    crawler = BeautifulSoupCrawler(proxy_configuration=proxy_configuration)

    # Define the default request handler, which will be called for every request.
    @crawler.router.default_handler
    async def default_handler(context: BeautifulSoupCrawlingContext) -> None:
        # Extract data from the page.
        data = {
            'url': context.request.url,
            'title': context.soup.title.string if context.soup.title else None,
        }
        context.log.info(f'Extracted data: {data}')

    # Run the crawler with the initial list of requests.
    await crawler.run(['https://crawlee.dev/'])


if __name__ == '__main__':
    asyncio.run(main())