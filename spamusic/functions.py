def playlist_insert(youtube, **kwargs):
    kwargs = {
        'part': 'snippet,status',
        'body': {
            'snippet': {
                'title': 'Nouvelle Playlist',
                'description': 'Une playlist de test',
            },
            'status': {
                'privacyStatus': 'private',
            },
        },
    }
    # This code creates a new, private playlist in the authorized user's channel.
    return youtube.playlists().insert(**kwargs).execute()


def playlist_list(youtube):
    kwargs = {
        'part': 'id,contentDetails,snippet',
        'maxResults': 50,
        'mine': True,
        'fields': 'items(contentDetails,id,snippet)'
    }
    return youtube.playlists().list(**kwargs).execute()