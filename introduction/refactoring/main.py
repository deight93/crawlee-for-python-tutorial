import asyncio

from crawlee.playwright_crawler import PlaywrightCrawler

from introduction.refactoring.routes import router


async def main() -> None:
    crawler = PlaywrightCrawler(
        # Let's limit our crawls to make our tests shorter and safer.
        max_requests_per_crawl=55,
        # Provide our router instance to the crawler.
        request_handler=router,
    )

    await crawler.run(['https://warehouse-theme-metal.myshopify.com/collections'])


if __name__ == '__main__':
    asyncio.run(main())