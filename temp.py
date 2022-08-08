'Query': TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # Exchange Rate Menu One Image URL
                    thumbnail_image_url='https://picsum.photos/id/352/900/400',
                    title='Exchange Rate Menu One', 
                    text='Click the button below to check the real-time exchange rate',
                    actions=[
                        MessageAction(
                            label='US Dollar Query',
                            text='USD'
                        ),
                        MessageAction(
                            label='Hong Kong Dollar Query',
                            text='HKD'
                        ),
                        MessageAction(
                            label='British Pound Query',
                            text='GBP'
                        )
                    ]
                ),
                CarouselColumn(
                    # Exchange Rate Menu Two Image URL
                    thumbnail_image_url='https://picsum.photos/id/364/900/400',
                    title='Exchange Rate Menu Two',
                    text='Click the button below to check the real-time exchange rate',
                    actions=[
                        MessageAction(
                            label='Australian Dollar Query',
                            text='AUD'
                        ),
                        MessageAction(
                            label='Canadian Dollar Query',
                            text='CAD'
                        ),
                        MessageAction(
                            label='Singapore Dollar Query',
                            text='SGD'
                        )
                    ]
                ),
                CarouselColumn(
                    # Exchange Rate Menu Three Image URL
                    thumbnail_image_url='https://picsum.photos/id/355/900/400',
                    title='Exchange Rate Menu Three',
                    text='Click the button below to check the real-time exchange rate',
                    actions=[
                        MessageAction(
                            label='Swiss Franc Query',
                            text='CHF'
                        ),
                        MessageAction(
                            label='Japanese Yen Query',
                            text='JPY'
                        ),
                        MessageAction(
                            label='Swedish Krona Query',
                            text='SEK'
                        )
                    ]
                )
            ]
        )
    )