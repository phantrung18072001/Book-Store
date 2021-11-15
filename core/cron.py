from django.core.management import call_command

def backupDB():
    try:
        call_command('dbbackup')
    except:
        pass
