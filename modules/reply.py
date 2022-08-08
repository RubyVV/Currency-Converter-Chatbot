from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn, QuickReply, QuickReplyButton
)

from modules.currency import get_exchange_table

table = get_exchange_table()

# official files
# https://github.com/line/line-bot-sdk-python

# common FAQ
faq = {
    'American Dollar': TextSendMessage(
        text= 'USD' + '\n' + 'bid: ' + table['American Dollar']['bid'] + '\n' + 'offer: ' + table['American Dollar']['offer']
    ),
    'Hong Kong Dollar': TextSendMessage(
        text= 'HKD' + '\n' + 'bid: ' + table['Hong Kong Dollar']['bid'] + '\n' + 'offer: ' + table['Hong Kong Dollar']['offer']
    ),

    'British Pound': TextSendMessage(
        text= 'GBP' + '\n' + 'bid: ' + table['British Pound']['bid'] + '\n' + 'offer: ' + table['British Pound']['offer']
    ),

    'Australian Dollar': TextSendMessage(
        text= 'AUD' + '\n' + 'bid: ' + table['Australian Dollar']['bid'] + '\n' + 'offer: ' + table['Australian Dollar']['offer']
    ),

    'Canadian Dollar': TextSendMessage(
        text= 'CAD' + '\n' + 'bid: ' + table['Canadian Dollar']['bid'] + '\n' + 'offer: ' + table['Canadian Dollar']['offer']
    ),

    'Singapore Dollar': TextSendMessage(
        text= 'SGD' + '\n' + 'bid: ' + table['Singapore Dollar']['bid'] + '\n' + 'offer: ' + table['Singapore Dollar']['offer']
    ),

    'Swiss Franc': TextSendMessage(
        text= 'CHF' + '\n' + 'bid: ' + table['Swiss Franc']['bid'] + '\n' + 'offer: ' + table['Swiss Franc']['offer']
    ),

    'Japanese Yen': TextSendMessage(
        text= 'JPY' + '\n' + 'bid: ' + table['Japanese Yen']['bid'] + '\n' + 'offer: ' + table['Japanese Yen']['offer']
    ),

    'Swedish Krona': TextSendMessage(
        text= 'SEK' + '\n' + 'bid: ' + table['Swedish Krona']['bid'] + '\n' + 'offer: ' + table['Swedish Krona']['offer']
    ),

    'Sticker': StickerSendMessage(
        package_id='1',
        sticker_id='1'
    ),
    
    'Hi!': TextSendMessage(
        text = 'Hi, what can I do for you?'
    ),
    'I wanna change some money': TextSendMessage(
        text = 'Sure! If you would like to know the current exchange rate, please type "Query".'
    ),
    'Do I need to make an appointment?': TextSendMessage(
        text = 'No, you can just walk in.'
    ),
    'Thank you!': TextSendMessage(
        text = "You're welcome! Is there anything else I can do for you?"
    ),
    'No, I am good': TextSendMessage(
        text = "OK. Have a nice day!"
    ),

    'Hall Photo': ImageSendMessage(
        original_content_url='https://lh5.googleusercontent.com/p/AF1QipM2QBHTqdQ1_WLQjhXaCOwM8aaRvdnorN-hliW2=w408-h306-k-no',
        preview_image_url='https://lh5.googleusercontent.com/p/AF1QipM2QBHTqdQ1_WLQjhXaCOwM8aaRvdnorN-hliW2=w408-h306-k-no'
    ),

    'Can you provide a photo of the hall?': ImageSendMessage(
        original_content_url='https://lh5.googleusercontent.com/p/AF1QipM2QBHTqdQ1_WLQjhXaCOwM8aaRvdnorN-hliW2=w408-h306-k-no',
        preview_image_url='https://lh5.googleusercontent.com/p/AF1QipM2QBHTqdQ1_WLQjhXaCOwM8aaRvdnorN-hliW2=w408-h306-k-no'
    ),

    'Transportation': TextSendMessage(text='How would you like to get there?',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="Take MRT", text="MRT")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="Take bus", text="Bus")
                              )
                          ])
                          ),
    'How can I get there?': TextSendMessage(text='How would you like to get there?',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="Take MRT", text="MRT")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="Take bus", text="Bus")
                              )
                          ])
                          ),
    'MRT': TextSendMessage(
        text="Take the MRT to Muzha Line Station and walk for 5 minutes."
    ),
    'Bus': TextSendMessage(
        text="Take the bus to Lianhua Station and walk for 3 minutes."
    ),
    'Address': LocationSendMessage(
        title='my location',
        address='Bank of Taiwan',
        latitude=26.8216381,
        longitude=116.4199868
    ),
    'Where is the bank?': LocationSendMessage(
        title='my location',
        address='Bank of Taiwan',
        latitude=26.8216381,
        longitude=116.4199868
    ),
    'Query': TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # Exchange Rate Menu One Image URL
                    thumbnail_image_url='https://picsum.photos/id/352/900/400',
                    title='Menu One',
                    text='Check real-time exchange rate',
                    actions=[
                        MessageAction(
                            label='American Dollar',
                            text= 'American Dollar'
                        ),
                        MessageAction(
                            label='Hong Kong Dollar',
                            text= 'Hong Kong Dollar'
                        ),
                        MessageAction(
                            label='British Pound',
                            text='British Pound'
                        )
                    ]
                ),
                CarouselColumn(
                    # Exchange Rate Menu Two Image URL
                    thumbnail_image_url='https://picsum.photos/id/364/900/400',
                    title='Menu Two',
                    text='Check real-time exchange rate',
                    actions=[
                        MessageAction(
                            label='Australian Dollar',
                            text='Australian Dollar'
                        ),
                        MessageAction(
                            label='Canadian Dollar',
                            text='Canadian Dollar'
                        ),
                        MessageAction(
                            label='Singapore Dollar',
                            text='Singapore Dollar'
                        )
                    ]
                ),
                CarouselColumn(
                    # Exchange Rate Menu Three Image URL
                    thumbnail_image_url='https://picsum.photos/id/355/900/400',
                    title='Menu Three',
                    text='Check real-time exchange rate',
                    actions=[
                        MessageAction(
                            label='Swiss Franc',
                            text='Swiss Franc'
                        ),
                        MessageAction(
                            label='Japanese Yen',
                            text='Japanese Yen'
                        ),
                        MessageAction(
                            label='Swedish Krona',
                            text='Swedish Krona'
                        )
                    ]
                )
            ]
        )
    )
}

# Main Menu
# Carousel Template
# https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template
menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                # Card One image URL
                thumbnail_image_url='https://picsum.photos/id/296/900/400',
                title='Main Menu One',
                text='Click the button below to start interacting',
                actions=[
                    MessageAction(
                        label='Exchange Rate Query',
                        text='Exchange Rate Query'
                    ),
                    MessageAction(
                        label='Opening Time',
                        text='Opening Time'
                    ),
                    MessageAction(
                        label='Address',
                        text='Address'
                    )
                ]
            ),
            CarouselColumn(
                # Card Two image URL
                thumbnail_image_url='https://picsum.photos/id/355/900/400',
                title='Main Menu Two',
                text='Click the button below to start interacting',
                actions=[
                    MessageAction(
                        label='Traffic Information',
                        text='Traffic'
                    ),
                    MessageAction(
                        label='Hall Photo',
                        text='Hall Photo'
                    ),
                    URIAction(
                        label='Official Website',
                        uri='https://train.csie.ntu.edu.tw/train/'
                    )
                ]
            )
        ]
    )
)
