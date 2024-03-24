import json
import os
from telethon import TelegramClient, events, utils
from config import *

client = TelegramClient('anon', api_id, api_hash)


async def write_details_to_text_file(folder_name, messages):
    with open(os.path.join(folder_name, 'downloaded_data_details.txt'), 'w', encoding='utf-8') as text_file:
        async for message in messages:
            text_file.write(f"Message ID: {message.id}\n")
            text_file.write(f"Sender ID: {message.sender_id}\n")
            text_file.write(f"Date: {message.date}\n")
            text_file.write(f"Message: {message.message}\n")
            text_file.write(f"Media Type: {'Photo' if message.photo else 'Document'}\n")
            
            text_file.write("\n")


@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'anodra' in event.raw_text.lower():
        await event.reply('yuklandi!')
        dialogs = []
        async for dialog in client.iter_dialogs():
            dialog_info = {
                'name': dialog.name,
                'id': dialog.id,
                'type': 'private' if dialog.is_user else 'group',
                'participants_count': dialog.participants_count if hasattr(dialog, 'participants_count') else None,
                'created_at': dialog.date.strftime('%Y-%m-%d %H:%M:%S') if hasattr(dialog, 'date') else None,
                'draft': dialog.draft,
                'message': {
                    'id': dialog.message.id,
                    'peer_id': dialog.message.peer_id,
                    'date': dialog.message.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'message': dialog.message.message,
                    'out': dialog.message.out,
                    'mentioned': dialog.message.mentioned,
                    'media_unread': dialog.message.media_unread,
                    'silent': dialog.message.silent,
                    'post': dialog.message.post,
                    'from_scheduled': dialog.message.from_scheduled,
                    'legacy': dialog.message.legacy,
                    'edit_hide': dialog.message.edit_hide,
                    'pinned': dialog.message.pinned,
                    'noforwards': dialog.message.noforwards,
                    'invert_media': dialog.message.invert_media,
                    'from_id': dialog.message.from_id,
                    'saved_peer_id': dialog.message.saved_peer_id,
                    'fwd_from': dialog.message.fwd_from,
                    'via_bot_id': dialog.message.via_bot_id,
                    'reply_to': dialog.message.reply_to,
                    'media': dialog.message.media,
                    'reply_markup': dialog.message.reply_markup,
                    'entities': dialog.message.entities,
                    'views': dialog.message.views,
                    'forwards': dialog.message.forwards,
                    'replies': dialog.message.replies,
                    'edit_date': dialog.message.edit_date,
                    'post_author': dialog.message.post_author,
                    'grouped_id': dialog.message.grouped_id,
                    'reactions': dialog.message.reactions,
                    'restriction_reason': dialog.message.restriction_reason,
                    'ttl_period': dialog.message.ttl_period
                }
            }
            dialogs.append(dialog_info)

        # Write the list of dialogs to a JSON file
        with open('dialogs.json', 'w', encoding='utf-8') as json_file:
            json.dump(dialogs, json_file, ensure_ascii=False, indent=4, default=str)

        # Disconnect the client
        await client.disconnect()

    elif '#yukla' in event.raw_text.lower():
        # Extract chat name, username, or ID
        chat_input = event.raw_text.split()[1]  # Assuming format is 'yukla chat_name|username|chat_id'
        try:
            chat_entity = await client.get_entity(chat_input)
            folder_name = utils.get_display_name(chat_entity).replace(" ", "_")
            os.makedirs(folder_name, exist_ok=True)
            os.makedirs(os.path.join(folder_name, 'images'), exist_ok=True)
            os.makedirs(os.path.join(folder_name, 'videos'), exist_ok=True)
            os.makedirs(os.path.join(folder_name, 'audios'), exist_ok=True)
            os.makedirs(os.path.join(folder_name, 'files'), exist_ok=True)

            msg = await event.reply('Yuklanmoqda...')

            async for message in client.iter_messages(chat_entity):
                if message.media:
                    if hasattr(message.media, 'photo'):
                        file_path = os.path.join(folder_name, 'images', f"{message.id}.jpg")
                    elif hasattr(message.media, 'document'):
                        if 'video' in message.media.document.mime_type:
                            file_path = os.path.join(folder_name, 'videos', f"{message.file.name}")
                        elif 'audio' in message.media.document.mime_type:
                            file_path = os.path.join(folder_name, 'audios', f"{message.file.name}")
                        else:
                            file_path = os.path.join(folder_name, 'files', f"{message.file.name}")
                    await client.download_media(message, file=file_path)
            await client.edit_message(event.chat_id, msg.id, 'Rasmlar, videolar, audiolar va boshqa fayllar yuklandi!')
            await write_details_to_text_file(folder_name, client.iter_messages(chat_entity))
        except ValueError:
            await client.edit_message(event.chat_id, msg.id, 'Chat topilmadi. Iltimos, chat nomini, username ni yoki ID ni to`g`ri kiriting.')
        await client.disconnect()

client.start()
client.run_until_disconnected()
