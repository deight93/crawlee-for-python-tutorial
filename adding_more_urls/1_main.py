import asyncio

from crawlee.beautifulsoup_crawler import BeautifulSoupCrawler, BeautifulSoupCrawlingContext
from crawlee import EnqueueStrategy
from crawlee import Glob

async def main() -> None:
    # Let's limit our crawls to make our tests shorter and safer.
    crawler = BeautifulSoupCrawler(max_requests_per_crawl=20)

    @crawler.router.default_handler
    async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
        url = context.request.url
        title = context.soup.title.string if context.soup.title else ''
        context.log.info(f'The title of {url} is: {title}.')

        # The enqueue_links function is available as one of the fields of the context.
        # It is also context aware, so it does not require any parameters.
        # await context.enqueue_links()

        # If you need to override the default selection of elements in enqueue_links, you can use the selector argument.
        # await context.enqueue_links(selector='a.article-link')

        # See the EnqueueStrategy object for more strategy options.
        # await context.enqueue_links(strategy=EnqueueStrategy.SAME_DOMAIN)

        # Wanders the internet.
        # await context.enqueue_links(strategy=EnqueueStrategy.ALL)

        # Filter URLs with patterns
        await context.enqueue_links(
            include=[Glob('https://crawlee.dev/docs/**')],
            exclude=[Glob('https://**/docs/3.10/**')],
        )

    await crawler.run(['https://crawlee.dev/'])


if __name__ == '__main__':
    asyncio.run(main())