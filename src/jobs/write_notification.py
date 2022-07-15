def send_notification(email: str, message=''):
    with open('log.txt', mode='a') as email_file:
        content = f'Email: {email} - mensagem: {message}'
        email_file.write(content)